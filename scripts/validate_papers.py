"""Validate structured paper metadata used to generate README.md."""
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PAPERS_FILE = DATA_DIR / "papers.yaml"
EXCLUDED_FILE = DATA_DIR / "excluded.yaml"

REQUIRED_FIELDS = {
    "name",
    "title",
    "paper_url",
    "date",
    "scope",
    "category",
    "abstract",
    "architecture",
    "tokenization",
}

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

ALLOWED_ARCHITECTURES = {
    "Encoder-only",
    "Decoder-only",
    "Encoder-Decoder",
    "Hybrid/SSM",
    "Specialized",
}

ALLOWED_TOKENIZATIONS = {
    "SNT",
    "Codon",
    "K-mer",
    "BPE",
    "Learnable",
    "Expression",
}


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def find_duplicates(records, field):
    seen = {}
    duplicates = []
    for record in records:
        value = record.get(field)
        if not value:
            continue
        if value in seen:
            duplicates.append(value)
        seen[value] = record
    return sorted(set(duplicates))


def validate():
    papers = load_yaml(PAPERS_FILE)
    excluded = load_yaml(EXCLUDED_FILE)
    errors = []

    if not papers:
        errors.append("data/papers.yaml is empty")

    for record in papers:
        name = record.get("name", "<unknown>")
        missing = sorted(REQUIRED_FIELDS - set(record))
        if missing:
            errors.append(f"{name}: missing required fields: {', '.join(missing)}")
        if record.get("scope") not in ALLOWED_SCOPES:
            errors.append(f"{name}: invalid scope {record.get('scope')!r}")
        if record.get("category") not in ALLOWED_CATEGORIES:
            errors.append(f"{name}: invalid category {record.get('category')!r}")
        if record.get("architecture") not in ALLOWED_ARCHITECTURES:
            errors.append(f"{name}: invalid architecture {record.get('architecture')!r}")
        if record.get("tokenization") not in ALLOWED_TOKENIZATIONS:
            errors.append(f"{name}: invalid tokenization {record.get('tokenization')!r}")

    for field in ("name", "title", "paper_url"):
        duplicates = find_duplicates(papers, field)
        if duplicates:
            errors.append(f"duplicate {field}: {', '.join(duplicates)}")

    excluded_names = {record.get("name") for record in excluded}
    overlap = sorted(record["name"] for record in papers if record.get("name") in excluded_names)
    if overlap:
        errors.append(f"papers also listed in excluded.yaml: {', '.join(overlap)}")

    if len(papers) != 45:
        errors.append(f"expected 45 confirmed papers, found {len(papers)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(papers)} confirmed papers and {len(excluded)} excluded entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
