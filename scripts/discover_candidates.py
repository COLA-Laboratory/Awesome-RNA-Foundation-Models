"""Discover candidate RNA foundation models from public scholarly sources.

The script is intentionally conservative: it searches a small set of official
or near-primary metadata sources, filters likely RNA language/foundation-model
papers, and writes only pending candidates. Confirmed README entries remain
manual-review metadata in data/papers.yaml.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
import re
import time
from pathlib import Path
from typing import Iterable
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PAPERS_FILE = DATA_DIR / "papers.yaml"
EXCLUDED_FILE = DATA_DIR / "excluded.yaml"
CANDIDATES_FILE = DATA_DIR / "candidates.yaml"

USER_AGENT = "Awesome-RNA-Foundation-Models/metadata-discovery"

BROAD_QUERIES = [
    "RNA foundation model",
    "RNA language model",
    "RNA pre-trained model",
    "RNA masked language model",
    "RNA generative language model",
    "RNA sequence foundation model",
    "mRNA foundation model",
    "mRNA language model",
    "codon language model",
    "UTR language model",
    "RNA BERT",
    "RNA GPT",
    "RNA Mamba",
]

RNA_TERMS = (
    "rna",
    "mrna",
    "ncrna",
    "lncrna",
    "utr",
    "codon",
    "transcript",
    "transcriptome",
    "splicing",
    "splice",
)

MODEL_TERMS = (
    "foundation model",
    "language model",
    "pre-trained",
    "pretrained",
    "self-supervised",
    "masked language",
    "bert",
    "gpt",
    "transformer",
    "mamba",
    "state space",
    "encoder",
    "decoder",
)

HIGH_CONFIDENCE_MODEL_TERMS = (
    "foundation model",
    "language model",
    "pre-trained",
    "pretrained",
    "masked language",
    "bert",
    "gpt",
    "mamba",
)

LOW_PRIORITY_TERMS = (
    "single-cell",
    "scrna-seq",
    "rna-seq expression",
    "expression profile",
    "morphology",
    "cellular morphology",
    "inverse folding",
    "reverse translation",
    "3d structure prediction",
    "protein language model",
)

BENCHMARK_TERMS = (
    "benchmark",
    "leaderboard",
    "evaluation",
    "survey",
    "review",
)


@dataclass(frozen=True)
class Candidate:
    title: str
    url: str
    source: str
    date: str
    abstract: str
    query: str


def load_yaml(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def write_yaml(path: Path, records: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(records, f, sort_keys=False, allow_unicode=True, width=120)


def normalize_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"https?://(dx\.)?doi\.org/", "doi:", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_url(value: str | None) -> str:
    if not value:
        return ""
    value = value.strip().rstrip("/")
    value = value.replace("https://doi.org/", "doi:")
    value = value.replace("http://doi.org/", "doi:")
    value = value.replace("https://dx.doi.org/", "doi:")
    return value.lower()


def existing_keys(*record_lists: Iterable[dict]) -> tuple[set[str], set[str]]:
    titles: set[str] = set()
    urls: set[str] = set()
    for records in record_lists:
        for record in records:
            title = record.get("title")
            url = record.get("paper_url") or record.get("url")
            if title:
                titles.add(normalize_text(title))
            if url:
                urls.add(normalize_url(url))
    return titles, urls


def request_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=30) as response:
        return yaml.safe_load(response.read().decode("utf-8"))


def request_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8")


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def query_arxiv(query: str, max_results: int) -> list[Candidate]:
    params = urlencode({
        "search_query": f'all:"{query}"',
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"https://export.arxiv.org/api/query?{params}"
    text = request_text(url)
    root = ET.fromstring(text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    candidates = []
    for entry in root.findall("atom:entry", ns):
        title = compact(entry.findtext("atom:title", default="", namespaces=ns))
        link = compact(entry.findtext("atom:id", default="", namespaces=ns))
        published = compact(entry.findtext("atom:published", default="", namespaces=ns))[:10]
        abstract = compact(entry.findtext("atom:summary", default="", namespaces=ns))
        if title and link:
            candidates.append(Candidate(title, link, "arXiv", published, abstract, query))
    return candidates


def query_biorxiv(from_date: date, to_date: date) -> list[Candidate]:
    candidates = []
    cursor = 0
    while True:
        url = f"https://api.biorxiv.org/details/biorxiv/{from_date.isoformat()}/{to_date.isoformat()}/{cursor}"
        data = request_json(url)
        records = data.get("collection") or []
        if not records:
            break
        for record in records:
            title = compact(record.get("title", ""))
            doi = compact(record.get("doi", ""))
            link = f"https://www.biorxiv.org/content/{doi}v{record.get('version', '1')}" if doi else ""
            published = compact(record.get("date", ""))
            abstract = compact(record.get("abstract", ""))
            if title and link:
                candidates.append(Candidate(title, link, "bioRxiv", published, abstract, "bioRxiv recent RNA/model filter"))
        if len(records) < 100:
            break
        cursor += 100
        time.sleep(0.2)
    return candidates


def parse_candidate_date(value: str) -> date | None:
    if not value:
        return None
    value = value.replace(".", "-")
    for fmt, length in (("%Y-%m-%d", 10), ("%Y-%m", 7), ("%Y", 4)):
        try:
            parsed = datetime.strptime(value[:length], fmt).date()
            return parsed
        except ValueError:
            continue
    return None


def build_queries(confirmed: list[dict]) -> list[str]:
    queries = set(BROAD_QUERIES)
    for record in confirmed:
        name = record.get("name", "")
        category = record.get("category", "")
        title = record.get("title", "")
        text = f"{name} {category} {title}"
        if "BERT" in text:
            queries.add("RNA BERT language model")
        if "GPT" in text:
            queries.add("RNA GPT language model")
        if "Mamba" in text or "SSM" in text or "state space" in text:
            queries.add("RNA state space language model")
        if "mRNA" in text or "CDS" in text or "Codon" in text:
            queries.add("mRNA codon foundation model")
        if "UTR" in text:
            queries.add("UTR foundation model")
        if "structure" in title.lower():
            queries.add("RNA structure-aware language model")
    return sorted(queries)


def query_crossref(query: str, from_date: date, max_results: int) -> list[Candidate]:
    params = urlencode({
        "query.title": query,
        "filter": f"from-pub-date:{from_date.isoformat()}",
        "rows": max_results,
        "sort": "published",
        "order": "desc",
    })
    url = f"https://api.crossref.org/works?{params}"
    data = request_json(url)
    items = data.get("message", {}).get("items", [])
    candidates = []
    for item in items:
        title_values = item.get("title") or []
        title = compact(title_values[0] if title_values else "")
        doi = compact(item.get("DOI", ""))
        link = f"https://doi.org/{doi}" if doi else compact(item.get("URL", ""))
        date_parts = item.get("published-print", item.get("published-online", item.get("created", {}))).get("date-parts", [[]])
        parts = date_parts[0] if date_parts else []
        published = ".".join(str(part).zfill(2) if idx else str(part) for idx, part in enumerate(parts[:2]))
        abstract = compact(re.sub(r"<[^>]+>", " ", item.get("abstract", "")))
        if title and link:
            candidates.append(Candidate(title, link, "Crossref", published, abstract, query))
    return candidates


def score_candidate(candidate: Candidate) -> tuple[int, list[str]]:
    text = normalize_text(f"{candidate.title} {candidate.abstract}")
    score = 0
    evidence = []
    for term in RNA_TERMS:
        if term in text:
            score += 2
            evidence.append(term)
    for term in MODEL_TERMS:
        if term in text:
            score += 2
            evidence.append(term)
    if "foundation model" in text or "language model" in text:
        score += 2
    for term in LOW_PRIORITY_TERMS:
        if term in text:
            score -= 2
            evidence.append(f"low-priority:{term}")
    return score, sorted(set(evidence))


def is_likely_new_model(candidate: Candidate) -> bool:
    title = normalize_text(candidate.title)
    text = normalize_text(f"{candidate.title} {candidate.abstract}")
    has_rna = any(term in text for term in RNA_TERMS)
    has_high_confidence_model_term = any(term in text for term in HIGH_CONFIDENCE_MODEL_TERMS)
    if not (has_rna and has_high_confidence_model_term):
        return False
    if any(term in title for term in LOW_PRIORITY_TERMS):
        return False
    if any(term in title for term in BENCHMARK_TERMS):
        return False
    if any(term in text for term in ("single cell", "single-cell", "scrna seq", "expression profile")):
        return False
    return True


def infer_model_name(title: str) -> str:
    prefix = title.split(":", 1)[0].strip()
    if 1 <= len(prefix.split()) <= 3:
        return prefix
    match = re.search(r"\b([A-Z][A-Za-z0-9.-]*(?:RNA|mRNA|BERT|GPT|FM|Mamba)[A-Za-z0-9.-]*)\b", title)
    if match and match.group(1).lower() != "rna":
        return match.group(1)
    match = re.search(r"\b([A-Z0-9][A-Z0-9.-]{2,})\b", title)
    if match:
        return match.group(1)
    return "-"


def suggest_scope_and_category(candidate: Candidate) -> tuple[str, str]:
    text = normalize_text(candidate.title)
    if "utr" in text:
        return "specialized_rna_fm", "UTR FM"
    if "mrna" in text or "codon" in text or "coding sequence" in text:
        return "core_rna_fm", "mRNA/CDS FM"
    if "generate" in text or "generative" in text or "design" in text:
        return "core_rna_fm", "Generative FM"
    if "splice" in text or "lncrna" in text or "plant" in text:
        return "specialized_rna_fm", "Specific RNA FM"
    if "structure" in text or "secondary" in text:
        return "specialized_rna_fm", "Structure-aware FM"
    return "core_rna_fm", "General RNA FM"


def candidate_to_record(candidate: Candidate, evidence: list[str]) -> dict:
    scope, category = suggest_scope_and_category(candidate)
    date_value = candidate.date[:7].replace("-", ".") if candidate.date else ""
    status = "preprint" if candidate.source in {"arXiv", "bioRxiv"} else "published_or_indexed"
    return {
        "name": infer_model_name(candidate.title),
        "title": candidate.title,
        "url": candidate.url,
        "source": candidate.source,
        "date": date_value,
        "status": "pending_review",
        "publication_status": status,
        "suggested_scope": scope,
        "suggested_category": category,
        "reason": "Matched RNA sequence and language/foundation-model terms; needs manual review before README inclusion.",
        "matched_terms": evidence,
        "discovery_query": candidate.query,
        "discovered_at": datetime.now(timezone.utc).date().isoformat(),
    }


def discover(lookback_days: int, max_results: int, min_score: int) -> list[dict]:
    confirmed = load_yaml(PAPERS_FILE)
    excluded = load_yaml(EXCLUDED_FILE)
    existing_candidates = load_yaml(CANDIDATES_FILE)
    known_titles, known_urls = existing_keys(confirmed, excluded, existing_candidates)

    from_date = datetime.now(timezone.utc).date() - timedelta(days=lookback_days)
    to_date = datetime.now(timezone.utc).date()
    raw_candidates: list[Candidate] = []

    def extend_from_source(label: str, fetch) -> None:
        try:
            raw_candidates.extend(fetch())
        except Exception as exc:  # Network services should not block all discovery.
            print(f"WARNING: {label} discovery failed: {exc}")

    queries = build_queries(confirmed)
    for query in queries:
        extend_from_source(f"arXiv query {query!r}", lambda query=query: query_arxiv(query, max_results))
        time.sleep(0.2)
    extend_from_source("bioRxiv recent scan", lambda: query_biorxiv(from_date, to_date))
    for query in queries[:10]:
        extend_from_source(f"Crossref query {query!r}", lambda query=query: query_crossref(query, from_date, max_results))
        time.sleep(0.2)

    new_records = []
    seen_titles = set(known_titles)
    seen_urls = set(known_urls)
    for candidate in raw_candidates:
        title_key = normalize_text(candidate.title)
        url_key = normalize_url(candidate.url)
        if title_key in seen_titles or url_key in seen_urls:
            continue
        candidate_date = parse_candidate_date(candidate.date)
        if candidate_date and candidate_date < from_date:
            continue
        score, evidence = score_candidate(candidate)
        if score < min_score:
            continue
        if not is_likely_new_model(candidate):
            continue
        record = candidate_to_record(candidate, evidence)
        record["score"] = score
        new_records.append(record)
        seen_titles.add(title_key)
        seen_urls.add(url_key)

    return sorted(new_records, key=lambda record: (record.get("date") or "", record["title"]), reverse=True)


def merge_candidates(existing: list[dict], discovered: list[dict]) -> list[dict]:
    title_keys, url_keys = existing_keys(existing)
    merged = list(existing)
    for record in discovered:
        title_key = normalize_text(record["title"])
        url_key = normalize_url(record["url"])
        if title_key in title_keys or url_key in url_keys:
            continue
        merged.append(record)
        title_keys.add(title_key)
        url_keys.add(url_key)
    return sorted(merged, key=lambda record: (record.get("discovered_at") or "", record.get("date") or "", record["title"]), reverse=True)


def print_summary(records: list[dict]) -> None:
    if not records:
        print("No new candidate RNA foundation models found.")
        return
    print(f"Found {len(records)} new candidate(s):")
    for record in records:
        print(f"- {record['name']} | {record['title']} | {record['date']} | {record['source']} | {record['url']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lookback-days", type=int, default=60)
    parser.add_argument("--max-results", type=int, default=20)
    parser.add_argument("--min-score", type=int, default=6)
    parser.add_argument("--update", action="store_true", help="Merge discoveries into data/candidates.yaml")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    discovered = discover(args.lookback_days, args.max_results, args.min_score)
    print_summary(discovered)
    if args.update and discovered:
        existing = load_yaml(CANDIDATES_FILE)
        write_yaml(CANDIDATES_FILE, merge_candidates(existing, discovered))
        print(f"Updated {CANDIDATES_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
