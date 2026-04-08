# Awesome RNA Foundation Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Last Update](https://img.shields.io/badge/Last_Update-2026.04-blue.svg)]()

A curated, comprehensive, and up-to-date collection of **RNA Sequence Foundation Models**, covering pre-trained language models for non-coding RNA, mRNA/CDS, UTR, structure-aware models, generative models, DNA+RNA multi-modal models, and related benchmarks.

> **Scope**: We focus on foundation models whose pre-training data includes **RNA sequences (A/U/C/G)**. Single-cell foundation models (e.g., scGPT, Geneformer) are **excluded**. DNA-only models that are commonly used as baselines in RNA benchmarks are listed separately for reference.

---

## Table of Contents

- [Awesome RNA Foundation Models ](#awesome-rna-foundation-models-)
  - [Table of Contents](#table-of-contents)
  - [RNA Sequence Foundation Models](#rna-sequence-foundation-models)
    - [ncRNA Foundation Models](#ncrna-foundation-models)
    - [mRNA / CDS Foundation Models](#mrna--cds-foundation-models)
    - [UTR Foundation Models](#utr-foundation-models)
    - [Specific RNA Type Models](#specific-rna-type-models)
    - [Structure-aware RNA Models](#structure-aware-rna-models)
    - [RNA Generative Models](#rna-generative-models)
    - [General RNA Models](#general-rna-models)
    - [Other RNA-related Models](#other-rna-related-models)
  - [DNA+RNA Foundation Models](#dnarna-foundation-models)
  - [Expression-based Foundation Models](#expression-based-foundation-models)
  - [Benchmarks \& Evaluations](#benchmarks--evaluations)
  - [Surveys \& Reviews](#surveys--reviews)
  - [Paper List](#paper-list)
    - [Foundation Models](#foundation-models)
    - [Benchmarks \& Evaluations](#benchmarks--evaluations-1)
    - [Surveys \& Reviews](#surveys--reviews-1)
  - [Contributing](#contributing)
  - [Abbreviations](#abbreviations)

---

## RNA Sequence Foundation Models

### ncRNA Foundation Models

Models primarily pre-trained on non-coding RNA sequences (from RNAcentral, Rfam, etc.).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **RNABert** | [Paper](https://doi.org/10.1093/nargab/lqac012) | [Code](https://github.com/mana438/RNABERT) | 2022.02 | Encoder-only | 0.5M | Rfam seed alignments + ncRNA | SNT |
| **RNAFM** | [Paper](https://arxiv.org/abs/2204.00300) | [Code](https://huggingface.co/multimolecule/rnafm) | 2022.08 | Encoder-only | 100M | RNAcentral (23M seqs) | SNT |
| **RNAMSM** | [Paper](https://doi.org/10.1093/nar/gkad1031) | [Code](https://github.com/yikunpku/RNA-MSM) | 2023.12 | Encoder-only | 95M | Rfam families + MSA homologs | SNT |
| **RNA-km** | [Paper](https://doi.org/10.1101/2024.01.27.577533) | [Code](https://github.com/gongtiansu/RNA-km) | 2024.01 | Encoder-only | 152M | RNAcentral (23M ncRNA seqs) | K-mer |
| **RNAErnie** | [Paper](https://www.nature.com/articles/s42256-024-00836-4) | [Code](https://huggingface.co/LLM-EDA/RNAErnie) | 2024.05 | Encoder-only | 105M | RNAcentral (23M seqs) | Nucleotide + motif |
| **ERNIE-RNA** | [Paper](https://doi.org/10.1101/2024.03.17.585376) | [Code](https://huggingface.co/multimolecule/ernierna-ss) | 2024.10 | Encoder-only | 86M | RNAcentral (20.4M seqs) | SNT |
| **DGRNA** | [Paper](https://doi.org/10.1101/2024.10.31.621427) | - | 2024.10 | Encoder-like | 100M | MARS (100M RNA seqs) | SNT |
| **ChaRNABERT** | [Paper](https://arxiv.org/abs/2411.11808) | - | 2024.11 | Encoder-only | 8M-650M | RNAcentral + NCBI (62M seqs) | Learnable (GBST) |
| **AIDO.RNA** | [Paper](https://doi.org/10.1101/2024.11.28.625345) | [Code](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B) | 2024.11 | Encoder-only | 650M / 1.6B | RNAcentral (42M seqs, ~30B nt) | SNT |
| **BiRNA-BERT** | [Paper](https://doi.org/10.1101/2024.07.02.601703) | [Code](https://github.com/buetnlpbio/BiRNA-BERT) | 2025.08 | Encoder-only | 117M | RNAcentral (36M seqs, ~26.4B nt) | Dual (NUC + BPE) |
| **RNA-BERTa** | [Paper](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) | [Code](https://huggingface.co/IlPakoZ/RNA-BERTa9700) | 2025.09 | Encoder-only | 55.9M | Public RNA collections (9.76M seqs) | SNT |
| **RiNALMo** | [Paper](https://arxiv.org/abs/2403.00043) | [Code](https://github.com/lbcb-sci/RiNALMo) | 2025.07 | Encoder-only | 135M-650M | RNAcentral (36M ncRNA seqs) | SNT |
| **RNAGenesis** | [Paper](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) | [Code](https://huggingface.co/Zaixi/RNAGenesis) | 2024.12 | Encoder + Diffusion | 1B | RNAcentral clustered ncRNA | Hybrid N-gram |
| **HydraRNA** | [Paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) | [Code](https://github.com/GuipengLi/HydraRNA) | 2025 | Encoder-only | 84M | 28.1M RNAs (ncRNA + coding) | SNT |
| **RNAElectra** | [Paper](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full) | - | 2026.03 | Encoder-only | - | RNAcentral ncRNAs | SNT |

### mRNA / CDS Foundation Models

Models pre-trained on messenger RNA coding sequences, codon-level representations.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **CodonBERT** | [Paper](https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1) | [Code](https://github.com/Sanofi-Public/CodonBERT) | 2023.09 | Encoder-only | 110M | NCBI (10M mRNA CDS) | Codon-aware |
| **CaLM** | [Paper](https://www.nature.com/articles/s42256-024-00791-0) | [Code](https://github.com/oxpig/CaLM) | 2024 | Encoder-only | 86M | ~9M non-redundant CDS | Codon-level (triplet) |
| **HELM** | [Paper](https://arxiv.org/abs/2410.12459) | - | 2025 | Encoder / Decoder | - | mRNA coding sequences | Codon-hierarchical |
| **Helix-mRNA** | [Paper](https://arxiv.org/abs/2502.13785) | [Code](https://huggingface.co/helical-ai/helix-mRNA) | 2025 | Hybrid (Mamba2+Attn) | Compact | mRNA sequences | SNT + codon markers |
| **GEMORNA** | [Paper](https://www.science.org/doi/10.1126/science.adr8470) | [Code](https://github.com/RainaBio/GEMORNA) | 2025 | Enc-Dec + Dec | - | mRNA CDS + UTR | Codon / nucleotide |
| **GenSLM** | [Paper](https://doi.org/10.1177/10943420231201154) | - | 2023 | Decoder-only | 2.5B-25B | 110M+ gene seqs + 1.5M SARS-CoV-2 genomes | Codon-level |
| **mRNABERT** | [Paper](https://www.nature.com/articles/s41467-025-65340-8) | [Code](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention) | 2025.11 | Encoder-only | 114M | 18M mRNA seqs (NCBI, MG-RAST, GWH, MGnify) | Dual tokenization |
| **mRNA-GPT** | [Paper](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) | [Code](https://github.com/ZHymLumine/mRNA-GPT/) | 2025.12 | Decoder-only | 302M | NCBI CDS (80M bact. + 83M euk. + 2M arch.) | Codon / nucleotide |
| **NUWA** | [Paper](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) | [Code](https://github.com/zysxmu/NUWA) | 2026.02 | Encoder-only | - | Multi-species mRNA CDS (115M seqs) | Codon tokens |
| **mRNA-GPT (full-length)** | [Paper](https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1) | - | 2026.03 | Decoder-only | - | 30M full-length mRNAs (5'UTR+CDS+3'UTR) | Nucleotide |
| **CodonMoE** | [Paper](https://openreview.net/forum?id=TOUrnb1EaG) | - | 2026 | MoE adapter | - | DNA FM + RNA adaptation | Codon-aware |

### UTR Foundation Models

Models focused on untranslated regions (5'UTR, 3'UTR).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **UTR-LM** | [Paper](https://www.nature.com/articles/s42256-024-00823-9) | [Code](https://huggingface.co/multimolecule/utrlm-te_el) | 2024.04 | Encoder-only | 1M | Ensembl 5'UTR (>214K seqs + synthetic) | SNT |
| **3UTRBert** | [Paper](https://doi.org/10.1101/2023.09.08.556883) | [Code](https://github.com/yangyn533/3UTRBERT) | 2024.07 | Encoder-only | 86M | GENCODE 3'UTR (20K seqs) | 3-mer |

### Specific RNA Type Models

Models targeting specific RNA types or species (splicing, lncRNA, G-quadruplex, plant RNA, RNA families).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **SpliceBERT** | [Paper](https://doi.org/10.1093/bib/bbae163) | [Code](https://github.com/chenkenbio/SpliceBERT) | 2023.01 | Encoder-only | 20M | UCSC pre-mRNA (72 species, >2M seqs) | SNT |
| **RFamLlama** | [Paper](https://openreview.net/forum?id=dXnQedxEJD) | [Code](https://huggingface.co/jinyuan22/RFamLlama-base) | 2024.08 | Decoder-only | 13-88M | Rfam (>4,000 families, 0.6M seqs) | Nucleotide + family |
| **PlantRNA-FM** | [Paper](https://www.nature.com/articles/s42256-024-00946-z) | [Code](https://huggingface.co/yangheng/PlantRNA-FM) | 2024.12 | Encoder-only | 35M | OneKP (1,124 plant species transcriptomes) | SNT |
| **LncRNA-BERT** | [Paper](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) | [Code](https://github.com/luukromeijn/lncRNA-Py) | 2025.01 | Encoder-only | - | GENCODE + RefSeq + NONCODE (536K seqs) | CSE / k-mer / nt |
| **G4mer** | [Paper](https://www.nature.com/articles/s41467-025-65020-7) | [Code](https://huggingface.co/Biociphers/g4mer) | 2025.12 | Encoder-only | 46M | Human transcriptome (G-quadruplex) | SNT |

### Structure-aware RNA Models

Models incorporating RNA secondary or tertiary structure information during pre-training.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **ATOM-1** | [Paper](https://doi.org/10.1101/2023.12.13.571579) | - | 2023.12 | Encoder-decoder | - | Chemical mapping sequencing data | SNT |
| **Ribonanza** | [Paper](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1) | [Code](https://github.com/Shujun-He/RibonanzaNet) | 2024.02 | Deep neural network | - | Eterna + Rfam + PDB (2M seqs) | - |
| **OmniGenome** | [Paper](https://arxiv.org/abs/2407.11242) | [Code](https://huggingface.co/yangheng/OmniGenome-186M) | 2024.07 | Encoder-only | 52M / 186M | OneKP (seq-structure pairs) | SNT |
| **MP-RNA** | [Paper](https://aclanthology.org/2024.findings-emnlp.304/) | [Code](https://huggingface.co/yangheng/MP-RNA) | 2024.11 | Encoder-style | 52-186M | OneKP (seq + structure) | SNT |
| **RNA-TorsionBERT** | [Paper](https://doi.org/10.1093/bioinformatics/btaf004) | [Code](https://huggingface.co/sayby/rna_torsionBERT) | 2025.01 | Encoder-only | 86.9M | PDB RNA 3D structures | SNT |
| **StructRFM** | [Paper](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) | [Code](https://github.com/heqin-zhu/structRFM) | 2025 | Encoder-only | - | 21M seq-structure pairs | SNT |

### RNA Generative Models

Models focused on RNA sequence generation (autoregressive, diffusion-based, etc.).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **LoRNA** | [Paper](https://doi.org/10.1101/2024.08.26.609813) | - | 2024.08 | Decoder-style | 6.5M | IsoSeq long-read (~100M reads, 7B tokens) | Specialized nt + region |
| **GenerRNA** | [Paper](https://doi.org/10.1371/journal.pone.0310814) | [Code](https://huggingface.co/pfnet/GenerRNA) | 2024.10 | Decoder-only | 350M | RNAcentral (16.09M seqs, ~17.4B nt) | BPE |
| **GARNET** | [Paper](https://www.nature.com/articles/s41467-024-54812-y) | [Code](https://github.com/Doudna-lab/GARNET_DL) | 2024.12 | Decoder + GNN | - | GTDB (30M seqs, 17B nt, 400K genomes) | Overlapping triplet |
| **RNAtranslator** | [Paper](https://doi.org/10.1371/journal.pcbi.1013541) | [Code](https://huggingface.co/SobhanShukueian/rnatranslator) | 2025.03 | Encoder-decoder | 41.4M | RNAInter (26M interaction pairs) | Nucleotide + AA |
| **EVA** | [Paper](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) | - | 2026.03 | Decoder-only (MoE) | - | 114M+ full-length RNA seqs | - |

### General RNA Models

General-purpose RNA models covering multiple RNA types.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **Uni-RNA** | [Paper](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) | [Code](https://github.com/ComDec/unirna_tf) | 2023.07 | Encoder-only | 400M | RNAcentral + MG-RAST + MGnify (1B seqs) | SNT |
| **RNALens** | [Paper](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) | [Code](https://github.com/oomics/RNALens) | 2025.07 | Encoder-only | 469M | Multispecies genomic + 5'UTR sequences | BPE |

### Other RNA-related Models

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **OPED** | [Paper](https://www.nature.com/articles/s42256-023-00739-w) | [Code](https://github.com/wenjiegroup/OPED) | 2023.10 | Encoder-decoder | - | pegRNA editing datasets (38K pairs) | SNT |

---

## DNA+RNA Foundation Models

Models pre-trained on **both DNA and RNA sequences**. These are not pure RNA FMs but their pre-training data includes RNA sequences and they can be applied to RNA downstream tasks.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **Evo** | [Paper](https://www.science.org/doi/10.1126/science.ado9336) | [Code](https://github.com/evo-design/evo) | 2024 | Decoder-only | 7B | OpenGenome (2.7M prokaryotic + phage genomes) | SNT |
| **LucaOne** | [Paper](https://www.nature.com/articles/s42256-025-01044-4) | [Code](https://github.com/LucaOne/LucaOne) | 2024 | Encoder-only | 1.8B | RefSeq + UniProt/PDB (800B tokens) | SNT / amino acid |
| **BSM** | [Paper](https://arxiv.org/abs/2410.11499) | - | 2024 | Decoder-only | 110M / 270M | RefSeq + web bio-seqs (DNA+RNA+Prot) | Mixed |
| **LAMAR** | [Paper](https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1) | [Code](https://github.com/zhw-e8/LAMAR) | 2024.10 | Encoder-only | 150M | Genome + transcriptome (225 mammals, 15M) | SNT |
| **Orthrus** | [Paper](https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3) | [Code](https://huggingface.co/quietflamingo/orthrus-large-4-track) | 2024.10 | Encoder-only | 1.3M / 10.1M | GENCODE + RefSeq + Zoonomia (32M transcripts) | SNT |
| **METAGENE-1** | [Paper](https://arxiv.org/abs/2501.02045) | [Code](https://huggingface.co/metagene-ai/METAGENE-1) | 2025.01 | Decoder-only | 7B | Wastewater metagenomic DNA/RNA (>1.5T bp) | BPE |
| **Life-Code** | [Paper](https://arxiv.org/abs/2502.07299) | - | 2025 | Hybrid encoder | - | Multi-omics (DNA/RNA/Prot unified) | Codon |
| **Evo 2** | [Paper](https://www.nature.com/articles/s41586-026-10176-5) | [Code](https://github.com/ArcInstitute/evo2) | 2025/2026 | Decoder-only | 7B / 40B | OpenGenome2 (9T nt, 128K genomes) | SNT |
| **OmniNA** | [Paper](https://academic.oup.com/nar/article/54/6/gkag083/8528802) | - | 2026 | Generative FM | - | 91.7M seqs + annotations (1076B bases) | - |
| **EDEN** | [Paper](https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1) | - | 2026.01 | Generative FM | 28B | 9.7T biological tokens (DNA+RNA+Protein) | - |

---

## Expression-based Foundation Models

Models operating on RNA-seq **gene expression profiles** (not raw nucleotide sequences). Listed for completeness.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| **BulkRNABert** | [Paper](https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2) | [Code](https://huggingface.co/InstaDeepAI/BulkRNABert) | 2024.06 | Encoder-only | 6.01M | TCGA + GTEx + ENCODE (RNA-seq expr.) | Expression bin tokens |
| **MOJO** | [Paper](https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1) | [Code](https://huggingface.co/InstaDeepAI/MOJO) | 2025.06 | Encoder (multimodal) | 52.3M | TCGA (RNA-seq + DNA methylation) | Expression bin tokens |

---

## Benchmarks & Evaluations

Benchmark datasets and systematic evaluations of RNA / nucleotide foundation models.

| Benchmark <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Focus <img width=300/> | Scale <img width=220/> |
|:----------|:-----:|:----:|:----:|:------|:------|
| **BEACON** | [Paper](https://arxiv.org/abs/2406.10391) | [Code](https://github.com/terry-r123/RNABenchmark) | 2024 | RNA (structural, functional, engineering) | 13 tasks |
| **BEND** | [Paper](https://arxiv.org/abs/2311.12570) | [Code](https://github.com/frederikkemarin/BEND) | 2024 | DNA LM biologically meaningful tasks | Multiple tasks |
| **RNA LLM Folding** | [Paper](https://arxiv.org/abs/2410.16212) | [Code](https://github.com/sinc-lab/rna-llm-folding) | 2024/2025 | RNA secondary structure prediction | 6 RNA LLMs, 4 datasets |
| **GUE** | [Paper](https://arxiv.org/abs/2306.15006) | - | 2023 | Genome understanding evaluation | 36 datasets, 9 tasks |
| **RNAGym** | [Paper](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1) | - | 2025 | RNA fitness & structure prediction (2D/3D) | Fitness + structure tasks |
| **RNAscope** | [Paper](https://openreview.net/forum?id=zYAuJxcl2E) | - | 2025 | RNA (structure, interaction, function) | 15 tasks, 1,253 experiments |
| **mRNABench** | [Paper](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) | [Code](https://github.com/morrislab/mRNABench) | 2025 | Mature mRNA prediction tasks | 10 datasets, 59 tasks, 135K experiments |
| **NABench** | [Paper](https://arxiv.org/html/2511.02888v1) | - | 2025 | Nucleic acid fitness prediction | 2.6M+ mutated seqs, 160+ experiments |
| **RNA 3D Benchmark** | [Paper](https://arxiv.org/abs/2503.21681) | - | 2025 | RNA 3D structure-function | 7 tasks, 9 datasets |
| **Genomic LM RNA Eval** | [Paper](https://www.nature.com/articles/s41467-025-66899-y) | - | 2025 | RNA processes (ncRNA, m6A, splicing, TE) | 11 genomic LMs, 4 RNA tasks |
| **DNA FM Benchmark** | [Paper](https://www.nature.com/articles/s41467-025-65823-8) | - | 2025 | Genomic & genetic tasks (incl. RNA-relevant) | Multiple tasks |
| **DNALongBench** | [Paper](https://www.nature.com/articles/s41467-025-65077-4) | - | 2025 | Long-range genomic tasks | 5 tasks, up to 1M bp |

---

## Surveys & Reviews

| Title <img width=350/> | Paper <img width=120/> | Year <img width=70/> | Scope <img width=400/> |
|:------|:-----:|:----:|:------|
| **A Comparative Review of RNA Language Models** | [Paper](https://arxiv.org/abs/2505.09087) | 2025 | Compares 13 RNA LMs + 3 DNA LMs + 1 protein LM |
| **Comprehensive Survey of Genome Language Models** | [Paper](https://academic.oup.com/bib/article/27/1/bbaf724/8426124) | 2026.01 | DNA/RNA genome LMs: limitations, long-range modeling |
| **LLMs in Bioinformatics: A Survey** | [Paper](https://arxiv.org/abs/2503.04490) | 2026.03 | LLMs for DNA, RNA, proteins (ACL 2025 Findings, updated 2026) |

---

## Paper List

A complete chronological list of all papers included in this survey.

### Foundation Models

**ncRNA Foundation Models**

- [Informative RNA-base embedding for RNA structural alignment and clustering by a representation learning framework](https://doi.org/10.1093/nargab/lqac012) [![abs](https://img.shields.io/badge/abs-2022.02-b31b1b.svg)](https://doi.org/10.1093/nargab/lqac012) [Code](https://github.com/mana438/RNABERT)
- [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) [![abs](https://img.shields.io/badge/abs-2022.08-b31b1b.svg)](https://arxiv.org/abs/2204.00300) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/rnafm)
- [Multiple sequence-alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1093/nar/gkad1031) [Code](https://github.com/yikunpku/RNA-MSM)
- [RNA-km: a tool for predicting RNA sequence properties using k-mer frequency features](https://doi.org/10.1101/2024.01.27.577533) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1101/2024.01.27.577533) [Code](https://github.com/gongtiansu/RNA-km)
- [RNAErnie: An RNA language model with structure-enhanced representations](https://www.nature.com/articles/s42256-024-00836-4) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00836-4) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LLM-EDA/RNAErnie)
- [ERNIE-RNA: An RNA Language Model with Structure-enhanced Representations](https://doi.org/10.1101/2024.03.17.585376) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.03.17.585376) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/ernierna-ss)
- [DGRNA: a long-context RNA foundation model with bidirectional Mamba2](https://doi.org/10.1101/2024.10.31.621427) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.10.31.621427)
- [ChaRNABERT: A pre-trained RNA language model with learnable tokenization](https://arxiv.org/abs/2411.11808) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://arxiv.org/abs/2411.11808)
- [AIDO.RNA: A Scalable RNA Foundation Model](https://doi.org/10.1101/2024.11.28.625345) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://doi.org/10.1101/2024.11.28.625345) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)
- [RNAGenesis: A Generative RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Zaixi/RNAGenesis)
- [HydraRNA: An Efficient RNA Foundation Model via Hybrid SSM and Attention](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [Code](https://github.com/GuipengLi/HydraRNA)
- [RiNALMo: General-Purpose RNA Language Models Can Generalize Well on Structure Prediction Tasks](https://arxiv.org/abs/2403.00043) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://arxiv.org/abs/2403.00043) [Code](https://github.com/lbcb-sci/RiNALMo)
- [BiRNA-BERT: An Efficient RNA Language Model with Adaptive Dual Tokenization](https://doi.org/10.1101/2024.07.02.601703) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://doi.org/10.1101/2024.07.02.601703) [Code](https://github.com/buetnlpbio/BiRNA-BERT)
- [DLRNA-BERTa: A Transformer for RNA-Drug Binding Affinity Prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/IlPakoZ/RNA-BERTa9700)
- [RNAElectra: An ELECTRA-style RNA Foundation Model](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full)

**mRNA / CDS Foundation Models**

- [GenSLMs: Genome-scale Language Models Reveal SARS-CoV-2 Evolutionary Dynamics](https://doi.org/10.1177/10943420231201154) [![abs](https://img.shields.io/badge/abs-2023.01-b31b1b.svg)](https://doi.org/10.1177/10943420231201154)
- [CodonBERT: Large Language Models for mRNA Unimodal and Multimodal Molecular Learning](https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1) [![abs](https://img.shields.io/badge/abs-2023.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1) [Code](https://github.com/Sanofi-Public/CodonBERT)
- [CaLM: Codon Adaptation Language Model for mRNA Design](https://www.nature.com/articles/s42256-024-00791-0) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00791-0) [Code](https://github.com/oxpig/CaLM)
- [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2410.12459)
- [Helix-mRNA: A Hybrid SSM-Attention Model for mRNA](https://arxiv.org/abs/2502.13785) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.13785) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/helical-ai/helix-mRNA)
- [GEMORNA: Generative mRNA Design via Codon and UTR Optimization](https://www.science.org/doi/10.1126/science.adr8470) [![abs](https://img.shields.io/badge/abs-2025.05-b31b1b.svg)](https://www.science.org/doi/10.1126/science.adr8470) [Code](https://github.com/RainaBio/GEMORNA)
- [mRNABERT: A Pre-trained Language Model for mRNA Sequences](https://www.nature.com/articles/s41467-025-65340-8) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65340-8) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)
- [mRNA-GPT: An Autoregressive mRNA Foundation Model across Three Domains of Life](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [Code](https://github.com/ZHymLumine/mRNA-GPT/)
- [CodonMoE: Adapting DNA Language Models for RNA via Mixture-of-Experts](https://openreview.net/forum?id=TOUrnb1EaG) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://openreview.net/forum?id=TOUrnb1EaG)
- [NUWA: A Codon Language Model for mRNA Coding Sequences](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [Code](https://github.com/zysxmu/NUWA)
- [mRNA-GPT: Full-Length mRNA Design via Autoregressive Generation with PPO](https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1)

**UTR Foundation Models**

- [UTR-LM: A 5' UTR Language Model for Predicting Translation Efficiency](https://www.nature.com/articles/s42256-024-00823-9) [![abs](https://img.shields.io/badge/abs-2024.04-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00823-9) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/utrlm-te_el)
- [3UTRBERT: Pre-trained Language Model for 3' UTR Sequences](https://doi.org/10.1101/2023.09.08.556883) [![abs](https://img.shields.io/badge/abs-2024.07-b31b1b.svg)](https://doi.org/10.1101/2023.09.08.556883) [Code](https://github.com/yangyn533/3UTRBERT)

**Specific RNA Type Models**

- [SpliceBERT: A Pre-trained Model for Self-supervised Learning of Pre-mRNA Splicing](https://doi.org/10.1093/bib/bbae163) [![abs](https://img.shields.io/badge/abs-2023.01-b31b1b.svg)](https://doi.org/10.1093/bib/bbae163) [Code](https://github.com/chenkenbio/SpliceBERT)
- [RFamLlama: Conditional RNA Generation by RNA Family](https://openreview.net/forum?id=dXnQedxEJD) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://openreview.net/forum?id=dXnQedxEJD) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/jinyuan22/RFamLlama-base)
- [PlantRNA-FM: A Plant RNA Foundation Model from Multi-species Transcriptomes](https://www.nature.com/articles/s42256-024-00946-z) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00946-z) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/PlantRNA-FM)
- [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [Code](https://github.com/luukromeijn/lncRNA-Py)
- [G4mer: An Interpretable Transformer for G-quadruplex Prediction in the Transcriptome](https://www.nature.com/articles/s41467-025-65020-7) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65020-7) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Biociphers/g4mer)

**Structure-aware RNA Models**

- [ATOM-1: Augmented Transformer with Structure-aware Chemical Mapping](https://doi.org/10.1101/2023.12.13.571579) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1101/2023.12.13.571579)
- [RibonanzaNet: Deep Learning for RNA Chemical Mapping Prediction](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1) [Code](https://github.com/Shujun-He/RibonanzaNet)
- [OmniGenome: Aligning RNA Sequences with Secondary Structures](https://arxiv.org/abs/2407.11242) [![abs](https://img.shields.io/badge/abs-2024.07-b31b1b.svg)](https://arxiv.org/abs/2407.11242) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/OmniGenome-186M)
- [MP-RNA: Multi-Purpose RNA Foundation Model with Structure Awareness](https://aclanthology.org/2024.findings-emnlp.304/) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://aclanthology.org/2024.findings-emnlp.304/) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/MP-RNA)
- [RNA-TorsionBERT: Predicting RNA Backbone Torsion Angles](https://doi.org/10.1093/bioinformatics/btaf004) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://doi.org/10.1093/bioinformatics/btaf004) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/sayby/rna_torsionBERT)
- [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [Code](https://github.com/heqin-zhu/structRFM)

**RNA Generative Models**

- [LoRNA: A Long-read RNA Foundation Model](https://doi.org/10.1101/2024.08.26.609813) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/2024.08.26.609813)
- [GenerRNA: A Generative Pre-trained Autoregressive RNA Language Model](https://doi.org/10.1371/journal.pone.0310814) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1371/journal.pone.0310814) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/pfnet/GenerRNA)
- [GARNET: A Generative RNA Design Model from Microbial Genomes](https://www.nature.com/articles/s41467-024-54812-y) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s41467-024-54812-y) [Code](https://github.com/Doudna-lab/GARNET_DL)
- [RNAtranslator: Protein-conditioned RNA Sequence Generation](https://doi.org/10.1371/journal.pcbi.1013541) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://doi.org/10.1371/journal.pcbi.1013541) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/SobhanShukueian/rnatranslator)
- [EVA: Evolutionary Versatile Architect for Long-context RNA Generation](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)

**General / Other RNA Models**

- [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![abs](https://img.shields.io/badge/abs-2023.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [Code](https://github.com/ComDec/unirna_tf)
- [OPED: Transformer-based pegRNA Editing Efficiency Prediction](https://www.nature.com/articles/s42256-023-00739-w) [![abs](https://img.shields.io/badge/abs-2023.10-b31b1b.svg)](https://www.nature.com/articles/s42256-023-00739-w) [Code](https://github.com/wenjiegroup/OPED)
- [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [Code](https://github.com/oomics/RNALens)

**DNA+RNA Foundation Models**

- [Sequence Modeling and Design from Molecular to Genome Scale with Evo](https://www.science.org/doi/10.1126/science.ado9336) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.science.org/doi/10.1126/science.ado9336) [Code](https://github.com/evo-design/evo)
- [LucaOne: A Unified Foundation Model for DNA, RNA and Protein](https://www.nature.com/articles/s42256-025-01044-4) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-025-01044-4) [Code](https://github.com/LucaOne/LucaOne)
- [BSM: Biological Sequence Model for Mixed-modal Pretraining](https://arxiv.org/abs/2410.11499) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.11499)
- [LAMAR: A Language Model for Mammalian and Viral Genomes and Transcriptomes](https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1) [Code](https://github.com/zhw-e8/LAMAR)
- [Orthrus: Contrastive Learning of Transcript Isoforms and Orthologs via Mamba](https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/quietflamingo/orthrus-large-4-track)
- [METAGENE-1: A 7B Metagenomic Foundation Model for DNA and RNA](https://arxiv.org/abs/2501.02045) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2501.02045) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/metagene-ai/METAGENE-1)
- [Life-Code: A Unified Foundation Model via Central Dogma](https://arxiv.org/abs/2502.07299) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.07299)
- [OmniNA: A Foundation Model for Nucleotide Sequences and Annotations](https://academic.oup.com/nar/article/54/6/gkag083/8528802) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://academic.oup.com/nar/article/54/6/gkag083/8528802)
- [EDEN: A 28B Foundation Model for Programmable Gene Insertion](https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1)
- [Genome Modeling and Design Across All Domains of Life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.nature.com/articles/s41586-026-10176-5) [Code](https://github.com/ArcInstitute/evo2)

**Expression-based Foundation Models**

- [BulkRNABert: A Pre-trained Model for Bulk RNA-seq Expression Data](https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/InstaDeepAI/BulkRNABert)
- [MOJO: A Multi-omics Foundation Model for RNA-seq and Methylation](https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/InstaDeepAI/MOJO)

### Benchmarks & Evaluations

- [DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genome](https://arxiv.org/abs/2306.15006) [![abs](https://img.shields.io/badge/abs-2023.06-b31b1b.svg)](https://arxiv.org/abs/2306.15006)
- [BEND: Benchmarking DNA Language Models on Biologically Meaningful Tasks](https://arxiv.org/abs/2311.12570) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://arxiv.org/abs/2311.12570) [Code](https://github.com/frederikkemarin/BEND)
- [BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://arxiv.org/abs/2406.10391) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://arxiv.org/abs/2406.10391) [Code](https://github.com/terry-r123/RNABenchmark)
- [Comprehensive Benchmarking of LLMs for RNA Secondary Structure Prediction](https://arxiv.org/abs/2410.16212) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.16212) [Code](https://github.com/sinc-lab/rna-llm-folding)
- [Comprehensive Benchmark for RNA 3D Structure-Function Modeling](https://arxiv.org/abs/2503.21681) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://arxiv.org/abs/2503.21681)
- [RNAGym: A Benchmark for RNA Fitness and Structure Prediction](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1)
- [DNALongBench: Benchmarking Long-range Genomic Tasks](https://www.nature.com/articles/s41467-025-65077-4) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65077-4)
- [mRNABench: Benchmarking Nucleotide FMs on Mature mRNA Tasks](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) [Code](https://github.com/morrislab/mRNABench)
- [Benchmarking DNA Foundation Models for Genomic and Genetic Tasks](https://www.nature.com/articles/s41467-025-65823-8) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65823-8)
- [Benchmarking Pre-trained Genomic Language Models for RNA Predictive Tasks](https://www.nature.com/articles/s41467-025-66899-y) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.nature.com/articles/s41467-025-66899-y)
- [RNAscope: Comprehensive Benchmark for RNA Foundation Models](https://openreview.net/forum?id=zYAuJxcl2E) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://openreview.net/forum?id=zYAuJxcl2E)
- [NABench: Nucleic Acid Fitness Prediction Benchmark](https://arxiv.org/html/2511.02888v1) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://arxiv.org/html/2511.02888v1)

### Surveys & Reviews

- [A Comparative Review of RNA Language Models](https://arxiv.org/abs/2505.09087) [![abs](https://img.shields.io/badge/abs-2025.05-b31b1b.svg)](https://arxiv.org/abs/2505.09087)
- [A Comprehensive Survey of Genome Language Models in Bioinformatics](https://academic.oup.com/bib/article/27/1/bbaf724/8426124) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://academic.oup.com/bib/article/27/1/bbaf724/8426124)
- [Large Language Models in Bioinformatics: A Survey](https://arxiv.org/abs/2503.04490) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://arxiv.org/abs/2503.04490)


## Contributing

Contributions are welcome! If you find a missing RNA foundation model, benchmark, or survey paper, please:

1. Open an issue with the model/paper details
2. Or submit a pull request following the existing table format

**What to include**: RNA sequence foundation models (pre-trained on A/U/C/G sequences), DNA+RNA models, and relevant benchmarks.

**What NOT to include**: Single-cell foundation models (scGPT, Geneformer, etc.), protein-only models, or purely DNA models (unless they are widely evaluated on RNA tasks).

---

## Abbreviations

| Abbreviation <img width=120/> | Meaning <img width=400/> |
|:-------------|:--------|
| **SNT** | Single Nucleotide Tokenization (A/U/C/G or A/T/C/G) |
| **MLM** | Masked Language Modeling |
| **BPE** | Byte Pair Encoding |
| **MoE** | Mixture of Experts |
| **SSM** | State Space Model |
| **CDS** | Coding Sequence |
| **UTR** | Untranslated Region |
| **ncRNA** | Non-coding RNA |

---

*Last updated: April 2026*
