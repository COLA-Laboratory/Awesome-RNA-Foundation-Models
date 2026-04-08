"""Generate a bullet-list paper index section for the README."""

# (name, paper_title, paper_url, year_month, github_url, hf_url, category)
papers = [
    # === ncRNA FMs ===
    ("RNABert", "Informative RNA-base embedding for RNA structural alignment and clustering by a representation learning framework",
     "https://doi.org/10.1093/nargab/lqac012", "2022.02", "https://github.com/mana438/RNABERT", None, "ncRNA FM"),
    ("RNAFM", "Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions",
     "https://arxiv.org/abs/2204.00300", "2022.08", None, "https://huggingface.co/multimolecule/rnafm", "ncRNA FM"),
    ("RNAMSM", "Multiple sequence-alignment-based RNA language model and its application to structural inference",
     "https://doi.org/10.1093/nar/gkad1031", "2023.12", "https://github.com/yikunpku/RNA-MSM", None, "ncRNA FM"),
    ("RNA-km", "RNA-km: a tool for predicting RNA sequence properties using k-mer frequency features",
     "https://doi.org/10.1101/2024.01.27.577533", "2024.01", "https://github.com/gongtiansu/RNA-km", None, "ncRNA FM"),
    ("RNAErnie", "RNAErnie: An RNA language model with structure-enhanced representations",
     "https://www.nature.com/articles/s42256-024-00836-4", "2024.05", None, "https://huggingface.co/LLM-EDA/RNAErnie", "ncRNA FM"),
    ("ERNIE-RNA", "ERNIE-RNA: An RNA Language Model with Structure-enhanced Representations",
     "https://doi.org/10.1101/2024.03.17.585376", "2024.10", None, "https://huggingface.co/multimolecule/ernierna-ss", "ncRNA FM"),
    ("DGRNA", "DGRNA: a long-context RNA foundation model with bidirectional Mamba2",
     "https://doi.org/10.1101/2024.10.31.621427", "2024.10", None, None, "ncRNA FM"),
    ("ChaRNABERT", "ChaRNABERT: A pre-trained RNA language model with learnable tokenization",
     "https://arxiv.org/abs/2411.11808", "2024.11", None, None, "ncRNA FM"),
    ("AIDO.RNA", "AIDO.RNA: A Scalable RNA Foundation Model",
     "https://doi.org/10.1101/2024.11.28.625345", "2024.11", None, "https://huggingface.co/genbio-ai/AIDO.RNA-1.6B", "ncRNA FM"),
    ("BiRNA-BERT", "BiRNA-BERT: An Efficient RNA Language Model with Adaptive Dual Tokenization",
     "https://doi.org/10.1101/2024.07.02.601703", "2025.08", "https://github.com/buetnlpbio/BiRNA-BERT", None, "ncRNA FM"),
    ("RNA-BERTa", "DLRNA-BERTa: A Transformer for RNA-Drug Binding Affinity Prediction",
     "https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1", "2025.09", None, "https://huggingface.co/IlPakoZ/RNA-BERTa9700", "ncRNA FM"),
    ("RiNALMo", "RiNALMo: General-Purpose RNA Language Models Can Generalize Well on Structure Prediction Tasks",
     "https://arxiv.org/abs/2403.00043", "2025.07", "https://github.com/lbcb-sci/RiNALMo", None, "ncRNA FM"),
    ("RNAGenesis", "RNAGenesis: A Generative RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2", "2024.12", None, "https://huggingface.co/Zaixi/RNAGenesis", "ncRNA FM"),
    ("HydraRNA", "HydraRNA: An Efficient RNA Foundation Model via Hybrid SSM and Attention",
     "https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7", "2025.03", "https://github.com/GuipengLi/HydraRNA", None, "ncRNA FM"),
    ("RNAElectra", "RNAElectra: An ELECTRA-style RNA Foundation Model",
     "https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full", "2026.03", None, None, "ncRNA FM"),

    # === mRNA/CDS FMs ===
    ("CodonBERT", "CodonBERT: Large Language Models for mRNA Unimodal and Multimodal Molecular Learning",
     "https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1", "2023.09", "https://github.com/Sanofi-Public/CodonBERT", None, "mRNA/CDS FM"),
    ("CaLM", "CaLM: Codon Adaptation Language Model for mRNA Design",
     "https://www.nature.com/articles/s42256-024-00791-0", "2024.02", "https://github.com/oxpig/CaLM", None, "mRNA/CDS FM"),
    ("HELM", "HELM: Hierarchical Encoding for mRNA Language Modeling",
     "https://arxiv.org/abs/2410.12459", "2025.01", None, None, "mRNA/CDS FM"),
    ("Helix-mRNA", "Helix-mRNA: A Hybrid SSM-Attention Model for mRNA",
     "https://arxiv.org/abs/2502.13785", "2025.02", None, "https://huggingface.co/helical-ai/helix-mRNA", "mRNA/CDS FM"),
    ("GEMORNA", "GEMORNA: Generative mRNA Design via Codon and UTR Optimization",
     "https://www.science.org/doi/10.1126/science.adr8470", "2025.05", "https://github.com/RainaBio/GEMORNA", None, "mRNA/CDS FM"),
    ("GenSLM", "GenSLMs: Genome-scale Language Models Reveal SARS-CoV-2 Evolutionary Dynamics",
     "https://doi.org/10.1177/10943420231201154", "2023.01", None, None, "mRNA/CDS FM"),
    ("mRNABERT", "mRNABERT: A Pre-trained Language Model for mRNA Sequences",
     "https://www.nature.com/articles/s41467-025-65340-8", "2025.11", None, "https://huggingface.co/Taykhoom/mRNABERT-no-flashattention", "mRNA/CDS FM"),
    ("mRNA-GPT", "mRNA-GPT: An Autoregressive mRNA Foundation Model across Three Domains of Life",
     "https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1", "2025.12", "https://github.com/ZHymLumine/mRNA-GPT/", None, "mRNA/CDS FM"),
    ("NUWA", "NUWA: A Codon Language Model for mRNA Coding Sequences",
     "https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3", "2026.02", "https://github.com/zysxmu/NUWA", None, "mRNA/CDS FM"),
    ("mRNA-GPT (full-length)", "mRNA-GPT: Full-Length mRNA Design via Autoregressive Generation with PPO",
     "https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1", "2026.03", None, None, "mRNA/CDS FM"),
    ("CodonMoE", "CodonMoE: Adapting DNA Language Models for RNA via Mixture-of-Experts",
     "https://openreview.net/forum?id=TOUrnb1EaG", "2026.01", None, None, "mRNA/CDS FM"),

    # === UTR FMs ===
    ("UTR-LM", "UTR-LM: A 5' UTR Language Model for Predicting Translation Efficiency",
     "https://www.nature.com/articles/s42256-024-00823-9", "2024.04", None, "https://huggingface.co/multimolecule/utrlm-te_el", "UTR FM"),
    ("3UTRBert", "3UTRBERT: Pre-trained Language Model for 3' UTR Sequences",
     "https://doi.org/10.1101/2023.09.08.556883", "2024.07", "https://github.com/yangyn533/3UTRBERT", None, "UTR FM"),

    # === Specific RNA FMs ===
    ("SpliceBERT", "SpliceBERT: A Pre-trained Model for Self-supervised Learning of Pre-mRNA Splicing",
     "https://doi.org/10.1093/bib/bbae163", "2023.01", "https://github.com/chenkenbio/SpliceBERT", None, "Specific RNA FM"),
    ("RFamLlama", "RFamLlama: Conditional RNA Generation by RNA Family",
     "https://openreview.net/forum?id=dXnQedxEJD", "2024.08", None, "https://huggingface.co/jinyuan22/RFamLlama-base", "Specific RNA FM"),
    ("PlantRNA-FM", "PlantRNA-FM: A Plant RNA Foundation Model from Multi-species Transcriptomes",
     "https://www.nature.com/articles/s42256-024-00946-z", "2024.12", None, "https://huggingface.co/yangheng/PlantRNA-FM", "Specific RNA FM"),
    ("LncRNA-BERT", "LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification",
     "https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1", "2025.01", "https://github.com/luukromeijn/lncRNA-Py", None, "Specific RNA FM"),
    ("G4mer", "G4mer: An Interpretable Transformer for G-quadruplex Prediction in the Transcriptome",
     "https://www.nature.com/articles/s41467-025-65020-7", "2025.12", None, "https://huggingface.co/Biociphers/g4mer", "Specific RNA FM"),

    # === Structure-aware RNA FMs ===
    ("ATOM-1", "ATOM-1: Augmented Transformer with Structure-aware Chemical Mapping",
     "https://doi.org/10.1101/2023.12.13.571579", "2023.12", None, None, "Structure-aware FM"),
    ("Ribonanza", "RibonanzaNet: Deep Learning for RNA Chemical Mapping Prediction",
     "https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1", "2024.02", "https://github.com/Shujun-He/RibonanzaNet", None, "Structure-aware FM"),
    ("OmniGenome", "OmniGenome: Aligning RNA Sequences with Secondary Structures",
     "https://arxiv.org/abs/2407.11242", "2024.07", None, "https://huggingface.co/yangheng/OmniGenome-186M", "Structure-aware FM"),
    ("MP-RNA", "MP-RNA: Multi-Purpose RNA Foundation Model with Structure Awareness",
     "https://aclanthology.org/2024.findings-emnlp.304/", "2024.11", None, "https://huggingface.co/yangheng/MP-RNA", "Structure-aware FM"),
    ("RNA-TorsionBERT", "RNA-TorsionBERT: Predicting RNA Backbone Torsion Angles",
     "https://doi.org/10.1093/bioinformatics/btaf004", "2025.01", None, "https://huggingface.co/sayby/rna_torsionBERT", "Structure-aware FM"),
    ("StructRFM", "StructRFM: Structure-guided RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1", "2025.08", "https://github.com/heqin-zhu/structRFM", None, "Structure-aware FM"),

    # === Generative FMs ===
    ("LoRNA", "LoRNA: A Long-read RNA Foundation Model",
     "https://doi.org/10.1101/2024.08.26.609813", "2024.08", None, None, "Generative FM"),
    ("GenerRNA", "GenerRNA: A Generative Pre-trained Autoregressive RNA Language Model",
     "https://doi.org/10.1371/journal.pone.0310814", "2024.10", None, "https://huggingface.co/pfnet/GenerRNA", "Generative FM"),
    ("GARNET", "GARNET: A Generative RNA Design Model from Microbial Genomes",
     "https://www.nature.com/articles/s41467-024-54812-y", "2024.12", "https://github.com/Doudna-lab/GARNET_DL", None, "Generative FM"),
    ("RNAtranslator", "RNAtranslator: Protein-conditioned RNA Sequence Generation",
     "https://doi.org/10.1371/journal.pcbi.1013541", "2025.03", None, "https://huggingface.co/SobhanShukueian/rnatranslator", "Generative FM"),
    ("EVA", "EVA: Evolutionary Versatile Architect for Long-context RNA Generation",
     "https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2", "2026.03", None, None, "Generative FM"),

    # === General / Other ===
    ("Uni-RNA", "Uni-RNA: Universal Pre-trained Models for RNA across Species",
     "https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1", "2023.07", "https://github.com/ComDec/unirna_tf", None, "General RNA FM"),
    ("RNALens", "RNALens: A Multi-task RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1", "2025.07", "https://github.com/oomics/RNALens", None, "General RNA FM"),
    ("OPED", "OPED: Transformer-based pegRNA Editing Efficiency Prediction",
     "https://www.nature.com/articles/s42256-023-00739-w", "2023.10", "https://github.com/wenjiegroup/OPED", None, "General RNA FM"),

    # === DNA+RNA FMs ===
    ("Evo", "Sequence Modeling and Design from Molecular to Genome Scale with Evo",
     "https://www.science.org/doi/10.1126/science.ado9336", "2024.02", "https://github.com/evo-design/evo", None, "DNA+RNA FM"),
    ("LucaOne", "LucaOne: A Unified Foundation Model for DNA, RNA and Protein",
     "https://www.nature.com/articles/s42256-025-01044-4", "2024.05", "https://github.com/LucaOne/LucaOne", None, "DNA+RNA FM"),
    ("BSM", "BSM: Biological Sequence Model for Mixed-modal Pretraining",
     "https://arxiv.org/abs/2410.11499", "2024.10", None, None, "DNA+RNA FM"),
    ("LAMAR", "LAMAR: A Language Model for Mammalian and Viral Genomes and Transcriptomes",
     "https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1", "2024.10", "https://github.com/zhw-e8/LAMAR", None, "DNA+RNA FM"),
    ("Orthrus", "Orthrus: Contrastive Learning of Transcript Isoforms and Orthologs via Mamba",
     "https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3", "2024.10", None, "https://huggingface.co/quietflamingo/orthrus-large-4-track", "DNA+RNA FM"),
    ("METAGENE-1", "METAGENE-1: A 7B Metagenomic Foundation Model for DNA and RNA",
     "https://arxiv.org/abs/2501.02045", "2025.01", None, "https://huggingface.co/metagene-ai/METAGENE-1", "DNA+RNA FM"),
    ("Life-Code", "Life-Code: A Unified Foundation Model via Central Dogma",
     "https://arxiv.org/abs/2502.07299", "2025.02", None, None, "DNA+RNA FM"),
    ("Evo 2", "Genome Modeling and Design Across All Domains of Life with Evo 2",
     "https://www.nature.com/articles/s41586-026-10176-5", "2026.02", "https://github.com/ArcInstitute/evo2", None, "DNA+RNA FM"),
    ("OmniNA", "OmniNA: A Foundation Model for Nucleotide Sequences and Annotations",
     "https://academic.oup.com/nar/article/54/6/gkag083/8528802", "2026.01", None, None, "DNA+RNA FM"),
    ("EDEN", "EDEN: A 28B Foundation Model for Programmable Gene Insertion",
     "https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1", "2026.01", None, None, "DNA+RNA FM"),

    # === Expression-based FMs ===
    ("BulkRNABert", "BulkRNABert: A Pre-trained Model for Bulk RNA-seq Expression Data",
     "https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2", "2024.06", None, "https://huggingface.co/InstaDeepAI/BulkRNABert", "Expression FM"),
    ("MOJO", "MOJO: A Multi-omics Foundation Model for RNA-seq and Methylation",
     "https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1", "2025.06", None, "https://huggingface.co/InstaDeepAI/MOJO", "Expression FM"),
]

benchmarks = [
    ("BEACON", "BEACON: Benchmark for Comprehensive RNA Tasks and Language Models",
     "https://arxiv.org/abs/2406.10391", "2024.06", "https://github.com/terry-r123/RNABenchmark", None),
    ("BEND", "BEND: Benchmarking DNA Language Models on Biologically Meaningful Tasks",
     "https://arxiv.org/abs/2311.12570", "2024.01", "https://github.com/frederikkemarin/BEND", None),
    ("GUE", "DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genome",
     "https://arxiv.org/abs/2306.15006", "2023.06", None, None),
    ("RNA LLM Folding", "Comprehensive Benchmarking of LLMs for RNA Secondary Structure Prediction",
     "https://arxiv.org/abs/2410.16212", "2024.10", "https://github.com/sinc-lab/rna-llm-folding", None),
    ("RNAGym", "RNAGym: A Benchmark for RNA Fitness and Structure Prediction",
     "https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1", "2025.06", None, None),
    ("RNAscope", "RNAscope: Comprehensive Benchmark for RNA Foundation Models",
     "https://openreview.net/forum?id=zYAuJxcl2E", "2025.10", None, None),
    ("mRNABench", "mRNABench: Benchmarking Nucleotide FMs on Mature mRNA Tasks",
     "https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1", "2025.07", "https://github.com/morrislab/mRNABench", None),
    ("NABench", "NABench: Nucleic Acid Fitness Prediction Benchmark",
     "https://arxiv.org/html/2511.02888v1", "2025.11", None, None),
    ("RNA 3D Benchmark", "Comprehensive Benchmark for RNA 3D Structure-Function Modeling",
     "https://arxiv.org/abs/2503.21681", "2025.03", None, None),
    ("Genomic LM RNA Eval", "Benchmarking Pre-trained Genomic Language Models for RNA Predictive Tasks",
     "https://www.nature.com/articles/s41467-025-66899-y", "2025.08", None, None),
    ("DNA FM Benchmark", "Benchmarking DNA Foundation Models for Genomic and Genetic Tasks",
     "https://www.nature.com/articles/s41467-025-65823-8", "2025.07", None, None),
    ("DNALongBench", "DNALongBench: Benchmarking Long-range Genomic Tasks",
     "https://www.nature.com/articles/s41467-025-65077-4", "2025.06", None, None),
]

surveys = [
    ("Comparative Review of RNA LMs", "A Comparative Review of RNA Language Models",
     "https://arxiv.org/abs/2505.09087", "2025.05", None, None),
    ("Genome LM Survey", "A Comprehensive Survey of Genome Language Models in Bioinformatics",
     "https://academic.oup.com/bib/article/27/1/bbaf724/8426124", "2026.01", None, None),
    ("LLMs in Bioinformatics", "Large Language Models in Bioinformatics: A Survey",
     "https://arxiv.org/abs/2503.04490", "2026.03", None, None),
]

def make_badges(paper_url, year_month, github_url, hf_url):
    parts = []
    parts.append(f'[![abs](https://img.shields.io/badge/abs-{year_month}-b31b1b.svg)](https://img.shields.io/badge/abs-{year_month}-b31b1b.svg)')
    # Actually the abs badge should link to the paper
    # and the date badge is separate
    return parts

def format_entry(name, title, paper_url, year_month, github_url, hf_url):
    """Format: - [Title](paper_url) ![abs](badge) ![date](badge) ![github](badge) ![hf](badge)"""
    line = f'- [{title}]({paper_url})'
    # abs + date badge (combined)
    line += f' [![abs](https://img.shields.io/badge/abs-{year_month}-b31b1b.svg)]({paper_url})'
    # github badge
    if github_url:
        line += f' [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)]({github_url})'
    # hf badge
    if hf_url:
        line += f' [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)]({hf_url})'
    return line

# Group papers by category
from collections import OrderedDict
categories = OrderedDict()
for name, title, url, ym, gh, hf, cat in papers:
    if cat not in categories:
        categories[cat] = []
    categories[cat].append((name, title, url, ym, gh, hf))

lines = []
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Paper List")
lines.append("")
lines.append("A complete chronological list of all papers included in this survey.")
lines.append("")

# Foundation Models by category
lines.append("### Foundation Models")
lines.append("")

cat_labels = {
    "ncRNA FM": "ncRNA Foundation Models",
    "mRNA/CDS FM": "mRNA / CDS Foundation Models",
    "UTR FM": "UTR Foundation Models",
    "Specific RNA FM": "Specific RNA Type Models",
    "Structure-aware FM": "Structure-aware RNA Models",
    "Generative FM": "RNA Generative Models",
    "General RNA FM": "General / Other RNA Models",
    "DNA+RNA FM": "DNA+RNA Foundation Models",
    "Expression FM": "Expression-based Foundation Models",
}

for cat, entries in categories.items():
    label = cat_labels.get(cat, cat)
    lines.append(f"**{label}**")
    lines.append("")
    # Sort by year_month
    entries.sort(key=lambda x: x[3])
    for name, title, url, ym, gh, hf in entries:
        lines.append(format_entry(name, title, url, ym, gh, hf))
    lines.append("")

# Benchmarks
lines.append("### Benchmarks & Evaluations")
lines.append("")
benchmarks.sort(key=lambda x: x[3])
for name, title, url, ym, gh, hf in benchmarks:
    lines.append(format_entry(name, title, url, ym, gh, hf))
lines.append("")

# Surveys
lines.append("### Surveys & Reviews")
lines.append("")
surveys.sort(key=lambda x: x[3])
for name, title, url, ym, gh, hf in surveys:
    lines.append(format_entry(name, title, url, ym, gh, hf))
lines.append("")

output = "\n".join(lines)
print(output)

# Now inject into README before "## Contributing"
with open("survey_yuanli/README.md", "r", encoding="utf-8") as f:
    readme = f.read()

insert_point = readme.find("\n## Contributing")
if insert_point == -1:
    print("ERROR: Could not find ## Contributing")
else:
    new_readme = readme[:insert_point] + output + "\n" + readme[insert_point:]
    with open("survey_yuanli/README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("\n\nSUCCESS: Paper list injected into README.md")
