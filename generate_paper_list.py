"""Generate a bullet-list paper index section for the README, with abstracts.
Four classification views: by foundation-model scope, RNA/data focus, architecture,
and tokenization strategy."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import re
from pathlib import Path
from collections import OrderedDict

import yaml

# Model entries live in data/papers.yaml so the README source of truth is
# structured data rather than Python tuples.
DATA_DIR = Path(__file__).resolve().parent / "data"
PAPERS_FILE = DATA_DIR / "papers.yaml"


def load_papers(path=PAPERS_FILE):
    """Load confirmed RNA foundation-model entries from YAML."""
    with open(path, "r", encoding="utf-8") as f:
        records = yaml.safe_load(f) or []

    papers = []
    scope_by_name = {}
    model_details = {}
    required = {
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
    for record in records:
        missing = sorted(required - set(record))
        if missing:
            raise KeyError(f"Missing required fields for {record.get('name', '<unknown>')}: {missing}")
        name = record["name"]
        papers.append((
            name,
            record["title"],
            record["paper_url"],
            record["date"],
            record.get("github_url"),
            record.get("hf_url"),
            record["category"],
            record["abstract"],
            record["architecture"],
            record["tokenization"],
        ))
        scope_by_name[name] = record["scope"]
        model_details[name] = {
            "params": record.get("params", "-"),
            "data": record.get("pretraining_data", "-"),
            "arch": record.get("table_architecture", record["architecture"]),
            "token": record.get("table_tokenization", record["tokenization"]),
        }
    return papers, scope_by_name, model_details


papers, scope_by_name, model_details = load_papers()

benchmarks = [
    ("BEACON", "BEACON: Benchmark for Comprehensive RNA Tasks and Language Models",
     "https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html", "2024.12", "https://github.com/terry-r123/RNABenchmark", None,
     "Introduces BEACON, a comprehensive benchmark covering 13 RNA tasks across structural, functional, and engineering categories for systematic evaluation of RNA language models."),

    ("BEND", "BEND: Benchmarking DNA Language Models on biologically meaningful tasks",
     "https://proceedings.iclr.cc/paper_files/paper/2024/hash/429e7b31625a8b7839f9e4d6e2aa9bb9-Abstract-Conference.html", "2024.05", "https://github.com/frederikkemarin/BEND", None,
     "Proposes BEND, a benchmark of biologically meaningful tasks for evaluating DNA language models, covering gene regulation, chromatin accessibility, and conservation prediction."),

    ("GUE", "DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genome",
     "https://arxiv.org/abs/2306.15006", "2023.06", None, None,
     "Introduces DNABERT-2 along with GUE (Genome Understanding Evaluation), a benchmark of 36 datasets across 9 task categories for evaluating genome foundation models."),

    ("RNA LLM Folding", "Comprehensive benchmarking of large language models for RNA secondary structure prediction",
     "https://academic.oup.com/bib/article/26/2/bbaf137/8109668", "2025.03", "https://github.com/sinc-lab/rna-llm-folding", None,
     "Systematically benchmarks 6 RNA large language models on RNA secondary structure prediction across 4 datasets, revealing performance gaps and limitations of current LLM-based folding approaches."),

    ("RNAGym", "RNAGym: A Benchmark for RNA Fitness and Structure Prediction",
     "https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1", "2025.06", None, None,
     "Presents RNAGym, a benchmark for evaluating RNA foundation models on fitness landscape prediction and 2D/3D structure prediction tasks with standardized evaluation protocols."),

    ("RNAscope", "RNAscope: Comprehensive Benchmark for RNA Foundation Models",
     "https://openreview.net/forum?id=zYAuJxcl2E", "2025.10", None, None,
     "Introduces RNAscope, a comprehensive benchmark with 15 tasks and 1,253 experiments for evaluating RNA foundation models across structure prediction, interaction, and function annotation."),

    ("mRNABench", "mRNABench: Benchmarking Nucleotide FMs on Mature mRNA Tasks",
     "https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1", "2025.07", "https://github.com/morrislab/mRNABench", None,
     "Proposes mRNABench with 10 datasets, 59 tasks, and 135K experiments for benchmarking nucleotide foundation models specifically on mature mRNA prediction tasks including stability and translation efficiency."),

    ("NABench", "NABench: Large-Scale Benchmarks of Nucleotide Foundation Models for Fitness Prediction",
     "https://arxiv.org/html/2511.02888v1", "2025.11", None, None,
     "Introduces NABench, a nucleic acid fitness prediction benchmark with 2.6M+ mutated sequences and 160+ experimental conditions for evaluating foundation models on RNA and DNA fitness landscapes."),

    ("RNA 3D Benchmark", "Comprehensive Benchmark for RNA 3D Structure-Function Modeling",
     "https://arxiv.org/abs/2503.21681", "2025.03", None, None,
     "Presents a comprehensive benchmark for RNA 3D structure-function modeling with 7 tasks across 9 datasets, evaluating how well models capture tertiary structural information for functional prediction."),

    ("Genomic LM RNA Eval", "Benchmarking Pre-trained Genomic Language Models for RNA Predictive Tasks",
     "https://www.nature.com/articles/s41467-025-66899-y", "2025.08", None, None,
     "Systematically benchmarks 11 pre-trained genomic language models on 4 RNA-specific tasks including ncRNA classification, m6A modification, splicing, and translation efficiency prediction."),

    ("DNA FM Benchmark", "Benchmarking DNA Foundation Models for Genomic and Genetic Tasks",
     "https://www.nature.com/articles/s41467-025-65823-8", "2025.07", None, None,
     "Provides a systematic benchmark of DNA foundation models across genomic and genetic tasks, including RNA-relevant tasks, evaluating representational capabilities and transfer learning performance."),

    ("DNALongBench", "DNALongBench: Benchmarking Long-range Genomic Tasks",
     "https://www.nature.com/articles/s41467-025-65077-4", "2025.06", None, None,
     "Introduces DNALongBench, a benchmark of 5 long-range genomic tasks with sequences up to 1M base pairs for evaluating foundation models on long-context genomic understanding."),
]

surveys = [
    ("Comparative Review of RNA LMs", "A Comparative Review of RNA Language Models",
     "https://arxiv.org/abs/2505.09087", "2025.05", None, None,
     "Provides a comparative review of 13 RNA language models, 3 DNA language models, and 1 protein language model, analyzing their architectures, pre-training strategies, and performance across RNA downstream tasks."),

    ("Genome LM Survey", "A Comprehensive Survey of Genome Language Models in Bioinformatics",
     "https://academic.oup.com/bib/article/27/1/bbaf724/8426124", "2026.01", None, None,
     "Surveys genome language models for DNA and RNA, discussing architectural innovations, pre-training strategies, limitations in long-range modeling, and future directions for biological sequence understanding."),

    ("LLMs in Bioinformatics", "Large Language Models in Bioinformatics: A Survey",
     "https://aclanthology.org/2025.findings-acl.184/", "2025.07", None, None,
     "Comprehensive survey of large language models applied to bioinformatics including DNA, RNA, and protein domains, covering model architectures, training paradigms, and applications across biological sequences."),
]

# ============================================================
# Helpers
# ============================================================
def is_preprint_url(url):
    """Return True for preprint-style sources that are not formal publications."""
    formal_exceptions = (
        "doi.org/10.1101/gr.",
    )
    if any(marker in url for marker in formal_exceptions):
        return False
    preprint_markers = (
        "arxiv.org",
        "biorxiv.org",
        "openreview.net",
        "doi.org/10.1101",
        "doi.org/10.64898",
    )
    return any(marker in url for marker in preprint_markers)


status_overrides = {
    "ChaRNABERT": "workshop",
    "RFamLlama": "workshop",
    "Helix-mRNA": "workshop",
}


def entry_status(name, url):
    """Return a compact status label for non-formal or workshop items."""
    if name in status_overrides:
        return status_overrides[name]
    if is_preprint_url(url):
        return "preprint"
    return None


def format_entry(name, title, paper_url, date, github_url, hf_url, abstract):
    """Format a paper entry as a bullet list item with badges."""
    status = entry_status(name, paper_url)
    date_text = f"{date}, {status}" if status else date
    line = f'- **{name}** — [{title}]({paper_url}) ({date_text})'
    line += f' [![abs](https://img.shields.io/badge/abs-{date}-b31b1b.svg)]({paper_url})'
    if status == "preprint":
        line += f' [![preprint](https://img.shields.io/badge/preprint-gray.svg)]({paper_url})'
    if github_url:
        line += f' [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)]({github_url})'
    if hf_url:
        line += f' [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)]({hf_url})'
    line += f'\n\n  > {abstract}\n'
    return line


def group_papers(papers, key_index, label_map, order):
    """Group papers by a field (key_index) and return ordered dict."""
    groups = OrderedDict()
    for key in order:
        groups[key] = []
    for p in papers:
        k = p[key_index]
        if k not in groups:
            groups[k] = []
        groups[k].append(p)
    # Sort within each group by year_month
    for k in groups:
        groups[k].sort(key=lambda x: x[3])
    return groups


def render_view(groups, label_map, description_map=None):
    """Render grouped papers as nested <details open> blocks."""
    lines = []
    for key, entries in groups.items():
        if not entries:
            continue
        label = label_map.get(key, key)
        count = len(entries)
        lines.append(f'<details open>')
        lines.append(f'<summary><b>{label} ({count})</b></summary>')
        lines.append("")
        if description_map and description_map.get(key):
            lines.append(description_map[key])
            lines.append("")
        for p in entries:
            name, title, url, ym, gh, hf = p[0], p[1], p[2], p[3], p[4], p[5]
            abstract = p[7]
            lines.append(format_entry(name, title, url, ym, gh, hf, abstract))
        lines.append("</details>")
        lines.append("")
    return lines


# ============================================================
# Classification configs
# ============================================================

# View 1: By foundation-model scope. This axis answers whether an entry is a
# newly pre-trained RNA FM, a narrower RNA-specific FM, a derivative/adaptation,
# or a related non-RNA-sequence resource.
scope_labels = {
    "core_rna_fm": "Core RNA Foundation Models",
    "specialized_rna_fm": "Specialized RNA Foundation Models",
    "adapted_derived": "Adapted / Derived RNA Models",
    "task_design": "Task-specific / Design-oriented RNA Models",
    "related_nucleotide": "RNA-related Nucleotide / Multi-omics FMs",
    "expression_profile": "Expression-profile Related Models",
}
scope_order = list(scope_labels.keys())
scope_descriptions = {
    "core_rna_fm": "Primary contribution is a reusable RNA or mRNA sequence foundation model pre-trained on raw nucleotide sequences and intended for broad downstream transfer or generation.",
    "specialized_rna_fm": "RNA-specific pre-training is present, but the scope is constrained by RNA subtype, species, structural modality, or a narrow biological question.",
    "adapted_derived": "The work mainly adapts, extends, or composes existing foundation models / pre-trained components for RNA-specific analysis or design, rather than introducing a fully new RNA backbone.",
    "task_design": "Useful RNA models whose main deliverable is a predictor or designer for a specific task, rather than a general reusable foundation-model backbone.",
    "related_nucleotide": "Foundation models for DNA, nucleotide, metagenomic, or multi-omics sequences that are RNA-relevant but not pure RNA sequence FMs.",
    "expression_profile": "Models over RNA-seq expression profiles or multi-omics expression features, not raw RNA nucleotide sequences.",
}
def scope_key(paper):
    name = paper[0]
    if name not in scope_by_name:
        raise KeyError(f"Missing scope classification for {name}")
    return scope_by_name[name]


def group_papers_by_scope(entries):
    groups = OrderedDict((key, []) for key in scope_order)
    for paper in entries:
        groups[scope_key(paper)].append(paper)
    for key in groups:
        groups[key].sort(key=lambda x: x[3])
    return groups


# View 2: By RNA / data focus
rna_type_labels = {
    "ncRNA FM": "ncRNA Sequence Models",
    "mRNA/CDS FM": "mRNA / CDS Sequence Models",
    "UTR FM": "UTR Sequence Models",
    "Specific RNA FM": "Specific RNA Type Models",
    "Structure-aware FM": "Structure-aware RNA Models",
    "Generative FM": "RNA Generative Models",
    "General RNA FM": "General / Other RNA Models",
    "DNA+RNA FM": "DNA+RNA Related Foundation Models",
    "Expression FM": "Expression-based Related Models",
}
rna_type_order = list(rna_type_labels.keys())

# View 3: By Architecture
arch_labels = {
    "Encoder-only": "Encoder-only (BERT-family)",
    "Decoder-only": "Decoder-only (GPT-family)",
    "Encoder-Decoder": "Encoder-Decoder (Seq2Seq)",
    "Hybrid/SSM": "Hybrid / SSM (Mamba, StripedHyena)",
    "Specialized": "Specialized (Diffusion, MoE, GNN, Multimodal)",
}
arch_order = ["Encoder-only", "Decoder-only", "Encoder-Decoder", "Hybrid/SSM", "Specialized"]

# View 4: By Tokenization Strategy
tok_labels = {
    "SNT": "Single Nucleotide Token (SNT)",
    "Codon": "Codon-level Tokenization",
    "K-mer": "K-mer Tokenization",
    "BPE": "Byte Pair Encoding (BPE)",
    "Learnable": "Learnable / Adaptive Tokenization",
    "Expression": "Expression-level Tokenization",
}
tok_order = ["SNT", "Codon", "K-mer", "BPE", "Learnable", "Expression"]

# Detailed table metadata is loaded from data/papers.yaml.
model_table_descriptions = {
    "ncRNA FM": "Models primarily focused on non-coding RNA sequences (from RNAcentral, Rfam, etc.).",
    "mRNA/CDS FM": "Models focused on messenger RNA coding sequences or full mRNA sequences.",
    "UTR FM": "Models focused on untranslated regions (5'UTR, 3'UTR).",
    "Specific RNA FM": "Models targeting specific RNA types or species (splicing, lncRNA, G-quadruplex, plant RNA, RNA families).",
    "Structure-aware FM": "Models incorporating RNA secondary or tertiary structure information during pre-training or inference.",
    "Generative FM": "Models focused on RNA sequence generation or generative transcript modeling.",
    "General RNA FM": "General-purpose RNA models covering multiple RNA types.",
    "DNA+RNA FM": "Nucleotide or biological sequence foundation models with RNA-relevant pre-training data, transcriptomic data, or downstream applications. These are not pure RNA sequence FMs and are listed as related resources.",
    "Expression FM": "Models operating on RNA-seq **gene expression profiles** (not raw nucleotide sequences). Listed for completeness.",
}

benchmark_details = {
    "BEACON": {"focus": "RNA (structural, functional, engineering)", "scale": "13 tasks"},
    "BEND": {"focus": "DNA LM biologically meaningful tasks", "scale": "Multiple tasks"},
    "GUE": {"focus": "Genome understanding evaluation", "scale": "36 datasets, 9 tasks"},
    "RNA LLM Folding": {"focus": "RNA secondary structure prediction", "scale": "6 RNA LLMs, 4 datasets"},
    "RNAGym": {"focus": "RNA fitness & structure prediction (2D/3D)", "scale": "Fitness + structure tasks"},
    "RNAscope": {"focus": "RNA (structure, interaction, function)", "scale": "15 tasks, 1,253 experiments"},
    "mRNABench": {"focus": "Mature mRNA prediction tasks", "scale": "10 datasets, 59 tasks, 135K experiments"},
    "NABench": {"focus": "Nucleic acid fitness prediction", "scale": "2.6M+ mutated seqs, 160+ experiments"},
    "RNA 3D Benchmark": {"focus": "RNA 3D structure-function", "scale": "7 tasks, 9 datasets"},
    "Genomic LM RNA Eval": {"focus": "RNA processes (ncRNA, m6A, splicing, TE)", "scale": "11 genomic LMs, 4 RNA tasks"},
    "DNA FM Benchmark": {"focus": "Genomic & genetic tasks (incl. RNA-relevant)", "scale": "Multiple tasks"},
    "DNALongBench": {"focus": "Long-range genomic tasks", "scale": "5 tasks, up to 1M bp"},
}

survey_details = {
    "Comparative Review of RNA LMs": {"scope": "Compares 13 RNA LMs + 3 DNA LMs + 1 protein LM"},
    "Genome LM Survey": {"scope": "DNA/RNA genome LMs: limitations, long-range modeling"},
    "LLMs in Bioinformatics": {"scope": "LLMs for DNA, RNA, proteins (ACL 2025 Findings, updated 2026)"},
}


def nobr(value):
    if value in (None, "-"):
        return "-"
    return f"<nobr>{value}</nobr>"


def link_cell(label, url):
    if not url:
        return "-"
    return nobr(f"[{label}]({url})")


def code_url(github_url, hf_url):
    return github_url or hf_url


def date_status_cell(date, url, name=None):
    status = entry_status(name, url) if name else ("preprint" if is_preprint_url(url) else None)
    if status:
        return nobr(f"{date}<br><sub>{status}</sub>")
    return nobr(date)


def scope_cell(name):
    return nobr(scope_labels[scope_by_name[name]])


def timeline_date(date):
    return date.replace(".", "-")


def render_model_timeline():
    rows = []
    rows.append("## Model Timeline")
    rows.append("")
    rows.append(f"Auto-generated from `data/papers.yaml` for {len(papers)} confirmed RNA foundation-model entries; it updates whenever confirmed metadata is regenerated.")
    rows.append("")
    rows.append("```mermaid")
    rows.append("timeline")
    rows.append("    title Confirmed RNA Foundation Models")
    for paper in sorted(papers, key=lambda x: x[3]):
        name, title, url, date, github_url, hf_url, category, abstract, arch, token = paper
        rows.append(f"    {timeline_date(date)} : {name}")
    rows.append("```")
    rows.append("")
    rows.append("<details>")
    rows.append("<summary><b>Chronological entries</b></summary>")
    rows.append("")
    rows.append("| Date | Model | Scope | Focus | Paper |")
    rows.append("|:-----|:------|:------|:------|:------|")
    for paper in sorted(papers, key=lambda x: x[3]):
        name, title, url, date, github_url, hf_url, category, abstract, arch, token = paper
        rows.append(
            "| "
            + " | ".join(
                [
                    date_status_cell(date, url, name),
                    nobr(f"**{name}**"),
                    scope_cell(name),
                    nobr(category),
                    link_cell("Paper", url),
                ]
            )
            + " |"
        )
    rows.append("")
    rows.append("</details>")
    rows.append("")
    rows.append("---")
    rows.append("")
    return rows


def render_model_table(entries, label, description):
    rows = []
    rows.append("<details open>")
    rows.append(f"<summary><b>{label}</b></summary>")
    rows.append("")
    rows.append(description)
    rows.append("")
    rows.append("| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |")
    rows.append("|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|")
    for paper in sorted(entries, key=lambda x: x[3]):
        name, title, url, date, github_url, hf_url, category, abstract, arch, token = paper
        details = model_details.get(name, {})
        rows.append(
            "| "
            + " | ".join(
                [
                    nobr(f"**{name}**"),
                    scope_cell(name),
                    link_cell("Paper", url),
                    link_cell("Code", code_url(github_url, hf_url)),
                    date_status_cell(date, url, name),
                    nobr(details.get("arch", arch)),
                    nobr(details.get("params", "-")),
                    nobr(details.get("data", "-")),
                    nobr(details.get("token", token)),
                ]
            )
            + " |"
        )
    rows.append("")
    rows.append("</details>")
    rows.append("")
    return rows


def render_benchmark_table(entries):
    rows = []
    rows.append("<details open>")
    rows.append("<summary><b>Benchmarks & Evaluations</b></summary>")
    rows.append("")
    rows.append("Benchmark datasets and systematic evaluations of RNA / nucleotide foundation models.")
    rows.append("")
    rows.append("| Benchmark <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Date / Status <img width=90/> | Focus <img width=300/> | Scale <img width=220/> |")
    rows.append("|:----------|:-----:|:----:|:----:|:------|:------|")
    for name, title, url, date, github_url, hf_url, abstract in sorted(entries, key=lambda x: x[3]):
        details = benchmark_details.get(name, {})
        rows.append(
            "| "
            + " | ".join(
                [
                    nobr(f"**{name}**"),
                    link_cell("Paper", url),
                    link_cell("Code", code_url(github_url, hf_url)),
                    date_status_cell(date, url, name),
                    nobr(details.get("focus", "-")),
                    nobr(details.get("scale", "-")),
                ]
            )
            + " |"
        )
    rows.append("")
    rows.append("</details>")
    rows.append("")
    return rows


def render_survey_table(entries):
    rows = []
    rows.append("<details open>")
    rows.append("<summary><b>Surveys & Reviews</b></summary>")
    rows.append("")
    rows.append("| Title <img width=350/> | Paper <img width=120/> | Date / Status <img width=90/> | Scope <img width=400/> |")
    rows.append("|:------|:-----:|:----:|:------|")
    for name, title, url, date, github_url, hf_url, abstract in sorted(entries, key=lambda x: x[3]):
        details = survey_details.get(name, {})
        rows.append(
            "| "
            + " | ".join(
                [
                    nobr(f"**{title}**"),
                    link_cell("Paper", url),
                    date_status_cell(date, url, name),
                    nobr(details.get("scope", "-")),
                ]
            )
            + " |"
        )
    rows.append("")
    rows.append("</details>")
    rows.append("")
    return rows


def render_detailed_tables():
    rows = []
    rows.append("## Detailed Tables")
    rows.append("")
    rows.append("<details open>")
    rows.append("<summary><b>RNA Sequence Models</b></summary>")
    rows.append("")
    rows.append("<blockquote>")
    rows.append("")
    grouped_by_type = group_papers(papers, 6, rna_type_labels, rna_type_order)
    for category in rna_type_order:
        if category in ("DNA+RNA FM", "Expression FM"):
            continue
        entries = grouped_by_type.get(category, [])
        if entries:
            rows.extend(render_model_table(entries, rna_type_labels[category], model_table_descriptions[category]))
    rows.append("</blockquote>")
    rows.append("")
    rows.append("</details>")
    rows.append("")
    for category in ("DNA+RNA FM", "Expression FM"):
        entries = grouped_by_type.get(category, [])
        if entries:
            rows.extend(render_model_table(entries, rna_type_labels[category], model_table_descriptions[category]))
    rows.append("<details open>")
    rows.append("<summary><b>Other Materials</b></summary>")
    rows.append("")
    rows.append("<blockquote>")
    rows.append("")
    rows.extend(render_benchmark_table(benchmarks))
    rows.extend(render_survey_table(surveys))
    rows.append("</blockquote>")
    rows.append("")
    rows.append("</details>")
    rows.append("")
    rows.append("---")
    rows.append("")
    rows.append("## Abbreviations")
    rows.append("")
    rows.append("| Abbreviation <img width=120/> | Meaning <img width=400/> |")
    rows.append("|:-------------|:--------|")
    rows.append("| <nobr>**SNT**</nobr> | <nobr>Single Nucleotide Tokenization (A/U/C/G or A/T/C/G)</nobr> |")
    rows.append("| <nobr>**MLM**</nobr> | <nobr>Masked Language Modeling</nobr> |")
    rows.append("| <nobr>**BPE**</nobr> | <nobr>Byte Pair Encoding</nobr> |")
    rows.append("| <nobr>**MoE**</nobr> | <nobr>Mixture of Experts</nobr> |")
    rows.append("| <nobr>**SSM**</nobr> | <nobr>State Space Model</nobr> |")
    rows.append("| <nobr>**CDS**</nobr> | <nobr>Coding Sequence</nobr> |")
    rows.append("| <nobr>**UTR**</nobr> | <nobr>Untranslated Region</nobr> |")
    rows.append("| <nobr>**ncRNA**</nobr> | <nobr>Non-coding RNA</nobr> |")
    rows.append("")
    rows.append("---")
    rows.append("")
    return rows

# ============================================================
# Build output
# ============================================================
lines = []
lines.extend(render_model_timeline())
lines.append("")
lines.append("## Paper List")
lines.append("")
lines.append("A list of RNA foundation models included in this survey. Each entry shows the model/resource name separately from the official paper title. Four classification views are provided below — click to expand/collapse each view.")
lines.append("")
lines.append("<!-- **Classification rules**:")
lines.append("")
lines.append("- **Core RNA Foundation Models**: reusable RNA or mRNA sequence backbones pre-trained on raw nucleotide sequences for broad downstream transfer or generation.")
lines.append("- **Specialized RNA Foundation Models**: RNA-specific pre-trained models whose scope is limited to a subtype, species, structural modality, or narrow biological question.")
lines.append("- **Adapted / Derived RNA Models**: models that adapt, extend, or transfer existing pre-trained components but still yield a reusable RNA language model.")
lines.append("- **Excluded from this strict model list**: downstream-only predictors/designers, reverse-translation or inverse-folding pipelines, RNA 3D prediction systems, broad DNA/nucleotide/multi-omics FMs, and expression-profile models. -->")
lines.append("")
lines.append("> **Date convention**: Dates shown in this section use the official publication or conference month when available; otherwise they use the linked preprint month and are marked `preprint`. Workshop-only entries are marked `workshop`.")
lines.append("")

# Model entries (collapsible wrapper with 4 views inside)
lines.append('<details open>')
lines.append('<summary><b>Models & Related Resources</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")

# --- View 1: By foundation-model scope ---
scope_groups = group_papers_by_scope(papers)
lines.append('<details open>')
lines.append('<summary><b>View 1: Classified by Foundation-model Scope</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(scope_groups, scope_labels, scope_descriptions))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# --- View 2: By RNA / data focus ---
rna_groups = group_papers(papers, 6, rna_type_labels, rna_type_order)
lines.append('<details open>')
lines.append('<summary><b>View 2: Classified by RNA / Data Focus</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(rna_groups, rna_type_labels))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# --- View 3: By Architecture ---
arch_groups = group_papers(papers, 8, arch_labels, arch_order)
lines.append('<details>')
lines.append('<summary><b>View 3: Classified by Architecture</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(arch_groups, arch_labels))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# --- View 4: By Tokenization ---
tok_groups = group_papers(papers, 9, tok_labels, tok_order)
lines.append('<details>')
lines.append('<summary><b>View 4: Classified by Tokenization Strategy</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(tok_groups, tok_labels))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# Other Materials (sibling of Foundation Models)
lines.append('<details open>')
lines.append('<summary><b>Other Materials</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")

# Benchmarks
lines.append('<details open>')
lines.append(f'<summary><b>Benchmarks & Evaluations ({len(benchmarks)})</b></summary>')
lines.append("")
benchmarks.sort(key=lambda x: x[3])
for name, title, url, ym, gh, hf, abstract in benchmarks:
    lines.append(format_entry(name, title, url, ym, gh, hf, abstract))
lines.append("</details>")
lines.append("")

# Surveys
lines.append('<details open>')
lines.append(f'<summary><b>Surveys & Reviews ({len(surveys)})</b></summary>')
lines.append("")
surveys.sort(key=lambda x: x[3])
for name, title, url, ym, gh, hf, abstract in surveys:
    lines.append(format_entry(name, title, url, ym, gh, hf, abstract))
lines.append("</details>")
lines.append("")

lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

lines.extend(render_detailed_tables())

output = "\n".join(lines)
print(output)

# Now inject into README: replace generated Paper List + Detailed Tables content.
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Find and replace existing generated content (stop before Contributing).
generated_start = readme.find("\n## Model Timeline")
if generated_start == -1:
    generated_start = readme.find("\n## Paper List")
contributing_start = readme.find("\n## Contributing")

next_section = contributing_start

if generated_start != -1 and next_section != -1:
    new_readme = readme[:generated_start] + output + "\n" + readme[next_section:]
elif next_section != -1:
    new_readme = readme[:next_section] + output + "\n" + readme[next_section:]
else:
    header = f"""# ✨✨ Awesome RNA Foundation Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Last Update](https://img.shields.io/badge/Last_Update-2026.05-blue.svg)]()

A curated and up-to-date collection of **RNA sequence foundation models**, covering reusable pre-trained language models for non-coding RNA, mRNA/CDS, UTR, structure-aware RNA representations, and generative RNA sequence modeling.

> [!NOTE]
> **Scope.** This README focuses on models that introduce or release reusable RNA/mRNA/CDS/UTR sequence backbones or checkpoints; downstream-only predictors/designers, reverse-translation or inverse-folding pipelines, RNA 3D prediction systems, broad DNA/nucleotide/multi-omics FMs, expression-profile models, and single-cell foundation models (e.g., scGPT, Geneformer) are excluded.

---

## Table of Contents

- [Model Timeline](#model-timeline) — Auto-generated timeline for confirmed RNA foundation models
- [Paper List](#paper-list) — Strict RNA foundation models (4 views), Benchmarks, Surveys
- [Detailed Tables](#detailed-tables) — Detailed tables for all {len(papers)} model entries, {len(benchmarks)} benchmarks, {len(surveys)} surveys
- [Abbreviations](#abbreviations)
- [Contributing](#contributing)

---

"""
    footer = """
## Contributing

Contributions are welcome! If you find a missing RNA foundation model, benchmark, or survey paper, please:

1. Open an issue with the model/paper details
2. Or submit a pull request following the existing table format

**What to include**: RNA sequence foundation models with reusable pre-trained backbones or checkpoints.

**What NOT to include**: Downstream-only predictors/designers, reverse-translation or inverse-folding pipelines, RNA 3D prediction systems, broad DNA/nucleotide/multi-omics FMs, expression-profile models, single-cell foundation models, protein-only models, or purely DNA models.

**Metadata workflow**: confirmed entries live in `data/papers.yaml`, pending discoveries go to `data/candidates.yaml`, and intentionally excluded items are tracked in `data/excluded.yaml`. A scheduled GitHub Action scans recent arXiv, bioRxiv, and Crossref metadata for candidate RNA foundation models and opens a review PR when it finds new items. After editing confirmed metadata, run `python generate_paper_list.py` and `python scripts/validate_papers.py`; CI also checks that generated README content is committed.


*Last updated: May 2026*
"""
    new_readme = header + output.lstrip("\n") + "\n" + footer

new_readme = re.sub(
    r"Detailed tables for all \d+ model entries, \d+ benchmarks, \d+ surveys",
    f"Detailed tables for all {len(papers)} model entries, {len(benchmarks)} benchmarks, {len(surveys)} surveys",
    new_readme,
)
if "- [Model Timeline](#model-timeline)" not in new_readme:
    new_readme = new_readme.replace(
        "- [Paper List](#paper-list) — Strict RNA foundation models (4 views), Benchmarks, Surveys",
        "- [Model Timeline](#model-timeline) — Auto-generated timeline for confirmed RNA foundation models\n"
        "- [Paper List](#paper-list) — Strict RNA foundation models (4 views), Benchmarks, Surveys",
    )
new_readme = new_readme.replace("\n---\n## Paper List", "\n---\n\n## Paper List")
new_readme = new_readme.replace("\n---\n## Model Timeline", "\n---\n\n## Model Timeline")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
print("\n\nSUCCESS: Paper list and detailed tables injected into README.md")
