# Awesome RNA Foundation Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Last Update](https://img.shields.io/badge/Last_Update-2026.04-blue.svg)]()

A curated, comprehensive, and up-to-date collection of **RNA Sequence Foundation Models**, covering pre-trained language models for non-coding RNA, mRNA/CDS, UTR, structure-aware models, generative models, DNA+RNA multi-modal models, and related benchmarks.

> **Scope**: We focus on foundation models whose pre-training data includes **RNA sequences (A/U/C/G)**. Single-cell foundation models (e.g., scGPT, Geneformer) are **excluded**. DNA-only models that are commonly used as baselines in RNA benchmarks are listed separately for reference.

---

## Table of Contents

- [Model Tables](#model-tables)
  - [RNA Sequence Foundation Models](#rna-sequence-foundation-models)
    - [ncRNA Foundation Models](#ncrna-foundation-models)
    - [mRNA / CDS Foundation Models](#mrna--cds-foundation-models)
    - [UTR Foundation Models](#utr-foundation-models)
    - [Specific RNA Type Models](#specific-rna-type-models)
    - [Structure-aware RNA Models](#structure-aware-rna-models)
    - [RNA Generative Models](#rna-generative-models)
    - [General RNA Models](#general-rna-models)
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

## Model Tables

### RNA Sequence Foundation Models

#### ncRNA Foundation Models

Models primarily pre-trained on non-coding RNA sequences (from RNAcentral, Rfam, etc.).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**RNABert**</nobr> | <nobr>[Paper](https://doi.org/10.1093/nargab/lqac012)</nobr> | <nobr>[Code](https://github.com/mana438/RNABERT)</nobr> | <nobr>2022.02</nobr> | <nobr>Encoder-only</nobr> | <nobr>0.5M</nobr> | <nobr>Rfam seed alignments + ncRNA</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAFM**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2204.00300)</nobr> | <nobr>[Code](https://huggingface.co/multimolecule/rnafm)</nobr> | <nobr>2022.08</nobr> | <nobr>Encoder-only</nobr> | <nobr>100M</nobr> | <nobr>RNAcentral (23M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAMSM**</nobr> | <nobr>[Paper](https://doi.org/10.1093/nar/gkad1031)</nobr> | <nobr>[Code](https://github.com/yikunpku/RNA-MSM)</nobr> | <nobr>2023.12</nobr> | <nobr>Encoder-only</nobr> | <nobr>95M</nobr> | <nobr>Rfam families + MSA homologs</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNA-km**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.01.27.577533)</nobr> | <nobr>[Code](https://github.com/gongtiansu/RNA-km)</nobr> | <nobr>2024.01</nobr> | <nobr>Encoder-only</nobr> | <nobr>152M</nobr> | <nobr>RNAcentral (23M ncRNA seqs)</nobr> | <nobr>K-mer</nobr> |
| <nobr>**RNAErnie**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00836-4)</nobr> | <nobr>[Code](https://huggingface.co/LLM-EDA/RNAErnie)</nobr> | <nobr>2024.05</nobr> | <nobr>Encoder-only</nobr> | <nobr>105M</nobr> | <nobr>RNAcentral (23M seqs)</nobr> | <nobr>Nucleotide + motif</nobr> |
| <nobr>**ERNIE-RNA**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.03.17.585376)</nobr> | <nobr>[Code](https://huggingface.co/multimolecule/ernierna-ss)</nobr> | <nobr>2024.10</nobr> | <nobr>Encoder-only</nobr> | <nobr>86M</nobr> | <nobr>RNAcentral (20.4M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**DGRNA**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.10.31.621427)</nobr> | - | <nobr>2024.10</nobr> | <nobr>Encoder-like</nobr> | <nobr>100M</nobr> | <nobr>MARS (100M RNA seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**ChaRNABERT**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2411.11808)</nobr> | - | <nobr>2024.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>8M-650M</nobr> | <nobr>RNAcentral + NCBI (62M seqs)</nobr> | <nobr>Learnable (GBST)</nobr> |
| <nobr>**AIDO.RNA**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.11.28.625345)</nobr> | <nobr>[Code](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)</nobr> | <nobr>2024.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>650M / 1.6B</nobr> | <nobr>RNAcentral (42M seqs, ~30B nt)</nobr> | <nobr>SNT</nobr> |
| <nobr>**BiRNA-BERT**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.07.02.601703)</nobr> | <nobr>[Code](https://github.com/buetnlpbio/BiRNA-BERT)</nobr> | <nobr>2025.08</nobr> | <nobr>Encoder-only</nobr> | <nobr>117M</nobr> | <nobr>RNAcentral (36M seqs, ~26.4B nt)</nobr> | <nobr>Dual (NUC + BPE)</nobr> |
| <nobr>**RNA-BERTa**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1)</nobr> | <nobr>[Code](https://huggingface.co/IlPakoZ/RNA-BERTa9700)</nobr> | <nobr>2025.09</nobr> | <nobr>Encoder-only</nobr> | <nobr>55.9M</nobr> | <nobr>Public RNA collections (9.76M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RiNALMo**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2403.00043)</nobr> | <nobr>[Code](https://github.com/lbcb-sci/RiNALMo)</nobr> | <nobr>2025.07</nobr> | <nobr>Encoder-only</nobr> | <nobr>135M-650M</nobr> | <nobr>RNAcentral (36M ncRNA seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAGenesis**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2)</nobr> | <nobr>[Code](https://huggingface.co/Zaixi/RNAGenesis)</nobr> | <nobr>2024.12</nobr> | <nobr>Encoder + Diffusion</nobr> | <nobr>1B</nobr> | <nobr>RNAcentral clustered ncRNA</nobr> | <nobr>Hybrid N-gram</nobr> |
| <nobr>**HydraRNA**</nobr> | <nobr>[Paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7)</nobr> | <nobr>[Code](https://github.com/GuipengLi/HydraRNA)</nobr> | <nobr>2025.03</nobr> | <nobr>Encoder-only</nobr> | <nobr>84M</nobr> | <nobr>28.1M RNAs (ncRNA + coding)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAElectra**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full)</nobr> | - | <nobr>2026.03</nobr> | <nobr>Encoder-only</nobr> | - | <nobr>RNAcentral ncRNAs</nobr> | <nobr>SNT</nobr> |

#### mRNA / CDS Foundation Models

Models pre-trained on messenger RNA coding sequences, codon-level representations.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**CodonBERT**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1)</nobr> | <nobr>[Code](https://github.com/Sanofi-Public/CodonBERT)</nobr> | <nobr>2023.09</nobr> | <nobr>Encoder-only</nobr> | <nobr>110M</nobr> | <nobr>NCBI (10M mRNA CDS)</nobr> | <nobr>Codon-aware</nobr> |
| <nobr>**CaLM**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00791-0)</nobr> | <nobr>[Code](https://github.com/oxpig/CaLM)</nobr> | <nobr>2024.02</nobr> | <nobr>Encoder-only</nobr> | <nobr>86M</nobr> | <nobr>~9M non-redundant CDS</nobr> | <nobr>Codon-level (triplet)</nobr> |
| <nobr>**HELM**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2410.12459)</nobr> | - | <nobr>2025.01</nobr> | <nobr>Encoder / Decoder</nobr> | - | <nobr>mRNA coding sequences</nobr> | <nobr>Codon-hierarchical</nobr> |
| <nobr>**Helix-mRNA**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2502.13785)</nobr> | <nobr>[Code](https://huggingface.co/helical-ai/helix-mRNA)</nobr> | <nobr>2025.02</nobr> | <nobr>Hybrid (Mamba2+Attn)</nobr> | <nobr>Compact</nobr> | <nobr>mRNA sequences</nobr> | <nobr>SNT + codon markers</nobr> |
| <nobr>**GEMORNA**</nobr> | <nobr>[Paper](https://www.science.org/doi/10.1126/science.adr8470)</nobr> | <nobr>[Code](https://github.com/RainaBio/GEMORNA)</nobr> | <nobr>2025.05</nobr> | <nobr>Enc-Dec + Dec</nobr> | - | <nobr>mRNA CDS + UTR</nobr> | <nobr>Codon / nucleotide</nobr> |
| <nobr>**GenSLM**</nobr> | <nobr>[Paper](https://doi.org/10.1177/10943420231201154)</nobr> | - | <nobr>2023.01</nobr> | <nobr>Decoder-only</nobr> | <nobr>2.5B-25B</nobr> | <nobr>110M+ gene seqs + 1.5M SARS-CoV-2 genomes</nobr> | <nobr>Codon-level</nobr> |
| <nobr>**mRNABERT**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65340-8)</nobr> | <nobr>[Code](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)</nobr> | <nobr>2025.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>114M</nobr> | <nobr>18M mRNA seqs (NCBI, MG-RAST, GWH, MGnify)</nobr> | <nobr>Dual tokenization</nobr> |
| <nobr>**mRNA-GPT**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1)</nobr> | <nobr>[Code](https://github.com/ZHymLumine/mRNA-GPT/)</nobr> | <nobr>2025.12</nobr> | <nobr>Decoder-only</nobr> | <nobr>302M</nobr> | <nobr>NCBI CDS (80M bact. + 83M euk. + 2M arch.)</nobr> | <nobr>Codon / nucleotide</nobr> |
| <nobr>**NUWA**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3)</nobr> | <nobr>[Code](https://github.com/zysxmu/NUWA)</nobr> | <nobr>2026.02</nobr> | <nobr>Encoder-only</nobr> | - | <nobr>Multi-species mRNA CDS (115M seqs)</nobr> | <nobr>Codon tokens</nobr> |
| <nobr>**mRNA-GPT (full-length)**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1)</nobr> | - | <nobr>2026.03</nobr> | <nobr>Decoder-only</nobr> | - | <nobr>30M full-length mRNAs (5'UTR+CDS+3'UTR)</nobr> | <nobr>Nucleotide</nobr> |
| <nobr>**CodonMoE**</nobr> | <nobr>[Paper](https://openreview.net/forum?id=TOUrnb1EaG)</nobr> | - | <nobr>2026.01</nobr> | <nobr>MoE adapter</nobr> | - | <nobr>DNA FM + RNA adaptation</nobr> | <nobr>Codon-aware</nobr> |

#### UTR Foundation Models

Models focused on untranslated regions (5'UTR, 3'UTR).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**UTR-LM**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00823-9)</nobr> | <nobr>[Code](https://huggingface.co/multimolecule/utrlm-te_el)</nobr> | <nobr>2024.04</nobr> | <nobr>Encoder-only</nobr> | <nobr>1M</nobr> | <nobr>Ensembl 5'UTR (>214K seqs + synthetic)</nobr> | <nobr>SNT</nobr> |
| <nobr>**3UTRBert**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2023.09.08.556883)</nobr> | <nobr>[Code](https://github.com/yangyn533/3UTRBERT)</nobr> | <nobr>2024.07</nobr> | <nobr>Encoder-only</nobr> | <nobr>86M</nobr> | <nobr>GENCODE 3'UTR (20K seqs)</nobr> | <nobr>3-mer</nobr> |

#### Specific RNA Type Models

Models targeting specific RNA types or species (splicing, lncRNA, G-quadruplex, plant RNA, RNA families).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**SpliceBERT**</nobr> | <nobr>[Paper](https://doi.org/10.1093/bib/bbae163)</nobr> | <nobr>[Code](https://github.com/chenkenbio/SpliceBERT)</nobr> | <nobr>2023.01</nobr> | <nobr>Encoder-only</nobr> | <nobr>20M</nobr> | <nobr>UCSC pre-mRNA (72 species, >2M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RFamLlama**</nobr> | <nobr>[Paper](https://openreview.net/forum?id=dXnQedxEJD)</nobr> | <nobr>[Code](https://huggingface.co/jinyuan22/RFamLlama-base)</nobr> | <nobr>2024.08</nobr> | <nobr>Decoder-only</nobr> | <nobr>13-88M</nobr> | <nobr>Rfam (>4,000 families, 0.6M seqs)</nobr> | <nobr>Nucleotide + family</nobr> |
| <nobr>**PlantRNA-FM**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00946-z)</nobr> | <nobr>[Code](https://huggingface.co/yangheng/PlantRNA-FM)</nobr> | <nobr>2024.12</nobr> | <nobr>Encoder-only</nobr> | <nobr>35M</nobr> | <nobr>OneKP (1,124 plant species transcriptomes)</nobr> | <nobr>SNT</nobr> |
| <nobr>**LncRNA-BERT**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1)</nobr> | <nobr>[Code](https://github.com/luukromeijn/lncRNA-Py)</nobr> | <nobr>2025.01</nobr> | <nobr>Encoder-only</nobr> | - | <nobr>GENCODE + RefSeq + NONCODE (536K seqs)</nobr> | <nobr>CSE / k-mer / nt</nobr> |
| <nobr>**G4mer**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65020-7)</nobr> | <nobr>[Code](https://huggingface.co/Biociphers/g4mer)</nobr> | <nobr>2025.12</nobr> | <nobr>Encoder-only</nobr> | <nobr>46M</nobr> | <nobr>Human transcriptome (G-quadruplex)</nobr> | <nobr>SNT</nobr> |

#### Structure-aware RNA Models

Models incorporating RNA secondary or tertiary structure information during pre-training.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**ATOM-1**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2023.12.13.571579)</nobr> | - | <nobr>2023.12</nobr> | <nobr>Encoder-decoder</nobr> | - | <nobr>Chemical mapping sequencing data</nobr> | <nobr>SNT</nobr> |
| <nobr>**Ribonanza**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1)</nobr> | <nobr>[Code](https://github.com/Shujun-He/RibonanzaNet)</nobr> | <nobr>2024.02</nobr> | <nobr>Deep neural network</nobr> | - | <nobr>Eterna + Rfam + PDB (2M seqs)</nobr> | - |
| <nobr>**OmniGenome**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2407.11242)</nobr> | <nobr>[Code](https://huggingface.co/yangheng/OmniGenome-186M)</nobr> | <nobr>2024.07</nobr> | <nobr>Encoder-only</nobr> | <nobr>52M / 186M</nobr> | <nobr>OneKP (seq-structure pairs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**MP-RNA**</nobr> | <nobr>[Paper](https://aclanthology.org/2024.findings-emnlp.304/)</nobr> | <nobr>[Code](https://huggingface.co/yangheng/MP-RNA)</nobr> | <nobr>2024.11</nobr> | <nobr>Encoder-style</nobr> | <nobr>52-186M</nobr> | <nobr>OneKP (seq + structure)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNA-TorsionBERT**</nobr> | <nobr>[Paper](https://doi.org/10.1093/bioinformatics/btaf004)</nobr> | <nobr>[Code](https://huggingface.co/sayby/rna_torsionBERT)</nobr> | <nobr>2025.01</nobr> | <nobr>Encoder-only</nobr> | <nobr>86.9M</nobr> | <nobr>PDB RNA 3D structures</nobr> | <nobr>SNT</nobr> |
| <nobr>**StructRFM**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1)</nobr> | <nobr>[Code](https://github.com/heqin-zhu/structRFM)</nobr> | <nobr>2025.08</nobr> | <nobr>Encoder-only</nobr> | - | <nobr>21M seq-structure pairs</nobr> | <nobr>SNT</nobr> |

#### RNA Generative Models

Models focused on RNA sequence generation (autoregressive, diffusion-based, etc.).

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**LoRNA**</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.08.26.609813)</nobr> | - | <nobr>2024.08</nobr> | <nobr>Decoder-style</nobr> | <nobr>6.5M</nobr> | <nobr>IsoSeq long-read (~100M reads, 7B tokens)</nobr> | <nobr>Specialized nt + region</nobr> |
| <nobr>**GenerRNA**</nobr> | <nobr>[Paper](https://doi.org/10.1371/journal.pone.0310814)</nobr> | <nobr>[Code](https://huggingface.co/pfnet/GenerRNA)</nobr> | <nobr>2024.10</nobr> | <nobr>Decoder-only</nobr> | <nobr>350M</nobr> | <nobr>RNAcentral (16.09M seqs, ~17.4B nt)</nobr> | <nobr>BPE</nobr> |
| <nobr>**GARNET**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-024-54812-y)</nobr> | <nobr>[Code](https://github.com/Doudna-lab/GARNET_DL)</nobr> | <nobr>2024.12</nobr> | <nobr>Decoder + GNN</nobr> | - | <nobr>GTDB (30M seqs, 17B nt, 400K genomes)</nobr> | <nobr>Overlapping triplet</nobr> |
| <nobr>**RNAtranslator**</nobr> | <nobr>[Paper](https://doi.org/10.1371/journal.pcbi.1013541)</nobr> | <nobr>[Code](https://huggingface.co/SobhanShukueian/rnatranslator)</nobr> | <nobr>2025.03</nobr> | <nobr>Encoder-decoder</nobr> | <nobr>41.4M</nobr> | <nobr>RNAInter (26M interaction pairs)</nobr> | <nobr>Nucleotide + AA</nobr> |
| <nobr>**EVA**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)</nobr> | - | <nobr>2026.03</nobr> | <nobr>Decoder-only (MoE)</nobr> | - | <nobr>114M+ full-length RNA seqs</nobr> | - |

#### General RNA Models

General-purpose RNA models covering multiple RNA types.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**Uni-RNA**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1)</nobr> | <nobr>[Code](https://github.com/ComDec/unirna_tf)</nobr> | <nobr>2023.07</nobr> | <nobr>Encoder-only</nobr> | <nobr>400M</nobr> | <nobr>RNAcentral + MG-RAST + MGnify (1B seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNALens**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1)</nobr> | <nobr>[Code](https://github.com/oomics/RNALens)</nobr> | <nobr>2025.07</nobr> | <nobr>Encoder-only</nobr> | <nobr>469M</nobr> | <nobr>Multispecies genomic + 5'UTR sequences</nobr> | <nobr>BPE</nobr> |

---

### DNA+RNA Foundation Models

Models pre-trained on **both DNA and RNA sequences**. These are not pure RNA FMs but their pre-training data includes RNA sequences and they can be applied to RNA downstream tasks.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**Evo**</nobr> | <nobr>[Paper](https://www.science.org/doi/10.1126/science.ado9336)</nobr> | <nobr>[Code](https://github.com/evo-design/evo)</nobr> | <nobr>2024.02</nobr> | <nobr>Decoder-only</nobr> | <nobr>7B</nobr> | <nobr>OpenGenome (2.7M prokaryotic + phage genomes)</nobr> | <nobr>SNT</nobr> |
| <nobr>**LucaOne**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-025-01044-4)</nobr> | <nobr>[Code](https://github.com/LucaOne/LucaOne)</nobr> | <nobr>2024.05</nobr> | <nobr>Encoder-only</nobr> | <nobr>1.8B</nobr> | <nobr>RefSeq + UniProt/PDB (800B tokens)</nobr> | <nobr>SNT / amino acid</nobr> |
| <nobr>**BSM**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2410.11499)</nobr> | - | <nobr>2024.10</nobr> | <nobr>Decoder-only</nobr> | <nobr>110M / 270M</nobr> | <nobr>RefSeq + web bio-seqs (DNA+RNA+Prot)</nobr> | <nobr>Mixed</nobr> |
| <nobr>**LAMAR**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1)</nobr> | <nobr>[Code](https://github.com/zhw-e8/LAMAR)</nobr> | <nobr>2024.10</nobr> | <nobr>Encoder-only</nobr> | <nobr>150M</nobr> | <nobr>Genome + transcriptome (225 mammals, 15M)</nobr> | <nobr>SNT</nobr> |
| <nobr>**Orthrus**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3)</nobr> | <nobr>[Code](https://huggingface.co/quietflamingo/orthrus-large-4-track)</nobr> | <nobr>2024.10</nobr> | <nobr>Encoder-only</nobr> | <nobr>1.3M / 10.1M</nobr> | <nobr>GENCODE + RefSeq + Zoonomia (32M transcripts)</nobr> | <nobr>SNT</nobr> |
| <nobr>**METAGENE-1**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2501.02045)</nobr> | <nobr>[Code](https://huggingface.co/metagene-ai/METAGENE-1)</nobr> | <nobr>2025.01</nobr> | <nobr>Decoder-only</nobr> | <nobr>7B</nobr> | <nobr>Wastewater metagenomic DNA/RNA (>1.5T bp)</nobr> | <nobr>BPE</nobr> |
| <nobr>**Life-Code**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2502.07299)</nobr> | - | <nobr>2025.02</nobr> | <nobr>Hybrid encoder</nobr> | - | <nobr>Multi-omics (DNA/RNA/Prot unified)</nobr> | <nobr>Codon</nobr> |
| <nobr>**Evo 2**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41586-026-10176-5)</nobr> | <nobr>[Code](https://github.com/ArcInstitute/evo2)</nobr> | <nobr>2026.02</nobr> | <nobr>Decoder-only</nobr> | <nobr>7B / 40B</nobr> | <nobr>OpenGenome2 (9T nt, 128K genomes)</nobr> | <nobr>SNT</nobr> |
| <nobr>**OmniNA**</nobr> | <nobr>[Paper](https://academic.oup.com/nar/article/54/6/gkag083/8528802)</nobr> | - | <nobr>2026.01</nobr> | <nobr>Generative FM</nobr> | - | <nobr>91.7M seqs + annotations (1076B bases)</nobr> | - |
| <nobr>**EDEN**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1)</nobr> | - | <nobr>2026.01</nobr> | <nobr>Generative FM</nobr> | <nobr>28B</nobr> | <nobr>9.7T biological tokens (DNA+RNA+Protein)</nobr> | - |

---

### Expression-based Foundation Models

Models operating on RNA-seq **gene expression profiles** (not raw nucleotide sequences). Listed for completeness.

| Model <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Architecture <img width=160/> | Params <img width=100/> | Pre-training Data <img width=260/> | Tokenization <img width=140/> |
|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**BulkRNABert**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2)</nobr> | <nobr>[Code](https://huggingface.co/InstaDeepAI/BulkRNABert)</nobr> | <nobr>2024.06</nobr> | <nobr>Encoder-only</nobr> | <nobr>6.01M</nobr> | <nobr>TCGA + GTEx + ENCODE (RNA-seq expr.)</nobr> | <nobr>Expression bin tokens</nobr> |
| <nobr>**MOJO**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1)</nobr> | <nobr>[Code](https://huggingface.co/InstaDeepAI/MOJO)</nobr> | <nobr>2025.06</nobr> | <nobr>Encoder (multimodal)</nobr> | <nobr>52.3M</nobr> | <nobr>TCGA (RNA-seq + DNA methylation)</nobr> | <nobr>Expression bin tokens</nobr> |

---

### Benchmarks & Evaluations

Benchmark datasets and systematic evaluations of RNA / nucleotide foundation models.

| Benchmark <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Year <img width=70/> | Focus <img width=300/> | Scale <img width=220/> |
|:----------|:-----:|:----:|:----:|:------|:------|
| <nobr>**BEACON**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2406.10391)</nobr> | <nobr>[Code](https://github.com/terry-r123/RNABenchmark)</nobr> | <nobr>2024.06</nobr> | <nobr>RNA (structural, functional, engineering)</nobr> | <nobr>13 tasks</nobr> |
| <nobr>**BEND**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2311.12570)</nobr> | <nobr>[Code](https://github.com/frederikkemarin/BEND)</nobr> | <nobr>2024.01</nobr> | <nobr>DNA LM biologically meaningful tasks</nobr> | <nobr>Multiple tasks</nobr> |
| <nobr>**RNA LLM Folding**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2410.16212)</nobr> | <nobr>[Code](https://github.com/sinc-lab/rna-llm-folding)</nobr> | <nobr>2024.10</nobr> | <nobr>RNA secondary structure prediction</nobr> | <nobr>6 RNA LLMs, 4 datasets</nobr> |
| <nobr>**GUE**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2306.15006)</nobr> | - | <nobr>2023.06</nobr> | <nobr>Genome understanding evaluation</nobr> | <nobr>36 datasets, 9 tasks</nobr> |
| <nobr>**RNAGym**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1)</nobr> | - | <nobr>2025.06</nobr> | <nobr>RNA fitness & structure prediction (2D/3D)</nobr> | <nobr>Fitness + structure tasks</nobr> |
| <nobr>**RNAscope**</nobr> | <nobr>[Paper](https://openreview.net/forum?id=zYAuJxcl2E)</nobr> | - | <nobr>2025.10</nobr> | <nobr>RNA (structure, interaction, function)</nobr> | <nobr>15 tasks, 1,253 experiments</nobr> |
| <nobr>**mRNABench**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1)</nobr> | <nobr>[Code](https://github.com/morrislab/mRNABench)</nobr> | <nobr>2025.07</nobr> | <nobr>Mature mRNA prediction tasks</nobr> | <nobr>10 datasets, 59 tasks, 135K experiments</nobr> |
| <nobr>**NABench**</nobr> | <nobr>[Paper](https://arxiv.org/html/2511.02888v1)</nobr> | - | <nobr>2025.11</nobr> | <nobr>Nucleic acid fitness prediction</nobr> | <nobr>2.6M+ mutated seqs, 160+ experiments</nobr> |
| <nobr>**RNA 3D Benchmark**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2503.21681)</nobr> | - | <nobr>2025.03</nobr> | <nobr>RNA 3D structure-function</nobr> | <nobr>7 tasks, 9 datasets</nobr> |
| <nobr>**Genomic LM RNA Eval**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-66899-y)</nobr> | - | <nobr>2025.08</nobr> | <nobr>RNA processes (ncRNA, m6A, splicing, TE)</nobr> | <nobr>11 genomic LMs, 4 RNA tasks</nobr> |
| <nobr>**DNA FM Benchmark**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65823-8)</nobr> | - | <nobr>2025.07</nobr> | <nobr>Genomic & genetic tasks (incl. RNA-relevant)</nobr> | <nobr>Multiple tasks</nobr> |
| <nobr>**DNALongBench**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65077-4)</nobr> | - | <nobr>2025.06</nobr> | <nobr>Long-range genomic tasks</nobr> | <nobr>5 tasks, up to 1M bp</nobr> |

---

### Surveys & Reviews

| Title <img width=350/> | Paper <img width=120/> | Year <img width=70/> | Scope <img width=400/> |
|:------|:-----:|:----:|:------|
| <nobr>**A Comparative Review of RNA Language Models**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2505.09087)</nobr> | <nobr>2025.05</nobr> | <nobr>Compares 13 RNA LMs + 3 DNA LMs + 1 protein LM</nobr> |
| <nobr>**Comprehensive Survey of Genome Language Models**</nobr> | <nobr>[Paper](https://academic.oup.com/bib/article/27/1/bbaf724/8426124)</nobr> | <nobr>2026.01</nobr> | <nobr>DNA/RNA genome LMs: limitations, long-range modeling</nobr> |
| <nobr>**LLMs in Bioinformatics: A Survey**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2503.04490)</nobr> | <nobr>2026.03</nobr> | <nobr>LLMs for DNA, RNA, proteins (ACL 2025 Findings, updated 2026)</nobr> |

---

---

---

---

---

## Paper List

A complete chronological list of all papers included in this survey.

### Foundation Models

<details open>
<summary><b>ncRNA Foundation Models</b></summary>

- [Informative RNA-base embedding for RNA structural alignment and clustering by a representation learning framework](https://doi.org/10.1093/nargab/lqac012) (2022.02) [![abs](https://img.shields.io/badge/abs-2022.02-b31b1b.svg)](https://doi.org/10.1093/nargab/lqac012) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/mana438/RNABERT)

  > Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.

- [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) (2022.08) [![abs](https://img.shields.io/badge/abs-2022.08-b31b1b.svg)](https://arxiv.org/abs/2204.00300) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/rnafm)

  > Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.

- [Multiple sequence-alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) (2023.12) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1093/nar/gkad1031) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yikunpku/RNA-MSM)

  > Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.

- [RNA-km: a tool for predicting RNA sequence properties using k-mer frequency features](https://doi.org/10.1101/2024.01.27.577533) (2024.01) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1101/2024.01.27.577533) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/gongtiansu/RNA-km)

  > Proposes RNA-km, a pre-trained encoder model that uses k-mer frequency features from 23M RNAcentral sequences to predict diverse RNA sequence properties including subcellular localization and modification sites.

- [RNAErnie: An RNA language model with structure-enhanced representations](https://www.nature.com/articles/s42256-024-00836-4) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00836-4) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LLM-EDA/RNAErnie)

  > Presents RNAErnie, a pre-trained RNA language model that integrates RNA sequence, secondary structure, and base-pairing information through a multi-level masking strategy, achieving superior performance across RNA downstream tasks.

- [ERNIE-RNA: An RNA Language Model with Structure-enhanced Representations](https://doi.org/10.1101/2024.03.17.585376) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.03.17.585376) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/ernierna-ss)

  > Develops ERNIE-RNA with structure-enhanced pre-training that jointly models RNA sequences and secondary structures, achieving improvements in RNA contact prediction, distance prediction, and secondary structure prediction.

- [DGRNA: a long-context RNA foundation model with bidirectional Mamba2](https://doi.org/10.1101/2024.10.31.621427) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.10.31.621427)

  > Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.

- [ChaRNABERT: A pre-trained RNA language model with learnable tokenization](https://arxiv.org/abs/2411.11808) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://arxiv.org/abs/2411.11808)

  > Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.

- [AIDO.RNA: A Scalable RNA Foundation Model](https://doi.org/10.1101/2024.11.28.625345) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://doi.org/10.1101/2024.11.28.625345) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)

  > Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.

- [RNAGenesis: A Generative RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Zaixi/RNAGenesis)

  > Proposes RNAGenesis, a 1B-parameter generative RNA foundation model combining encoder representations with diffusion-based generation, enabling both RNA understanding and de novo RNA sequence design.

- [HydraRNA: An Efficient RNA Foundation Model via Hybrid SSM and Attention](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) (2025.03) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/GuipengLi/HydraRNA)

  > Introduces HydraRNA, an efficient RNA foundation model using a hybrid architecture combining state space models (SSM) and attention mechanisms, achieving competitive performance with significantly reduced computational cost.

- [RiNALMo: General-Purpose RNA Language Models Can Generalize Well on Structure Prediction Tasks](https://arxiv.org/abs/2403.00043) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://arxiv.org/abs/2403.00043) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/lbcb-sci/RiNALMo)

  > Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.

- [BiRNA-BERT: An Efficient RNA Language Model with Adaptive Dual Tokenization](https://doi.org/10.1101/2024.07.02.601703) (2025.08) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://doi.org/10.1101/2024.07.02.601703) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/buetnlpbio/BiRNA-BERT)

  > Introduces BiRNA-BERT with a dual tokenization strategy combining single-nucleotide and BPE tokenization, enabling efficient processing of long RNA sequences while maintaining fine-grained nucleotide-level representations.

- [DLRNA-BERTa: A Transformer for RNA-Drug Binding Affinity Prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) (2025.09) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/IlPakoZ/RNA-BERTa9700)

  > Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.

- [RNAElectra: An ELECTRA-style RNA Foundation Model](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full)

  > Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.

</details>

<details open>
<summary><b>mRNA / CDS Foundation Models</b></summary>

- [GenSLMs: Genome-scale Language Models Reveal SARS-CoV-2 Evolutionary Dynamics](https://doi.org/10.1177/10943420231201154) (2023.01) [![abs](https://img.shields.io/badge/abs-2023.01-b31b1b.svg)](https://doi.org/10.1177/10943420231201154)

  > Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.

- [CodonBERT: Large Language Models for mRNA Unimodal and Multimodal Molecular Learning](https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1) (2023.09) [![abs](https://img.shields.io/badge/abs-2023.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Sanofi-Public/CodonBERT)

  > Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization, enabling both unimodal RNA and multimodal RNA-protein molecular learning.

- [CaLM: Codon Adaptation Language Model for mRNA Design](https://www.nature.com/articles/s42256-024-00791-0) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00791-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oxpig/CaLM)

  > Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.

- [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) (2025.01) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2410.12459)

  > Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.

- [Helix-mRNA: A Hybrid SSM-Attention Model for mRNA](https://arxiv.org/abs/2502.13785) (2025.02) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.13785) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/helical-ai/helix-mRNA)

  > Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.

- [GEMORNA: Generative mRNA Design via Codon and UTR Optimization](https://www.science.org/doi/10.1126/science.adr8470) (2025.05) [![abs](https://img.shields.io/badge/abs-2025.05-b31b1b.svg)](https://www.science.org/doi/10.1126/science.adr8470) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/RainaBio/GEMORNA)

  > Presents GEMORNA, a generative model for end-to-end mRNA design that jointly optimizes coding sequences and UTR regions, enabling the design of mRNAs with enhanced stability, translation efficiency, and immunogenicity profiles.

- [mRNABERT: A Pre-trained Language Model for mRNA Sequences](https://www.nature.com/articles/s41467-025-65340-8) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65340-8) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)

  > Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.

- [mRNA-GPT: An Autoregressive mRNA Foundation Model across Three Domains of Life](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) (2025.12) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ZHymLumine/mRNA-GPT/)

  > Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.

- [CodonMoE: Adapting DNA Language Models for RNA via Mixture-of-Experts](https://openreview.net/forum?id=TOUrnb1EaG) (2026.01) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://openreview.net/forum?id=TOUrnb1EaG)

  > Proposes CodonMoE, a parameter-efficient approach to adapt pre-trained DNA foundation models for RNA tasks using Mixture-of-Experts adapters with codon-aware routing for improved mRNA property prediction.

- [NUWA: A Codon Language Model for mRNA Coding Sequences](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) (2026.02) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/zysxmu/NUWA)

  > Proposes NUWA, a codon-level language model pre-trained on 115M multi-species mRNA coding sequences, learning codon usage patterns for downstream tasks including codon optimization and mRNA expression prediction.

- [mRNA-GPT: Full-Length mRNA Design via Autoregressive Generation with PPO](https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1)

  > Extends mRNA-GPT to full-length mRNA design (5'UTR+CDS+3'UTR) using autoregressive generation with PPO-based reinforcement learning to optimize translation efficiency and stability of generated mRNA sequences.

</details>

<details open>
<summary><b>UTR Foundation Models</b></summary>

- [UTR-LM: A 5' UTR Language Model for Predicting Translation Efficiency](https://www.nature.com/articles/s42256-024-00823-9) (2024.04) [![abs](https://img.shields.io/badge/abs-2024.04-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00823-9) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/utrlm-te_el)

  > Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.

- [3UTRBERT: Pre-trained Language Model for 3' UTR Sequences](https://doi.org/10.1101/2023.09.08.556883) (2024.07) [![abs](https://img.shields.io/badge/abs-2024.07-b31b1b.svg)](https://doi.org/10.1101/2023.09.08.556883) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yangyn533/3UTRBERT)

  > Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.

</details>

<details open>
<summary><b>Specific RNA Type Models</b></summary>

- [SpliceBERT: A Pre-trained Model for Self-supervised Learning of Pre-mRNA Splicing](https://doi.org/10.1093/bib/bbae163) (2023.01) [![abs](https://img.shields.io/badge/abs-2023.01-b31b1b.svg)](https://doi.org/10.1093/bib/bbae163) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/chenkenbio/SpliceBERT)

  > Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.

- [RFamLlama: Conditional RNA Generation by RNA Family](https://openreview.net/forum?id=dXnQedxEJD) (2024.08) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://openreview.net/forum?id=dXnQedxEJD) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/jinyuan22/RFamLlama-base)

  > Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.

- [PlantRNA-FM: A Plant RNA Foundation Model from Multi-species Transcriptomes](https://www.nature.com/articles/s42256-024-00946-z) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00946-z) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/PlantRNA-FM)

  > Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.

- [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) (2025.01) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/luukromeijn/lncRNA-Py)

  > Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.

- [G4mer: An Interpretable Transformer for G-quadruplex Prediction in the Transcriptome](https://www.nature.com/articles/s41467-025-65020-7) (2025.12) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65020-7) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Biociphers/g4mer)

  > Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.

</details>

<details open>
<summary><b>Structure-aware RNA Models</b></summary>

- [ATOM-1: Augmented Transformer with Structure-aware Chemical Mapping](https://doi.org/10.1101/2023.12.13.571579) (2023.12) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1101/2023.12.13.571579)

  > Proposes ATOM-1, an augmented transformer pre-trained on chemical mapping (SHAPE, DMS) sequencing data, learning structure-aware RNA representations that encode both sequence and experimentally-derived structural information.

- [RibonanzaNet: Deep Learning for RNA Chemical Mapping Prediction](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Shujun-He/RibonanzaNet)

  > Presents RibonanzaNet, a deep neural network trained on 2M RNA sequences with experimental chemical mapping data from Eterna, Rfam, and PDB, predicting RNA chemical reactivity profiles for structure determination.

- [OmniGenome: Aligning RNA Sequences with Secondary Structures](https://arxiv.org/abs/2407.11242) (2024.07) [![abs](https://img.shields.io/badge/abs-2024.07-b31b1b.svg)](https://arxiv.org/abs/2407.11242) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/OmniGenome-186M)

  > Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.

- [MP-RNA: Multi-Purpose RNA Foundation Model with Structure Awareness](https://aclanthology.org/2024.findings-emnlp.304/) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://aclanthology.org/2024.findings-emnlp.304/) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/MP-RNA)

  > Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.

- [RNA-TorsionBERT: Predicting RNA Backbone Torsion Angles](https://doi.org/10.1093/bioinformatics/btaf004) (2025.01) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://doi.org/10.1093/bioinformatics/btaf004) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/sayby/rna_torsionBERT)

  > Proposes RNA-TorsionBERT, a BERT model pre-trained on PDB RNA 3D structures to predict backbone torsion angles directly from RNA sequences, enabling rapid assessment of RNA 3D structural properties.

- [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) (2025.08) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/heqin-zhu/structRFM)

  > Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.

</details>

<details open>
<summary><b>RNA Generative Models</b></summary>

- [LoRNA: A Long-read RNA Foundation Model](https://doi.org/10.1101/2024.08.26.609813) (2024.08) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/2024.08.26.609813)

  > Introduces LoRNA, a foundation model designed for long-read RNA sequencing data, pre-trained on ~100M IsoSeq long reads (7B tokens) with specialized nucleotide and region tokenization for transcript-level analysis.

- [GenerRNA: A Generative Pre-trained Autoregressive RNA Language Model](https://doi.org/10.1371/journal.pone.0310814) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1371/journal.pone.0310814) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/pfnet/GenerRNA)

  > Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.

- [GARNET: A Generative RNA Design Model from Microbial Genomes](https://www.nature.com/articles/s41467-024-54812-y) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s41467-024-54812-y) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Doudna-lab/GARNET_DL)

  > Develops GARNET, a generative model combining a decoder with a GNN, trained on 30M microbial genome sequences (17B nucleotides) from GTDB for designing novel functional RNA sequences with desired structural properties.

- [RNAtranslator: Protein-conditioned RNA Sequence Generation](https://doi.org/10.1371/journal.pcbi.1013541) (2025.03) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://doi.org/10.1371/journal.pcbi.1013541) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/SobhanShukueian/rnatranslator)

  > Proposes RNAtranslator, a 41.4M-parameter encoder-decoder model trained on 26M RNA-protein interaction pairs for generating RNA sequences conditioned on protein binding partners, enabling rational RNA aptamer design.

- [EVA: Evolutionary Versatile Architect for Long-context RNA Generation](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)

  > Introduces EVA, a Mixture-of-Experts decoder model for long-context RNA sequence generation, trained on 114M+ full-length RNA sequences for generating diverse functional RNA molecules at unprecedented lengths.

</details>

<details open>
<summary><b>General / Other RNA Models</b></summary>

- [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) (2023.07) [![abs](https://img.shields.io/badge/abs-2023.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ComDec/unirna_tf)

  > Presents Uni-RNA, a 400M-parameter universal RNA model pre-trained on 1B sequences from RNAcentral, MG-RAST, and MGnify, covering RNA across diverse species for general-purpose RNA representation learning.

- [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oomics/RNALens)

  > Introduces RNALens, a 469M-parameter multi-task RNA foundation model pre-trained on multispecies genomic and 5'UTR sequences using BPE tokenization, supporting diverse RNA analysis tasks within a unified framework.

</details>

<details open>
<summary><b>DNA+RNA Foundation Models</b></summary>

- [Sequence Modeling and Design from Molecular to Genome Scale with Evo](https://www.science.org/doi/10.1126/science.ado9336) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.science.org/doi/10.1126/science.ado9336) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/evo-design/evo)

  > Presents Evo, a 7B-parameter genomic foundation model using StripedHyena architecture, pre-trained on 2.7M prokaryotic and phage genomes at single-nucleotide resolution, enabling sequence modeling and design from molecular to genome scale.

- [LucaOne: A Unified Foundation Model for DNA, RNA and Protein](https://www.nature.com/articles/s42256-025-01044-4) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-025-01044-4) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/LucaOne/LucaOne)

  > Introduces LucaOne, a 1.8B-parameter unified model pre-trained on 800B tokens from RefSeq, UniProt, and PDB, jointly modeling DNA, RNA, and protein sequences for cross-modal biological sequence understanding.

- [BSM: Biological Sequence Model for Mixed-modal Pretraining](https://arxiv.org/abs/2410.11499) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.11499)

  > Proposes BSM (110M/270M parameters), a biological sequence model with mixed-modal pre-training on DNA, RNA, and protein sequences from RefSeq and web-collected biological data for unified sequence representation.

- [LAMAR: A Language Model for Mammalian and Viral Genomes and Transcriptomes](https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/zhw-e8/LAMAR)

  > Develops LAMAR, a 150M-parameter language model pre-trained on genomes and transcriptomes from 225 mammalian species (15M sequences), capturing mammalian-specific and viral genomic patterns for RNA and DNA tasks.

- [Orthrus: Contrastive Learning of Transcript Isoforms and Orthologs via Mamba](https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/quietflamingo/orthrus-large-4-track)

  > Introduces Orthrus, a Mamba-based model using contrastive learning on 32M transcript sequences from GENCODE, RefSeq, and Zoonomia to learn representations of transcript isoforms and cross-species orthologs.

- [METAGENE-1: A 7B Metagenomic Foundation Model for DNA and RNA](https://arxiv.org/abs/2501.02045) (2025.01) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2501.02045) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/metagene-ai/METAGENE-1)

  > Presents METAGENE-1, a 7B-parameter metagenomic foundation model pre-trained on >1.5 trillion base pairs of wastewater metagenomic DNA and RNA sequences using BPE tokenization for pathogen detection and biosurveillance.

- [Life-Code: A Unified Foundation Model via Central Dogma](https://arxiv.org/abs/2502.07299) (2025.02) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.07299)

  > Proposes Life-Code, a unified foundation model that jointly models DNA, RNA, and protein following the central dogma of molecular biology, using codon-level tokenization to capture cross-modal biological relationships.

- [OmniNA: A Foundation Model for Nucleotide Sequences and Annotations](https://academic.oup.com/nar/article/54/6/gkag083/8528802) (2026.01) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://academic.oup.com/nar/article/54/6/gkag083/8528802)

  > Introduces OmniNA, a generative foundation model pre-trained on 91.7M nucleotide sequences with annotations (1076B bases), jointly modeling sequences and functional annotations for unified nucleotide analysis.

- [EDEN: A 28B Foundation Model for Programmable Gene Insertion](https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1) (2026.01) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1)

  > Develops EDEN, a 28B-parameter foundation model pre-trained on 9.7 trillion biological tokens (DNA+RNA+Protein) for programmable gene insertion, enabling precise genome engineering guided by learned sequence representations.

- [Genome Modeling and Design Across All Domains of Life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5) (2026.02) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.nature.com/articles/s41586-026-10176-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ArcInstitute/evo2)

  > Presents Evo 2 (7B/40B parameters), a next-generation genomic foundation model trained on 9 trillion nucleotides from 128K genomes spanning all domains of life, enabling genome-scale modeling, understanding, and design.

</details>

<details open>
<summary><b>Expression-based Foundation Models</b></summary>

- [BulkRNABert: A Pre-trained Model for Bulk RNA-seq Expression Data](https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2) (2024.06) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/InstaDeepAI/BulkRNABert)

  > Presents BulkRNABert, a 6M-parameter encoder model pre-trained on bulk RNA-seq gene expression profiles from TCGA, GTEx, and ENCODE using expression bin tokens for cancer classification and gene expression analysis.

- [MOJO: A Multi-omics Foundation Model for RNA-seq and Methylation](https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/InstaDeepAI/MOJO)

  > Introduces MOJO, a 52.3M-parameter multimodal encoder pre-trained on TCGA RNA-seq expression and DNA methylation data, enabling joint multi-omics analysis for cancer subtyping and biomarker discovery.

</details>

### Benchmarks & Evaluations

- [DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genome](https://arxiv.org/abs/2306.15006) (2023.06) [![abs](https://img.shields.io/badge/abs-2023.06-b31b1b.svg)](https://arxiv.org/abs/2306.15006)

  > Introduces DNABERT-2 along with GUE (Genome Understanding Evaluation), a benchmark of 36 datasets across 9 task categories for evaluating genome foundation models.

- [BEND: Benchmarking DNA Language Models on Biologically Meaningful Tasks](https://arxiv.org/abs/2311.12570) (2024.01) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://arxiv.org/abs/2311.12570) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/frederikkemarin/BEND)

  > Proposes BEND, a benchmark of biologically meaningful tasks for evaluating DNA language models, covering gene regulation, chromatin accessibility, and conservation prediction.

- [BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://arxiv.org/abs/2406.10391) (2024.06) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://arxiv.org/abs/2406.10391) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/terry-r123/RNABenchmark)

  > Introduces BEACON, a comprehensive benchmark covering 13 RNA tasks across structural, functional, and engineering categories for systematic evaluation of RNA language models.

- [Comprehensive Benchmarking of LLMs for RNA Secondary Structure Prediction](https://arxiv.org/abs/2410.16212) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.16212) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/sinc-lab/rna-llm-folding)

  > Systematically benchmarks 6 RNA large language models on RNA secondary structure prediction across 4 datasets, revealing performance gaps and limitations of current LLM-based folding approaches.

- [Comprehensive Benchmark for RNA 3D Structure-Function Modeling](https://arxiv.org/abs/2503.21681) (2025.03) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://arxiv.org/abs/2503.21681)

  > Presents a comprehensive benchmark for RNA 3D structure-function modeling with 7 tasks across 9 datasets, evaluating how well models capture tertiary structural information for functional prediction.

- [RNAGym: A Benchmark for RNA Fitness and Structure Prediction](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1)

  > Presents RNAGym, a benchmark for evaluating RNA foundation models on fitness landscape prediction and 2D/3D structure prediction tasks with standardized evaluation protocols.

- [DNALongBench: Benchmarking Long-range Genomic Tasks](https://www.nature.com/articles/s41467-025-65077-4) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65077-4)

  > Introduces DNALongBench, a benchmark of 5 long-range genomic tasks with sequences up to 1M base pairs for evaluating foundation models on long-context genomic understanding.

- [mRNABench: Benchmarking Nucleotide FMs on Mature mRNA Tasks](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/morrislab/mRNABench)

  > Proposes mRNABench with 10 datasets, 59 tasks, and 135K experiments for benchmarking nucleotide foundation models specifically on mature mRNA prediction tasks including stability and translation efficiency.

- [Benchmarking DNA Foundation Models for Genomic and Genetic Tasks](https://www.nature.com/articles/s41467-025-65823-8) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65823-8)

  > Provides a systematic benchmark of DNA foundation models across genomic and genetic tasks, including RNA-relevant tasks, evaluating representational capabilities and transfer learning performance.

- [Benchmarking Pre-trained Genomic Language Models for RNA Predictive Tasks](https://www.nature.com/articles/s41467-025-66899-y) (2025.08) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.nature.com/articles/s41467-025-66899-y)

  > Systematically benchmarks 11 pre-trained genomic language models on 4 RNA-specific tasks including ncRNA classification, m6A modification, splicing, and translation efficiency prediction.

- [RNAscope: Comprehensive Benchmark for RNA Foundation Models](https://openreview.net/forum?id=zYAuJxcl2E) (2025.10) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://openreview.net/forum?id=zYAuJxcl2E)

  > Introduces RNAscope, a comprehensive benchmark with 15 tasks and 1,253 experiments for evaluating RNA foundation models across structure prediction, interaction, and function annotation.

- [NABench: Nucleic Acid Fitness Prediction Benchmark](https://arxiv.org/html/2511.02888v1) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://arxiv.org/html/2511.02888v1)

  > Introduces NABench, a nucleic acid fitness prediction benchmark with 2.6M+ mutated sequences and 160+ experimental conditions for evaluating foundation models on RNA and DNA fitness landscapes.


### Surveys & Reviews

- [A Comparative Review of RNA Language Models](https://arxiv.org/abs/2505.09087) (2025.05) [![abs](https://img.shields.io/badge/abs-2025.05-b31b1b.svg)](https://arxiv.org/abs/2505.09087)

  > Provides a comparative review of 13 RNA language models, 3 DNA language models, and 1 protein language model, analyzing their architectures, pre-training strategies, and performance across RNA downstream tasks.

- [A Comprehensive Survey of Genome Language Models in Bioinformatics](https://academic.oup.com/bib/article/27/1/bbaf724/8426124) (2026.01) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://academic.oup.com/bib/article/27/1/bbaf724/8426124)

  > Surveys genome language models for DNA and RNA, discussing architectural innovations, pre-training strategies, limitations in long-range modeling, and future directions for biological sequence understanding.

- [Large Language Models in Bioinformatics: A Survey](https://arxiv.org/abs/2503.04490) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://arxiv.org/abs/2503.04490)

  > Comprehensive survey of large language models applied to bioinformatics including DNA, RNA, and protein domains, covering model architectures, training paradigms, and applications across biological sequences.



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
| <nobr>**SNT**</nobr> | <nobr>Single Nucleotide Tokenization (A/U/C/G or A/T/C/G)</nobr> |
| <nobr>**MLM**</nobr> | <nobr>Masked Language Modeling</nobr> |
| <nobr>**BPE**</nobr> | <nobr>Byte Pair Encoding</nobr> |
| <nobr>**MoE**</nobr> | <nobr>Mixture of Experts</nobr> |
| <nobr>**SSM**</nobr> | <nobr>State Space Model</nobr> |
| <nobr>**CDS**</nobr> | <nobr>Coding Sequence</nobr> |
| <nobr>**UTR**</nobr> | <nobr>Untranslated Region</nobr> |
| <nobr>**ncRNA**</nobr> | <nobr>Non-coding RNA</nobr> |

---

*Last updated: April 2026*
