"""Auto-classify discovered RNA foundation-model candidates.

This script converts high-confidence entries in data/candidates.yaml into
draft records in data/papers.yaml so the normal README and timeline generation
path can update them. The generated records are intentionally conservative and
marked with review_status: auto_classified for PR review before merging.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.discover_candidates import (
    CANDIDATES_FILE,
    PAPERS_FILE,
    infer_model_name,
    load_yaml,
    normalize_text,
    normalize_url,
    write_yaml,
)


ALLOWED_SCOPES = {
    "core_rna_fm",
    "specialized_rna_fm",
    "adapted_derived",
    "task_design",
    "related_nucleotide",
    "expression_profile",
}

ALLOWED_CATEGORIES = {
    "ncRNA FM",
    "mRNA/CDS FM",
    "UTR FM",
    "Specific RNA FM",
    "Structure-aware FM",
    "Generative FM",
    "General RNA FM",
    "DNA+RNA FM",
    "Expression FM",
}


def compact(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def first_sentence(value: str | None, max_chars: int = 340) -> str:
    text = compact(value)
    if not text:
        return ""
    match = re.search(r"(.+?[.!?])(?:\s|$)", text)
    sentence = match.group(1) if match else text
    if len(sentence) <= max_chars:
        return sentence
    return sentence[: max_chars - 3].rstrip() + "..."


def infer_architecture(record: dict) -> tuple[str, str]:
    text = normalize_text(f"{record.get('title', '')} {record.get('abstract', '')}")
    if any(term in text for term in ("mamba", "state space", "stripedhyena", "retnet", "retentive")):
        return "Hybrid/SSM", "Hybrid / SSM"
    if any(term in text for term in ("encoder decoder", "encoder-decoder", "seq2seq", "sequence to sequence")):
        return "Encoder-Decoder", "Encoder-Decoder"
    if any(term in text for term in ("diffusion", "mixture of experts", "moe", "multimodal", "graph neural", "gnn")):
        return "Specialized", "Specialized"
    if any(term in text for term in ("gpt", "llama", "autoregressive", "decoder only", "decoder-only", "generation", "generative", "design")):
        return "Decoder-only", "Decoder-only"
    return "Encoder-only", "Encoder-only"


def infer_tokenization(record: dict) -> tuple[str, str]:
    text = normalize_text(f"{record.get('title', '')} {record.get('abstract', '')}")
    if any(term in text for term in ("codon", "coding sequence", "coding constraint", "cds")):
        return "Codon", "Codon-level"
    if any(term in text for term in ("k mer", "k-mer", "3 mer", "3-mer", "5 mer", "5-mer")):
        return "K-mer", "K-mer"
    if any(term in text for term in ("byte pair", "bpe")):
        return "BPE", "BPE"
    if any(term in text for term in ("adaptive token", "learnable token", "character level", "character-level")):
        return "Learnable", "Learnable / adaptive"
    return "SNT", "SNT"


def normalized_existing(records: list[dict]) -> tuple[set[str], set[str], set[str]]:
    names = {normalize_text(record.get("name", "")) for record in records if record.get("name")}
    titles = {normalize_text(record.get("title", "")) for record in records if record.get("title")}
    urls = {normalize_url(record.get("paper_url") or record.get("url")) for record in records if record.get("paper_url") or record.get("url")}
    return names, titles, urls


def candidate_is_promotable(record: dict) -> bool:
    scope = record.get("suggested_scope")
    category = record.get("suggested_category")
    if scope not in ALLOWED_SCOPES:
        return False
    if category not in ALLOWED_CATEGORIES:
        return False
    return bool(record.get("title") and record.get("url") and record.get("date"))


def candidate_to_paper(record: dict) -> dict:
    architecture, table_architecture = infer_architecture(record)
    tokenization, table_tokenization = infer_tokenization(record)
    title = compact(record["title"])
    abstract = first_sentence(record.get("abstract")) or compact(record.get("reason"))
    if not abstract:
        abstract = f"Auto-classified RNA foundation-model candidate discovered from {record.get('source', 'source metadata')}."
    name = compact(record.get("name")) if record.get("name") and record.get("name") != "-" else infer_model_name(title)
    source = record.get("source", "")
    paper_url = record["url"]
    paper = {
        "name": name,
        "title": title,
        "paper_url": paper_url,
        "date": record["date"],
        "github_url": None,
        "hf_url": None,
        "scope": record["suggested_scope"],
        "category": record["suggested_category"],
        "abstract": abstract,
        "architecture": architecture,
        "tokenization": tokenization,
        "table_architecture": table_architecture,
        "params": "-",
        "pretraining_data": "-",
        "table_tokenization": table_tokenization,
        "review_status": "auto_classified",
        "discovered_at": record.get("discovered_at"),
    }
    if source in {"arXiv", "bioRxiv"}:
        paper["timeline_url"] = paper_url
    return paper


def write_candidates(records: list[dict]) -> None:
    if records:
        write_yaml(CANDIDATES_FILE, records)
    else:
        CANDIDATES_FILE.write_text("# Newly discovered candidates pending manual review.\n[]\n", encoding="utf-8")


def classify_candidates(update: bool) -> int:
    papers = load_yaml(PAPERS_FILE)
    candidates = load_yaml(CANDIDATES_FILE)
    known_names, known_titles, known_urls = normalized_existing(papers)

    promoted = []
    remaining = []
    for candidate in candidates:
        name_key = normalize_text(candidate.get("name", ""))
        title_key = normalize_text(candidate.get("title", ""))
        url_key = normalize_url(candidate.get("url"))
        already_known = name_key in known_names or title_key in known_titles or url_key in known_urls
        if already_known:
            continue
        if not candidate_is_promotable(candidate):
            remaining.append(candidate)
            continue
        paper = candidate_to_paper(candidate)
        promoted.append(paper)
        known_names.add(normalize_text(paper["name"]))
        known_titles.add(normalize_text(paper["title"]))
        known_urls.add(normalize_url(paper["paper_url"]))

    if not promoted:
        print("No promotable candidate records found.")
        return 0

    print(f"Auto-classified {len(promoted)} candidate(s):")
    for paper in promoted:
        print(f"- {paper['name']} | {paper['title']} | {paper['date']} | {paper['scope']} | {paper['category']}")

    if update:
        write_yaml(PAPERS_FILE, papers + promoted)
        write_candidates(remaining)
        print("Updated data/papers.yaml and data/candidates.yaml")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update", action="store_true", help="Write auto-classified candidates into data/papers.yaml")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return classify_candidates(args.update)


if __name__ == "__main__":
    raise SystemExit(main())
