# Awesome RNA Foundation Models

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/) [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) [![Last Update](https://img.shields.io/badge/Last_Update-2026.05-blue.svg)]()

A curated, continuously updated catalog of **RNA sequence foundation models**, covering reusable RNA/mRNA/CDS/UTR sequence backbones and checkpoints, specialized RNA-family or structure-aware sequence models, adapted / derived RNA language models, and generative RNA sequence models.

> **Scope.** Included model entries must introduce or release a reusable sequence model, backbone, or checkpoint whose pre-training / large-scale training corpus explicitly includes RNA, mRNA, CDS, UTR, transcript, ncRNA, RNA metagenomic, or RNA/transcript-derived sequence data, and must support embedding extraction, fine-tuning, generation, or broad transfer to RNA downstream tasks. Downstream-only predictors/designers, reverse-translation or inverse-folding pipelines, RNA 3D prediction systems, DNA/protein/multi-omics FMs with no explicit RNA/transcript sequence pre-training signal, expression-profile/RNA-seq feature models, protein-only models, single-cell foundation models, and non-model resources are excluded from model entries; benchmarks and surveys are listed separately.

## Table of Contents

- [Model Timeline](#model-timeline) — Auto-generated timeline for confirmed RNA sequence foundation model entries
- [Paper List](#paper-list) — RNA sequence foundation models (4 views), Benchmarks, Surveys
- [Detailed Tables](#detailed-tables) — Detailed tables for all 52 model entries, 12 benchmarks, 3 surveys
- [Abbreviations](#abbreviations)
- [Contributing](#contributing)

---

## Model Timeline

Timeline of 52 confirmed RNA sequence foundation model entries, generated from `data/papers.yaml` whenever confirmed metadata is refreshed.

**Date note:** timeline dates use each model's first public release or preprint when available; paper-list dates below use formal publication or conference dates when available.

**Interactive view:** [open the SVG timeline](https://raw.githack.com/COLA-Laboratory/Awesome-RNA-Foundation-Models/main/assets/model_timeline-95cc8d834b11.svg) to click model labels and source papers.

[![RNA foundation model timeline](assets/model_timeline-95cc8d834b11.svg)](https://raw.githack.com/COLA-Laboratory/Awesome-RNA-Foundation-Models/main/assets/model_timeline-95cc8d834b11.svg)

---


## Paper List

A survey list of RNA sequence foundation models and RNA-inclusive sequence foundation models included in this survey. Each entry shows the model/resource name separately from the official paper title. Four classification views are provided below — click to expand/collapse each view.

<!-- **Classification rules**:

- **Core RNA Foundation Models**: reusable RNA or mRNA sequence backbones pre-trained on raw nucleotide sequences for broad downstream transfer or generation.
- **Specialized RNA Foundation Models**: RNA-specific pre-trained models whose scope is limited to a subtype, species, structural modality, or narrow biological question.
- **Adapted / Derived RNA Models**: models that adapt, extend, or transfer existing pre-trained components but still yield a reusable RNA language model.
- **Broad RNA-Inclusive Foundation Models**: broader nucleotide, biological-sequence, central-dogma, or multi-modal foundation models whose pre-training explicitly includes RNA / transcript sequences and whose checkpoints support reusable sequence representations, fine-tuning, or generation for RNA-relevant tasks.
- **Excluded from this list**: downstream-only predictors/designers, reverse-translation or inverse-folding pipelines, RNA 3D prediction systems, DNA/protein/multi-omics FMs with no explicit RNA/transcript sequence pre-training signal, expression-profile/RNA-seq feature models, protein-only models, single-cell foundation models, non-model datasets/benchmarks/surveys as model entries, and papers with no reusable sequence model. -->

> **Date convention**: Dates shown in this section use the official publication or conference month when available; otherwise they use the linked preprint month and are marked `preprint`. Workshop-only entries are marked `workshop`.

<details open>
<summary><b>RNA Sequence Foundation Models</b></summary>

<blockquote>

<details open>
<summary><b>View 1: Classified by Foundation-model Scope</b></summary>

<blockquote>

<details open>
<summary><b>Core RNA Foundation Models (23)</b></summary>

Primary contribution is a reusable RNA or mRNA sequence foundation model pre-trained on raw nucleotide sequences and intended for broad downstream transfer or generation.

- **RNAFM** — [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) (2022.04, preprint) [![abs](https://img.shields.io/badge/abs-2022.04-b31b1b.svg)](https://arxiv.org/abs/2204.00300) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2204.00300) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/rnafm)

  > Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.

- **Uni-RNA** — [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) (2023.07, preprint) [![abs](https://img.shields.io/badge/abs-2023.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ComDec/unirna_tf)

  > Presents Uni-RNA, a 400M-parameter universal RNA model pre-trained on 1B sequences from RNAcentral, MG-RAST, and MGnify, covering RNA across diverse species for general-purpose RNA representation learning.

- **RNAErnie** — [Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning](https://www.nature.com/articles/s42256-024-00836-4) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00836-4) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LLM-EDA/RNAErnie)

  > Presents RNAErnie, an RNA-focused pre-trained model that combines motif-aware pretraining with type-guided fine-tuning for diverse RNA sequence analysis tasks.

- **DGRNA** — [DGRNA: a long-context RNA foundation model with bidirectional attention Mamba2](https://doi.org/10.1101/2024.10.31.621427) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.10.31.621427) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.10.31.621427)

  > Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.

- **HELM** — [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.12459) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2410.12459)

  > Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.

- **GenerRNA** — [GenerRNA: A generative pre-trained language model for de novo RNA design](https://doi.org/10.1371/journal.pone.0310814) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1371/journal.pone.0310814) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/pfnet/GenerRNA)

  > Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.

- **AIDO.RNA** — [A Large-Scale Foundation Model for RNA Function and Structure Prediction](https://doi.org/10.1101/2024.11.28.625345) (2024.11, preprint) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://doi.org/10.1101/2024.11.28.625345) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.11.28.625345) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)

  > Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.

- **ChaRNABERT** — [Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models](https://openreview.net/forum?id=cAiECLDjzF) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=cAiECLDjzF)

  > Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.

- **Helix-mRNA** — [Helix-mRNA: A Hybrid Foundation Model For Full Sequence mRNA Therapeutics](https://openreview.net/forum?id=Ky0CkFiVhu) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=Ky0CkFiVhu) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/helical-ai/helix-mRNA)

  > Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.

- **RiNALMo** — [RiNALMo: general-purpose RNA language models can generalize well on structure prediction tasks](https://www.nature.com/articles/s41467-025-60872-5) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-60872-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/lbcb-sci/RiNALMo)

  > Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.

- **RNALens** — [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) (2025.07, preprint) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oomics/RNALens)

  > Introduces RNALens, a 469M-parameter multi-task RNA foundation model pre-trained on multispecies genomic and 5'UTR sequences using BPE tokenization, supporting diverse RNA analysis tasks within a unified framework.

- **RNA-BERTa** — [DLRNA-BERTa: A transformer approach for RNA-drug binding affinity prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) (2025.09, preprint) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/IlPakoZ/RNA-BERTa9700)

  > Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.

- **CodonFM** — [Introducing the CodonFM Open Model for RNA Design and Analysis](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) (2025.10) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NVIDIA-Digital-Bio/CodonFM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/nvidia/NV-CodonFM-Encodon-1B-v1)

  > Releases NVIDIA CodonFM / Encodon, a family of codon-level masked language models trained on 131M RefSeq protein-coding sequences for mRNA design, codon optimization, and synonymous or missense variant interpretation.

- **ERNIE-RNA** — [ERNIE-RNA: an RNA language model with structure-enhanced representations](https://www.nature.com/articles/s41467-025-64972-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-64972-0) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/ernierna-ss)

  > Develops ERNIE-RNA with base-pairing-aware attention bias for structure-enhanced pre-training on RNAcentral ncRNAs, improving structure and function prediction tasks.

- **BiRNA-BERT** — [BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization](https://www.nature.com/articles/s42003-025-08982-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s42003-025-08982-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/buetnlpbio/BiRNA-BERT)

  > Introduces BiRNA-BERT, a 117M-parameter encoder trained on 36M ncRNA sequences with adaptive dual tokenization combining nucleotide-level and BPE representations.

- **HydraRNA** — [HydraRNA: a hybrid architecture based full-length RNA language model](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/GuipengLi/HydraRNA)

  > Introduces HydraRNA, a full-length RNA language model using a hybrid bidirectional state space and attention architecture for both coding and non-coding RNA tasks.

- **mRNABERT** — [mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset](https://www.nature.com/articles/s41467-025-65340-8) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65340-8) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)

  > Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.

- **mRNA-GPT** — [Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) (2025.12, preprint) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ZHymLumine/mRNA-GPT/)

  > Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.

- **NUWA** — [Large mRNA language foundation modeling with NUWA for unified sequence perception and generation](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) (2026.02, preprint) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/zysxmu/NUWA)

  > Proposes NUWA, a large mRNA foundation model pre-trained on 115M multi-species coding sequences for unified mRNA sequence perception and generation.

- **RNAElectra** — [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://doi.org/10.64898/2026.03.15.711950) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://doi.org/10.64898/2026.03.15.711950) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.64898/2026.03.15.711950)

  > Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.

- **RNAret** — [Retentive Network promotes efficient RNA language modeling of long sequences](https://www.nature.com/articles/s42003-026-09757-x) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s42003-026-09757-x) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/DrBlackZJU/RNAret/)

  > Introduces RNAret, a Retentive Network-based RNA language model pre-trained with masked language modeling on 29.8M RNAcentral sequences, enabling efficient long-sequence RNA representation learning across interaction, structure, and classification tasks.

- **EVA** — [A Long-Context Generative Foundation Model Deciphers RNA Design Principles](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)

  > Introduces EVA, a Mixture-of-Experts decoder model for long-context RNA sequence generation, trained on 114M+ full-length RNA sequences for generating diverse functional RNA molecules at unprecedented lengths.

- **RIBOSPAN** — [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](https://arxiv.org/abs/2608.22849v2) (2026.08, preprint) [![abs](https://img.shields.io/badge/abs-2026.08-b31b1b.svg)](https://arxiv.org/abs/2608.22849v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2608.22849v2)

  > Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution.

</details>

<details open>
<summary><b>Specialized RNA Foundation Models (20)</b></summary>

RNA-specific pre-training is present, but the scope is constrained by RNA subtype, species, structural modality, or a narrow biological question.

- **RNABert** — [Informative RNA base embedding for RNA structural alignment and clustering by deep representation learning](https://doi.org/10.1093/nargab/lqac012) (2022.01) [![abs](https://img.shields.io/badge/abs-2022.01-b31b1b.svg)](https://doi.org/10.1093/nargab/lqac012) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/mana438/RNABERT)

  > Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.

- **GenSLM** — [GenSLMs: Genome-scale language models reveal SARS-CoV-2 evolutionary dynamics](https://doi.org/10.1177/10943420231201154) (2023.11) [![abs](https://img.shields.io/badge/abs-2023.11-b31b1b.svg)](https://doi.org/10.1177/10943420231201154)

  > Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.

- **ATOM-1** — [ATOM-1: A Foundation Model for RNA Structure and Function Built on Chemical Mapping Data](https://doi.org/10.1101/2023.12.13.571579) (2023.12, preprint) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1101/2023.12.13.571579) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2023.12.13.571579)

  > Proposes ATOM-1, a foundation model trained on chemical mapping data to learn RNA structure-aware representations for secondary and tertiary structure probing and RNA function prediction.

- **RNAMSM** — [Multiple sequence alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) (2024.01) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1093/nar/gkad1031) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yikunpku/RNA-MSM)

  > Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.

- **RNA-km** — [Language models enable zero-shot prediction of RNA secondary structures including pseudoknots](https://doi.org/10.1101/2024.01.27.577533) (2024.01, preprint) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1101/2024.01.27.577533) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.01.27.577533) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/gongtiansu/RNA-km)

  > Proposes RNA-km, a self-supervised RNA language model trained on 23M ncRNA sequences with k-mer masking and relative positional encoding, enabling zero-shot RNA secondary structure prediction including pseudoknots.

- **CaLM** — [Codon language embeddings provide strong signals for use in protein engineering](https://www.nature.com/articles/s42256-024-00791-0) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00791-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oxpig/CaLM)

  > Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.

- **SpliceBERT** — [Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction](https://doi.org/10.1093/bib/bbae163) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://doi.org/10.1093/bib/bbae163) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/chenkenbio/SpliceBERT)

  > Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.

- **UTR-LM** — [A 5′ UTR language model for decoding untranslated regions of mRNA and function predictions](https://www.nature.com/articles/s42256-024-00823-9) (2024.04) [![abs](https://img.shields.io/badge/abs-2024.04-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00823-9) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/utrlm-te_el)

  > Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.

- **RFamLlama** — [RFamLlama: an efficient conditional language model for RNA sequence generation across diverse structural families](https://openreview.net/forum?id=dXnQedxEJD) (2024.06, workshop) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://openreview.net/forum?id=dXnQedxEJD) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/jinyuan22/RFamLlama-base)

  > Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.

- **CodonBERT** — [CodonBERT large language model for mRNA vaccines](https://doi.org/10.1101/gr.278870.123) (2024.08) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/gr.278870.123) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Sanofi-Public/CodonBERT)

  > Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization for mRNA sequence representation and vaccine-related design tasks.

- **LoRNA SH** — [A long-context RNA foundation model for predicting transcriptome architecture](https://doi.org/10.1101/2024.08.26.609813) (2024.08, preprint) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/2024.08.26.609813) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.08.26.609813)

  > Introduces LoRNA SH, a StripedHyena-based long-context RNA foundation model trained on full-length transcriptome architecture data to predict isoform abundance, isoform structure, and variant effects.

- **3UTRBERT** — [Deciphering 3'UTR Mediated Gene Regulation Using Interpretable Deep Representation Learning](https://doi.org/10.1002/advs.202407013) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1002/advs.202407013) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yangyn533/3UTRBERT)

  > Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.

- **MP-RNA** — [MP-RNA: Unleashing Multi-species RNA Foundation Model via Calibrated Secondary Structure Prediction](https://aclanthology.org/2024.findings-emnlp.304/) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://aclanthology.org/2024.findings-emnlp.304/) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/MP-RNA)

  > Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.

- **PlantRNA-FM** — [An interpretable RNA foundation model for exploring functional RNA motifs in plants](https://www.nature.com/articles/s42256-024-00946-z) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00946-z) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/PlantRNA-FM)

  > Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.

- **LncRNA-BERT** — [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/luukromeijn/lncRNA-Py)

  > Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.

- **OmniGenome** — [Bridging Sequence-Structure Alignment in RNA Foundation Models](https://ojs.aaai.org/index.php/AAAI/article/view/35500) (2025.04) [![abs](https://img.shields.io/badge/abs-2025.04-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/35500) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/OmniGenome-186M)

  > Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.

- **StructRFM** — [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) (2025.08, preprint) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/heqin-zhu/structRFM)

  > Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.

- **G4mer** — [G4mer: An RNA language model for transcriptome-wide identification of G-quadruplexes and disease variants from population-scale genetic data](https://www.nature.com/articles/s41467-025-65020-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65020-7) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Biociphers/g4mer)

  > Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.

- **miRBind2** — [miRBind2 enables sequence-only prediction of miRNA binding and transcript repression](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1)

  > MotivationMicroRNAs (miRNAs) regulate gene expression by guiding Argonaute proteins to partially complementary sites on target RNAs.

- **Orthrus** — [Orthrus: toward evolutionary and functional RNA foundation models](https://www.nature.com/articles/s41592-026-03064-3) (2026.04) [![abs](https://img.shields.io/badge/abs-2026.04-b31b1b.svg)](https://www.nature.com/articles/s41592-026-03064-3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/quietflamingo/orthrus-large-4-track)

  > Introduces Orthrus, a Mamba-based mature RNA foundation model using contrastive learning on transcript isoforms and cross-species orthologs to learn evolutionary and functional RNA representations.

</details>

<details open>
<summary><b>Adapted / Derived RNA Models (4)</b></summary>

The work mainly adapts, extends, or composes existing foundation models / pre-trained components for RNA-specific analysis or design, rather than introducing a fully new RNA backbone.

- **mRNA-FM** — [RNA-FM: The RNA Foundation Model](https://github.com/ml4bio/RNA-FM) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://github.com/ml4bio/RNA-FM) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ml4bio/RNA-FM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/mrnafm)

  > Adds mRNA-FM as the coding-sequence extension of RNA-FM, pre-trained on 45M mRNA CDS sequences to provide contextual embeddings for mRNA and protein-related downstream tasks.

- **RNAGenesis** — [RNAGenesis: A Generalist Foundation Model for Functional RNA Therapeutics](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) (2024.12, preprint) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Zaixi/RNAGenesis)

  > Proposes RNAGenesis, a 1B-parameter generative RNA model that integrates sequence representation, structure prediction, and de novo functional design, listed here as an adapted / derived RNA design model rather than a core ncRNA pre-training-only FM.

- **ProtRNA** — [ProtRNA: A protein-derived RNA language model by cross-modality transfer learning](https://www.sciencedirect.com/science/article/pii/S2405471225002042) (2025.09) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S2405471225002042) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/roxie-zhang/ProtRNA)

  > Adapts the protein language model ESM-2 to RNA through cross-modality transfer learning on 6M RNAcentral sequences, providing a parameter- and data-efficient RNA language model.

- **codonGPT** — [codonGPT: reinforcement learning on a generative language model enables scalable mRNA design](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) (2025.12) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NanilTx/codonGPT_pub) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/naniltx/codonGPT)

  > Introduces codonGPT, a GPT-style generative language model trained exclusively on 338,417 coding mRNA sequences with codon-level tokenization, and demonstrates reinforcement learning for constrained mRNA sequence optimization.

</details>

<details open>
<summary><b>Broad RNA-Inclusive Foundation Models (5)</b></summary>

The model is not RNA-only, but its pre-training corpus explicitly includes RNA / transcript sequences and the checkpoint supports reusable sequence representations, fine-tuning, or generation relevant to RNA tasks.

- **METAGENE-1** — [METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring](https://arxiv.org/abs/2501.02045) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2501.02045) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2501.02045) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/metagene-ai/METAGENE-1)

  > Introduces METAGENE-1, a 7B autoregressive metagenomic foundation model pre-trained on diverse metagenomic DNA and RNA sequences, supporting genomic sequence embeddings, pathogen detection, biosurveillance, and pandemic monitoring tasks.

- **Life-Code** — [Life-Code: Central Dogma Modeling with Multi-Omics Sequence Unification](https://arxiv.org/abs/2502.07299) (2025.02, preprint) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.07299) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2502.07299)

  > Introduces Life-Code, a central-dogma sequence foundation framework that unifies DNA, RNA/cDNA, amino-acid, and multi-omics information into nucleotide-based sequences with codon tokenization and masked modeling over coding and non-coding regions.

- **LucaOne** — [Generalized biological foundation model with unified nucleic acid and protein language](https://www.nature.com/articles/s42256-025-01044-4) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s42256-025-01044-4) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/LucaOne/LucaOneApp) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LucaGroup/LucaOne-default-step36M)

  > Introduces LucaOne, a unified biological foundation model trained on nucleic acid (DNA and RNA) and protein sequences from 169,861 species, supporting reusable embeddings and downstream tasks involving DNA, RNA, proteins, and their interrelated pairs.

- **Evo 2** — [Genome Modeling and Design Across All Domains of Life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s41586-026-10176-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ArcInstitute/evo2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/arcinstitute/evo2_40b)

  > Introduces Evo 2, an open biological sequence foundation model trained on OpenGenome2 across all domains of life; the released OpenGenome2 composition includes eukaryotic mRNAs and ncRNA sources such as RNAcentral and Rfam, enabling broad nucleotide-sequence prediction and generation.

- **OmniNA** — [A foundation model for nucleotide sequences](https://academic.oup.com/nar/article/54/6/gkag083/8528802) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://academic.oup.com/nar/article/54/6/gkag083/8528802) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/xilinshen/OmniNA) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/XLS/OmniNA-1.7B)

  > Introduces OmniNA, an annotation-aware generative foundation model for nucleic acid sequences trained on NCBI NT nucleotide sequences and annotations spanning genomic DNA and RNA, with reusable representations for genomics and transcriptomics tasks.

</details>

</blockquote>

</details>

<details open>
<summary><b>View 2: Classified by RNA / Data Focus</b></summary>

<blockquote>

<details open>
<summary><b>ncRNA Sequence Models (16)</b></summary>

- **RNABert** — [Informative RNA base embedding for RNA structural alignment and clustering by deep representation learning](https://doi.org/10.1093/nargab/lqac012) (2022.01) [![abs](https://img.shields.io/badge/abs-2022.01-b31b1b.svg)](https://doi.org/10.1093/nargab/lqac012) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/mana438/RNABERT)

  > Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.

- **RNAFM** — [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) (2022.04, preprint) [![abs](https://img.shields.io/badge/abs-2022.04-b31b1b.svg)](https://arxiv.org/abs/2204.00300) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2204.00300) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/rnafm)

  > Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.

- **RNAMSM** — [Multiple sequence alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) (2024.01) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1093/nar/gkad1031) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yikunpku/RNA-MSM)

  > Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.

- **RNA-km** — [Language models enable zero-shot prediction of RNA secondary structures including pseudoknots](https://doi.org/10.1101/2024.01.27.577533) (2024.01, preprint) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1101/2024.01.27.577533) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.01.27.577533) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/gongtiansu/RNA-km)

  > Proposes RNA-km, a self-supervised RNA language model trained on 23M ncRNA sequences with k-mer masking and relative positional encoding, enabling zero-shot RNA secondary structure prediction including pseudoknots.

- **RNAErnie** — [Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning](https://www.nature.com/articles/s42256-024-00836-4) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00836-4) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LLM-EDA/RNAErnie)

  > Presents RNAErnie, an RNA-focused pre-trained model that combines motif-aware pretraining with type-guided fine-tuning for diverse RNA sequence analysis tasks.

- **DGRNA** — [DGRNA: a long-context RNA foundation model with bidirectional attention Mamba2](https://doi.org/10.1101/2024.10.31.621427) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.10.31.621427) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.10.31.621427)

  > Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.

- **AIDO.RNA** — [A Large-Scale Foundation Model for RNA Function and Structure Prediction](https://doi.org/10.1101/2024.11.28.625345) (2024.11, preprint) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://doi.org/10.1101/2024.11.28.625345) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.11.28.625345) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)

  > Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.

- **ChaRNABERT** — [Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models](https://openreview.net/forum?id=cAiECLDjzF) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=cAiECLDjzF)

  > Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.

- **RiNALMo** — [RiNALMo: general-purpose RNA language models can generalize well on structure prediction tasks](https://www.nature.com/articles/s41467-025-60872-5) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-60872-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/lbcb-sci/RiNALMo)

  > Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.

- **RNA-BERTa** — [DLRNA-BERTa: A transformer approach for RNA-drug binding affinity prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) (2025.09, preprint) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/IlPakoZ/RNA-BERTa9700)

  > Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.

- **ProtRNA** — [ProtRNA: A protein-derived RNA language model by cross-modality transfer learning](https://www.sciencedirect.com/science/article/pii/S2405471225002042) (2025.09) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S2405471225002042) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/roxie-zhang/ProtRNA)

  > Adapts the protein language model ESM-2 to RNA through cross-modality transfer learning on 6M RNAcentral sequences, providing a parameter- and data-efficient RNA language model.

- **ERNIE-RNA** — [ERNIE-RNA: an RNA language model with structure-enhanced representations](https://www.nature.com/articles/s41467-025-64972-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-64972-0) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/ernierna-ss)

  > Develops ERNIE-RNA with base-pairing-aware attention bias for structure-enhanced pre-training on RNAcentral ncRNAs, improving structure and function prediction tasks.

- **BiRNA-BERT** — [BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization](https://www.nature.com/articles/s42003-025-08982-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s42003-025-08982-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/buetnlpbio/BiRNA-BERT)

  > Introduces BiRNA-BERT, a 117M-parameter encoder trained on 36M ncRNA sequences with adaptive dual tokenization combining nucleotide-level and BPE representations.

- **HydraRNA** — [HydraRNA: a hybrid architecture based full-length RNA language model](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/GuipengLi/HydraRNA)

  > Introduces HydraRNA, a full-length RNA language model using a hybrid bidirectional state space and attention architecture for both coding and non-coding RNA tasks.

- **RNAElectra** — [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://doi.org/10.64898/2026.03.15.711950) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://doi.org/10.64898/2026.03.15.711950) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.64898/2026.03.15.711950)

  > Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.

- **RNAret** — [Retentive Network promotes efficient RNA language modeling of long sequences](https://www.nature.com/articles/s42003-026-09757-x) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s42003-026-09757-x) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/DrBlackZJU/RNAret/)

  > Introduces RNAret, a Retentive Network-based RNA language model pre-trained with masked language modeling on 29.8M RNAcentral sequences, enabling efficient long-sequence RNA representation learning across interaction, structure, and classification tasks.

</details>

<details open>
<summary><b>mRNA / CDS Sequence Models (12)</b></summary>

- **GenSLM** — [GenSLMs: Genome-scale language models reveal SARS-CoV-2 evolutionary dynamics](https://doi.org/10.1177/10943420231201154) (2023.11) [![abs](https://img.shields.io/badge/abs-2023.11-b31b1b.svg)](https://doi.org/10.1177/10943420231201154)

  > Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.

- **CaLM** — [Codon language embeddings provide strong signals for use in protein engineering](https://www.nature.com/articles/s42256-024-00791-0) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00791-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oxpig/CaLM)

  > Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.

- **mRNA-FM** — [RNA-FM: The RNA Foundation Model](https://github.com/ml4bio/RNA-FM) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://github.com/ml4bio/RNA-FM) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ml4bio/RNA-FM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/mrnafm)

  > Adds mRNA-FM as the coding-sequence extension of RNA-FM, pre-trained on 45M mRNA CDS sequences to provide contextual embeddings for mRNA and protein-related downstream tasks.

- **CodonBERT** — [CodonBERT large language model for mRNA vaccines](https://doi.org/10.1101/gr.278870.123) (2024.08) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/gr.278870.123) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Sanofi-Public/CodonBERT)

  > Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization for mRNA sequence representation and vaccine-related design tasks.

- **HELM** — [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.12459) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2410.12459)

  > Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.

- **Helix-mRNA** — [Helix-mRNA: A Hybrid Foundation Model For Full Sequence mRNA Therapeutics](https://openreview.net/forum?id=Ky0CkFiVhu) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=Ky0CkFiVhu) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/helical-ai/helix-mRNA)

  > Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.

- **CodonFM** — [Introducing the CodonFM Open Model for RNA Design and Analysis](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) (2025.10) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NVIDIA-Digital-Bio/CodonFM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/nvidia/NV-CodonFM-Encodon-1B-v1)

  > Releases NVIDIA CodonFM / Encodon, a family of codon-level masked language models trained on 131M RefSeq protein-coding sequences for mRNA design, codon optimization, and synonymous or missense variant interpretation.

- **mRNABERT** — [mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset](https://www.nature.com/articles/s41467-025-65340-8) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65340-8) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)

  > Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.

- **mRNA-GPT** — [Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) (2025.12, preprint) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ZHymLumine/mRNA-GPT/)

  > Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.

- **codonGPT** — [codonGPT: reinforcement learning on a generative language model enables scalable mRNA design](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) (2025.12) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NanilTx/codonGPT_pub) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/naniltx/codonGPT)

  > Introduces codonGPT, a GPT-style generative language model trained exclusively on 338,417 coding mRNA sequences with codon-level tokenization, and demonstrates reinforcement learning for constrained mRNA sequence optimization.

- **NUWA** — [Large mRNA language foundation modeling with NUWA for unified sequence perception and generation](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) (2026.02, preprint) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/zysxmu/NUWA)

  > Proposes NUWA, a large mRNA foundation model pre-trained on 115M multi-species coding sequences for unified mRNA sequence perception and generation.

- **RIBOSPAN** — [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](https://arxiv.org/abs/2608.22849v2) (2026.08, preprint) [![abs](https://img.shields.io/badge/abs-2026.08-b31b1b.svg)](https://arxiv.org/abs/2608.22849v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2608.22849v2)

  > Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution.

</details>

<details open>
<summary><b>UTR Sequence Models (3)</b></summary>

- **UTR-LM** — [A 5′ UTR language model for decoding untranslated regions of mRNA and function predictions](https://www.nature.com/articles/s42256-024-00823-9) (2024.04) [![abs](https://img.shields.io/badge/abs-2024.04-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00823-9) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/utrlm-te_el)

  > Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.

- **3UTRBERT** — [Deciphering 3'UTR Mediated Gene Regulation Using Interpretable Deep Representation Learning](https://doi.org/10.1002/advs.202407013) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1002/advs.202407013) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yangyn533/3UTRBERT)

  > Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.

- **miRBind2** — [miRBind2 enables sequence-only prediction of miRNA binding and transcript repression](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1)

  > MotivationMicroRNAs (miRNAs) regulate gene expression by guiding Argonaute proteins to partially complementary sites on target RNAs.

</details>

<details open>
<summary><b>Specific RNA Type Models (6)</b></summary>

- **SpliceBERT** — [Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction](https://doi.org/10.1093/bib/bbae163) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://doi.org/10.1093/bib/bbae163) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/chenkenbio/SpliceBERT)

  > Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.

- **RFamLlama** — [RFamLlama: an efficient conditional language model for RNA sequence generation across diverse structural families](https://openreview.net/forum?id=dXnQedxEJD) (2024.06, workshop) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://openreview.net/forum?id=dXnQedxEJD) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/jinyuan22/RFamLlama-base)

  > Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.

- **PlantRNA-FM** — [An interpretable RNA foundation model for exploring functional RNA motifs in plants](https://www.nature.com/articles/s42256-024-00946-z) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00946-z) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/PlantRNA-FM)

  > Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.

- **LncRNA-BERT** — [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/luukromeijn/lncRNA-Py)

  > Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.

- **G4mer** — [G4mer: An RNA language model for transcriptome-wide identification of G-quadruplexes and disease variants from population-scale genetic data](https://www.nature.com/articles/s41467-025-65020-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65020-7) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Biociphers/g4mer)

  > Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.

- **Orthrus** — [Orthrus: toward evolutionary and functional RNA foundation models](https://www.nature.com/articles/s41592-026-03064-3) (2026.04) [![abs](https://img.shields.io/badge/abs-2026.04-b31b1b.svg)](https://www.nature.com/articles/s41592-026-03064-3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/quietflamingo/orthrus-large-4-track)

  > Introduces Orthrus, a Mamba-based mature RNA foundation model using contrastive learning on transcript isoforms and cross-species orthologs to learn evolutionary and functional RNA representations.

</details>

<details open>
<summary><b>Structure-aware RNA Models (4)</b></summary>

- **ATOM-1** — [ATOM-1: A Foundation Model for RNA Structure and Function Built on Chemical Mapping Data](https://doi.org/10.1101/2023.12.13.571579) (2023.12, preprint) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1101/2023.12.13.571579) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2023.12.13.571579)

  > Proposes ATOM-1, a foundation model trained on chemical mapping data to learn RNA structure-aware representations for secondary and tertiary structure probing and RNA function prediction.

- **MP-RNA** — [MP-RNA: Unleashing Multi-species RNA Foundation Model via Calibrated Secondary Structure Prediction](https://aclanthology.org/2024.findings-emnlp.304/) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://aclanthology.org/2024.findings-emnlp.304/) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/MP-RNA)

  > Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.

- **OmniGenome** — [Bridging Sequence-Structure Alignment in RNA Foundation Models](https://ojs.aaai.org/index.php/AAAI/article/view/35500) (2025.04) [![abs](https://img.shields.io/badge/abs-2025.04-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/35500) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/OmniGenome-186M)

  > Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.

- **StructRFM** — [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) (2025.08, preprint) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/heqin-zhu/structRFM)

  > Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.

</details>

<details open>
<summary><b>RNA Generative Models (3)</b></summary>

- **GenerRNA** — [GenerRNA: A generative pre-trained language model for de novo RNA design](https://doi.org/10.1371/journal.pone.0310814) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1371/journal.pone.0310814) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/pfnet/GenerRNA)

  > Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.

- **RNAGenesis** — [RNAGenesis: A Generalist Foundation Model for Functional RNA Therapeutics](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) (2024.12, preprint) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Zaixi/RNAGenesis)

  > Proposes RNAGenesis, a 1B-parameter generative RNA model that integrates sequence representation, structure prediction, and de novo functional design, listed here as an adapted / derived RNA design model rather than a core ncRNA pre-training-only FM.

- **EVA** — [A Long-Context Generative Foundation Model Deciphers RNA Design Principles](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)

  > Introduces EVA, a Mixture-of-Experts decoder model for long-context RNA sequence generation, trained on 114M+ full-length RNA sequences for generating diverse functional RNA molecules at unprecedented lengths.

</details>

<details open>
<summary><b>General / Other RNA Models (3)</b></summary>

- **Uni-RNA** — [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) (2023.07, preprint) [![abs](https://img.shields.io/badge/abs-2023.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ComDec/unirna_tf)

  > Presents Uni-RNA, a 400M-parameter universal RNA model pre-trained on 1B sequences from RNAcentral, MG-RAST, and MGnify, covering RNA across diverse species for general-purpose RNA representation learning.

- **LoRNA SH** — [A long-context RNA foundation model for predicting transcriptome architecture](https://doi.org/10.1101/2024.08.26.609813) (2024.08, preprint) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/2024.08.26.609813) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.08.26.609813)

  > Introduces LoRNA SH, a StripedHyena-based long-context RNA foundation model trained on full-length transcriptome architecture data to predict isoform abundance, isoform structure, and variant effects.

- **RNALens** — [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) (2025.07, preprint) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oomics/RNALens)

  > Introduces RNALens, a 469M-parameter multi-task RNA foundation model pre-trained on multispecies genomic and 5'UTR sequences using BPE tokenization, supporting diverse RNA analysis tasks within a unified framework.

</details>

<details open>
<summary><b>Broad RNA-Inclusive Nucleotide / Multi-modal Models (5)</b></summary>

- **METAGENE-1** — [METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring](https://arxiv.org/abs/2501.02045) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2501.02045) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2501.02045) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/metagene-ai/METAGENE-1)

  > Introduces METAGENE-1, a 7B autoregressive metagenomic foundation model pre-trained on diverse metagenomic DNA and RNA sequences, supporting genomic sequence embeddings, pathogen detection, biosurveillance, and pandemic monitoring tasks.

- **Life-Code** — [Life-Code: Central Dogma Modeling with Multi-Omics Sequence Unification](https://arxiv.org/abs/2502.07299) (2025.02, preprint) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.07299) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2502.07299)

  > Introduces Life-Code, a central-dogma sequence foundation framework that unifies DNA, RNA/cDNA, amino-acid, and multi-omics information into nucleotide-based sequences with codon tokenization and masked modeling over coding and non-coding regions.

- **LucaOne** — [Generalized biological foundation model with unified nucleic acid and protein language](https://www.nature.com/articles/s42256-025-01044-4) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s42256-025-01044-4) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/LucaOne/LucaOneApp) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LucaGroup/LucaOne-default-step36M)

  > Introduces LucaOne, a unified biological foundation model trained on nucleic acid (DNA and RNA) and protein sequences from 169,861 species, supporting reusable embeddings and downstream tasks involving DNA, RNA, proteins, and their interrelated pairs.

- **Evo 2** — [Genome Modeling and Design Across All Domains of Life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s41586-026-10176-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ArcInstitute/evo2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/arcinstitute/evo2_40b)

  > Introduces Evo 2, an open biological sequence foundation model trained on OpenGenome2 across all domains of life; the released OpenGenome2 composition includes eukaryotic mRNAs and ncRNA sources such as RNAcentral and Rfam, enabling broad nucleotide-sequence prediction and generation.

- **OmniNA** — [A foundation model for nucleotide sequences](https://academic.oup.com/nar/article/54/6/gkag083/8528802) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://academic.oup.com/nar/article/54/6/gkag083/8528802) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/xilinshen/OmniNA) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/XLS/OmniNA-1.7B)

  > Introduces OmniNA, an annotation-aware generative foundation model for nucleic acid sequences trained on NCBI NT nucleotide sequences and annotations spanning genomic DNA and RNA, with reusable representations for genomics and transcriptomics tasks.

</details>

</blockquote>

</details>

<details>
<summary><b>View 3: Classified by Architecture</b></summary>

<blockquote>

<details open>
<summary><b>Encoder-only (BERT-family) (32)</b></summary>

- **RNABert** — [Informative RNA base embedding for RNA structural alignment and clustering by deep representation learning](https://doi.org/10.1093/nargab/lqac012) (2022.01) [![abs](https://img.shields.io/badge/abs-2022.01-b31b1b.svg)](https://doi.org/10.1093/nargab/lqac012) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/mana438/RNABERT)

  > Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.

- **RNAFM** — [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) (2022.04, preprint) [![abs](https://img.shields.io/badge/abs-2022.04-b31b1b.svg)](https://arxiv.org/abs/2204.00300) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2204.00300) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/rnafm)

  > Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.

- **Uni-RNA** — [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) (2023.07, preprint) [![abs](https://img.shields.io/badge/abs-2023.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ComDec/unirna_tf)

  > Presents Uni-RNA, a 400M-parameter universal RNA model pre-trained on 1B sequences from RNAcentral, MG-RAST, and MGnify, covering RNA across diverse species for general-purpose RNA representation learning.

- **RNAMSM** — [Multiple sequence alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) (2024.01) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1093/nar/gkad1031) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yikunpku/RNA-MSM)

  > Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.

- **RNA-km** — [Language models enable zero-shot prediction of RNA secondary structures including pseudoknots](https://doi.org/10.1101/2024.01.27.577533) (2024.01, preprint) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1101/2024.01.27.577533) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.01.27.577533) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/gongtiansu/RNA-km)

  > Proposes RNA-km, a self-supervised RNA language model trained on 23M ncRNA sequences with k-mer masking and relative positional encoding, enabling zero-shot RNA secondary structure prediction including pseudoknots.

- **CaLM** — [Codon language embeddings provide strong signals for use in protein engineering](https://www.nature.com/articles/s42256-024-00791-0) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00791-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oxpig/CaLM)

  > Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.

- **mRNA-FM** — [RNA-FM: The RNA Foundation Model](https://github.com/ml4bio/RNA-FM) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://github.com/ml4bio/RNA-FM) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ml4bio/RNA-FM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/mrnafm)

  > Adds mRNA-FM as the coding-sequence extension of RNA-FM, pre-trained on 45M mRNA CDS sequences to provide contextual embeddings for mRNA and protein-related downstream tasks.

- **SpliceBERT** — [Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction](https://doi.org/10.1093/bib/bbae163) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://doi.org/10.1093/bib/bbae163) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/chenkenbio/SpliceBERT)

  > Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.

- **UTR-LM** — [A 5′ UTR language model for decoding untranslated regions of mRNA and function predictions](https://www.nature.com/articles/s42256-024-00823-9) (2024.04) [![abs](https://img.shields.io/badge/abs-2024.04-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00823-9) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/utrlm-te_el)

  > Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.

- **RNAErnie** — [Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning](https://www.nature.com/articles/s42256-024-00836-4) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00836-4) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LLM-EDA/RNAErnie)

  > Presents RNAErnie, an RNA-focused pre-trained model that combines motif-aware pretraining with type-guided fine-tuning for diverse RNA sequence analysis tasks.

- **CodonBERT** — [CodonBERT large language model for mRNA vaccines](https://doi.org/10.1101/gr.278870.123) (2024.08) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/gr.278870.123) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Sanofi-Public/CodonBERT)

  > Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization for mRNA sequence representation and vaccine-related design tasks.

- **3UTRBERT** — [Deciphering 3'UTR Mediated Gene Regulation Using Interpretable Deep Representation Learning](https://doi.org/10.1002/advs.202407013) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1002/advs.202407013) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yangyn533/3UTRBERT)

  > Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.

- **AIDO.RNA** — [A Large-Scale Foundation Model for RNA Function and Structure Prediction](https://doi.org/10.1101/2024.11.28.625345) (2024.11, preprint) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://doi.org/10.1101/2024.11.28.625345) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.11.28.625345) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)

  > Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.

- **MP-RNA** — [MP-RNA: Unleashing Multi-species RNA Foundation Model via Calibrated Secondary Structure Prediction](https://aclanthology.org/2024.findings-emnlp.304/) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://aclanthology.org/2024.findings-emnlp.304/) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/MP-RNA)

  > Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.

- **PlantRNA-FM** — [An interpretable RNA foundation model for exploring functional RNA motifs in plants](https://www.nature.com/articles/s42256-024-00946-z) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00946-z) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/PlantRNA-FM)

  > Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.

- **LncRNA-BERT** — [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/luukromeijn/lncRNA-Py)

  > Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.

- **ChaRNABERT** — [Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models](https://openreview.net/forum?id=cAiECLDjzF) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=cAiECLDjzF)

  > Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.

- **OmniGenome** — [Bridging Sequence-Structure Alignment in RNA Foundation Models](https://ojs.aaai.org/index.php/AAAI/article/view/35500) (2025.04) [![abs](https://img.shields.io/badge/abs-2025.04-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/35500) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/OmniGenome-186M)

  > Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.

- **LucaOne** — [Generalized biological foundation model with unified nucleic acid and protein language](https://www.nature.com/articles/s42256-025-01044-4) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s42256-025-01044-4) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/LucaOne/LucaOneApp) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LucaGroup/LucaOne-default-step36M)

  > Introduces LucaOne, a unified biological foundation model trained on nucleic acid (DNA and RNA) and protein sequences from 169,861 species, supporting reusable embeddings and downstream tasks involving DNA, RNA, proteins, and their interrelated pairs.

- **RiNALMo** — [RiNALMo: general-purpose RNA language models can generalize well on structure prediction tasks](https://www.nature.com/articles/s41467-025-60872-5) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-60872-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/lbcb-sci/RiNALMo)

  > Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.

- **RNALens** — [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) (2025.07, preprint) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oomics/RNALens)

  > Introduces RNALens, a 469M-parameter multi-task RNA foundation model pre-trained on multispecies genomic and 5'UTR sequences using BPE tokenization, supporting diverse RNA analysis tasks within a unified framework.

- **StructRFM** — [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) (2025.08, preprint) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/heqin-zhu/structRFM)

  > Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.

- **RNA-BERTa** — [DLRNA-BERTa: A transformer approach for RNA-drug binding affinity prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) (2025.09, preprint) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/IlPakoZ/RNA-BERTa9700)

  > Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.

- **ProtRNA** — [ProtRNA: A protein-derived RNA language model by cross-modality transfer learning](https://www.sciencedirect.com/science/article/pii/S2405471225002042) (2025.09) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S2405471225002042) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/roxie-zhang/ProtRNA)

  > Adapts the protein language model ESM-2 to RNA through cross-modality transfer learning on 6M RNAcentral sequences, providing a parameter- and data-efficient RNA language model.

- **CodonFM** — [Introducing the CodonFM Open Model for RNA Design and Analysis](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) (2025.10) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NVIDIA-Digital-Bio/CodonFM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/nvidia/NV-CodonFM-Encodon-1B-v1)

  > Releases NVIDIA CodonFM / Encodon, a family of codon-level masked language models trained on 131M RefSeq protein-coding sequences for mRNA design, codon optimization, and synonymous or missense variant interpretation.

- **ERNIE-RNA** — [ERNIE-RNA: an RNA language model with structure-enhanced representations](https://www.nature.com/articles/s41467-025-64972-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-64972-0) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/ernierna-ss)

  > Develops ERNIE-RNA with base-pairing-aware attention bias for structure-enhanced pre-training on RNAcentral ncRNAs, improving structure and function prediction tasks.

- **BiRNA-BERT** — [BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization](https://www.nature.com/articles/s42003-025-08982-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s42003-025-08982-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/buetnlpbio/BiRNA-BERT)

  > Introduces BiRNA-BERT, a 117M-parameter encoder trained on 36M ncRNA sequences with adaptive dual tokenization combining nucleotide-level and BPE representations.

- **mRNABERT** — [mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset](https://www.nature.com/articles/s41467-025-65340-8) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65340-8) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)

  > Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.

- **G4mer** — [G4mer: An RNA language model for transcriptome-wide identification of G-quadruplexes and disease variants from population-scale genetic data](https://www.nature.com/articles/s41467-025-65020-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65020-7) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Biociphers/g4mer)

  > Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.

- **NUWA** — [Large mRNA language foundation modeling with NUWA for unified sequence perception and generation](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) (2026.02, preprint) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/zysxmu/NUWA)

  > Proposes NUWA, a large mRNA foundation model pre-trained on 115M multi-species coding sequences for unified mRNA sequence perception and generation.

- **RNAElectra** — [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://doi.org/10.64898/2026.03.15.711950) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://doi.org/10.64898/2026.03.15.711950) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.64898/2026.03.15.711950)

  > Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.

- **miRBind2** — [miRBind2 enables sequence-only prediction of miRNA binding and transcript repression](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1)

  > MotivationMicroRNAs (miRNAs) regulate gene expression by guiding Argonaute proteins to partially complementary sites on target RNAs.

</details>

<details open>
<summary><b>Decoder-only (GPT-family) (7)</b></summary>

- **GenSLM** — [GenSLMs: Genome-scale language models reveal SARS-CoV-2 evolutionary dynamics](https://doi.org/10.1177/10943420231201154) (2023.11) [![abs](https://img.shields.io/badge/abs-2023.11-b31b1b.svg)](https://doi.org/10.1177/10943420231201154)

  > Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.

- **RFamLlama** — [RFamLlama: an efficient conditional language model for RNA sequence generation across diverse structural families](https://openreview.net/forum?id=dXnQedxEJD) (2024.06, workshop) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://openreview.net/forum?id=dXnQedxEJD) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/jinyuan22/RFamLlama-base)

  > Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.

- **GenerRNA** — [GenerRNA: A generative pre-trained language model for de novo RNA design](https://doi.org/10.1371/journal.pone.0310814) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1371/journal.pone.0310814) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/pfnet/GenerRNA)

  > Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.

- **METAGENE-1** — [METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring](https://arxiv.org/abs/2501.02045) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2501.02045) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2501.02045) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/metagene-ai/METAGENE-1)

  > Introduces METAGENE-1, a 7B autoregressive metagenomic foundation model pre-trained on diverse metagenomic DNA and RNA sequences, supporting genomic sequence embeddings, pathogen detection, biosurveillance, and pandemic monitoring tasks.

- **mRNA-GPT** — [Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) (2025.12, preprint) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ZHymLumine/mRNA-GPT/)

  > Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.

- **codonGPT** — [codonGPT: reinforcement learning on a generative language model enables scalable mRNA design](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) (2025.12) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NanilTx/codonGPT_pub) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/naniltx/codonGPT)

  > Introduces codonGPT, a GPT-style generative language model trained exclusively on 338,417 coding mRNA sequences with codon-level tokenization, and demonstrates reinforcement learning for constrained mRNA sequence optimization.

- **OmniNA** — [A foundation model for nucleotide sequences](https://academic.oup.com/nar/article/54/6/gkag083/8528802) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://academic.oup.com/nar/article/54/6/gkag083/8528802) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/xilinshen/OmniNA) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/XLS/OmniNA-1.7B)

  > Introduces OmniNA, an annotation-aware generative foundation model for nucleic acid sequences trained on NCBI NT nucleotide sequences and annotations spanning genomic DNA and RNA, with reusable representations for genomics and transcriptomics tasks.

</details>

<details open>
<summary><b>Encoder-Decoder (Seq2Seq) (2)</b></summary>

- **ATOM-1** — [ATOM-1: A Foundation Model for RNA Structure and Function Built on Chemical Mapping Data](https://doi.org/10.1101/2023.12.13.571579) (2023.12, preprint) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1101/2023.12.13.571579) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2023.12.13.571579)

  > Proposes ATOM-1, a foundation model trained on chemical mapping data to learn RNA structure-aware representations for secondary and tertiary structure probing and RNA function prediction.

- **HELM** — [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.12459) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2410.12459)

  > Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.

</details>

<details open>
<summary><b>Hybrid / SSM (Mamba, StripedHyena) (8)</b></summary>

- **LoRNA SH** — [A long-context RNA foundation model for predicting transcriptome architecture](https://doi.org/10.1101/2024.08.26.609813) (2024.08, preprint) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/2024.08.26.609813) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.08.26.609813)

  > Introduces LoRNA SH, a StripedHyena-based long-context RNA foundation model trained on full-length transcriptome architecture data to predict isoform abundance, isoform structure, and variant effects.

- **DGRNA** — [DGRNA: a long-context RNA foundation model with bidirectional attention Mamba2](https://doi.org/10.1101/2024.10.31.621427) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.10.31.621427) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.10.31.621427)

  > Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.

- **Life-Code** — [Life-Code: Central Dogma Modeling with Multi-Omics Sequence Unification](https://arxiv.org/abs/2502.07299) (2025.02, preprint) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.07299) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2502.07299)

  > Introduces Life-Code, a central-dogma sequence foundation framework that unifies DNA, RNA/cDNA, amino-acid, and multi-omics information into nucleotide-based sequences with codon tokenization and masked modeling over coding and non-coding regions.

- **Helix-mRNA** — [Helix-mRNA: A Hybrid Foundation Model For Full Sequence mRNA Therapeutics](https://openreview.net/forum?id=Ky0CkFiVhu) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=Ky0CkFiVhu) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/helical-ai/helix-mRNA)

  > Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.

- **HydraRNA** — [HydraRNA: a hybrid architecture based full-length RNA language model](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/GuipengLi/HydraRNA)

  > Introduces HydraRNA, a full-length RNA language model using a hybrid bidirectional state space and attention architecture for both coding and non-coding RNA tasks.

- **RNAret** — [Retentive Network promotes efficient RNA language modeling of long sequences](https://www.nature.com/articles/s42003-026-09757-x) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s42003-026-09757-x) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/DrBlackZJU/RNAret/)

  > Introduces RNAret, a Retentive Network-based RNA language model pre-trained with masked language modeling on 29.8M RNAcentral sequences, enabling efficient long-sequence RNA representation learning across interaction, structure, and classification tasks.

- **Evo 2** — [Genome Modeling and Design Across All Domains of Life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s41586-026-10176-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ArcInstitute/evo2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/arcinstitute/evo2_40b)

  > Introduces Evo 2, an open biological sequence foundation model trained on OpenGenome2 across all domains of life; the released OpenGenome2 composition includes eukaryotic mRNAs and ncRNA sources such as RNAcentral and Rfam, enabling broad nucleotide-sequence prediction and generation.

- **Orthrus** — [Orthrus: toward evolutionary and functional RNA foundation models](https://www.nature.com/articles/s41592-026-03064-3) (2026.04) [![abs](https://img.shields.io/badge/abs-2026.04-b31b1b.svg)](https://www.nature.com/articles/s41592-026-03064-3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/quietflamingo/orthrus-large-4-track)

  > Introduces Orthrus, a Mamba-based mature RNA foundation model using contrastive learning on transcript isoforms and cross-species orthologs to learn evolutionary and functional RNA representations.

</details>

<details open>
<summary><b>Specialized (Diffusion, MoE, GNN, Multimodal) (3)</b></summary>

- **RNAGenesis** — [RNAGenesis: A Generalist Foundation Model for Functional RNA Therapeutics](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) (2024.12, preprint) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Zaixi/RNAGenesis)

  > Proposes RNAGenesis, a 1B-parameter generative RNA model that integrates sequence representation, structure prediction, and de novo functional design, listed here as an adapted / derived RNA design model rather than a core ncRNA pre-training-only FM.

- **EVA** — [A Long-Context Generative Foundation Model Deciphers RNA Design Principles](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)

  > Introduces EVA, a Mixture-of-Experts decoder model for long-context RNA sequence generation, trained on 114M+ full-length RNA sequences for generating diverse functional RNA molecules at unprecedented lengths.

- **RIBOSPAN** — [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](https://arxiv.org/abs/2608.22849v2) (2026.08, preprint) [![abs](https://img.shields.io/badge/abs-2026.08-b31b1b.svg)](https://arxiv.org/abs/2608.22849v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2608.22849v2)

  > Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution.

</details>

</blockquote>

</details>

<details>
<summary><b>View 4: Classified by Tokenization Strategy</b></summary>

<blockquote>

<details open>
<summary><b>Single Nucleotide Token (SNT) (29)</b></summary>

- **RNABert** — [Informative RNA base embedding for RNA structural alignment and clustering by deep representation learning](https://doi.org/10.1093/nargab/lqac012) (2022.01) [![abs](https://img.shields.io/badge/abs-2022.01-b31b1b.svg)](https://doi.org/10.1093/nargab/lqac012) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/mana438/RNABERT)

  > Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.

- **RNAFM** — [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) (2022.04, preprint) [![abs](https://img.shields.io/badge/abs-2022.04-b31b1b.svg)](https://arxiv.org/abs/2204.00300) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2204.00300) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/rnafm)

  > Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.

- **Uni-RNA** — [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) (2023.07, preprint) [![abs](https://img.shields.io/badge/abs-2023.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ComDec/unirna_tf)

  > Presents Uni-RNA, a 400M-parameter universal RNA model pre-trained on 1B sequences from RNAcentral, MG-RAST, and MGnify, covering RNA across diverse species for general-purpose RNA representation learning.

- **ATOM-1** — [ATOM-1: A Foundation Model for RNA Structure and Function Built on Chemical Mapping Data](https://doi.org/10.1101/2023.12.13.571579) (2023.12, preprint) [![abs](https://img.shields.io/badge/abs-2023.12-b31b1b.svg)](https://doi.org/10.1101/2023.12.13.571579) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2023.12.13.571579)

  > Proposes ATOM-1, a foundation model trained on chemical mapping data to learn RNA structure-aware representations for secondary and tertiary structure probing and RNA function prediction.

- **RNAMSM** — [Multiple sequence alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) (2024.01) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1093/nar/gkad1031) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yikunpku/RNA-MSM)

  > Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.

- **RNA-km** — [Language models enable zero-shot prediction of RNA secondary structures including pseudoknots](https://doi.org/10.1101/2024.01.27.577533) (2024.01, preprint) [![abs](https://img.shields.io/badge/abs-2024.01-b31b1b.svg)](https://doi.org/10.1101/2024.01.27.577533) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.01.27.577533) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/gongtiansu/RNA-km)

  > Proposes RNA-km, a self-supervised RNA language model trained on 23M ncRNA sequences with k-mer masking and relative positional encoding, enabling zero-shot RNA secondary structure prediction including pseudoknots.

- **mRNA-FM** — [RNA-FM: The RNA Foundation Model](https://github.com/ml4bio/RNA-FM) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://github.com/ml4bio/RNA-FM) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ml4bio/RNA-FM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/mrnafm)

  > Adds mRNA-FM as the coding-sequence extension of RNA-FM, pre-trained on 45M mRNA CDS sequences to provide contextual embeddings for mRNA and protein-related downstream tasks.

- **SpliceBERT** — [Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction](https://doi.org/10.1093/bib/bbae163) (2024.03) [![abs](https://img.shields.io/badge/abs-2024.03-b31b1b.svg)](https://doi.org/10.1093/bib/bbae163) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/chenkenbio/SpliceBERT)

  > Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.

- **UTR-LM** — [A 5′ UTR language model for decoding untranslated regions of mRNA and function predictions](https://www.nature.com/articles/s42256-024-00823-9) (2024.04) [![abs](https://img.shields.io/badge/abs-2024.04-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00823-9) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/utrlm-te_el)

  > Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.

- **RNAErnie** — [Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning](https://www.nature.com/articles/s42256-024-00836-4) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00836-4) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LLM-EDA/RNAErnie)

  > Presents RNAErnie, an RNA-focused pre-trained model that combines motif-aware pretraining with type-guided fine-tuning for diverse RNA sequence analysis tasks.

- **RFamLlama** — [RFamLlama: an efficient conditional language model for RNA sequence generation across diverse structural families](https://openreview.net/forum?id=dXnQedxEJD) (2024.06, workshop) [![abs](https://img.shields.io/badge/abs-2024.06-b31b1b.svg)](https://openreview.net/forum?id=dXnQedxEJD) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/jinyuan22/RFamLlama-base)

  > Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.

- **LoRNA SH** — [A long-context RNA foundation model for predicting transcriptome architecture](https://doi.org/10.1101/2024.08.26.609813) (2024.08, preprint) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/2024.08.26.609813) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.08.26.609813)

  > Introduces LoRNA SH, a StripedHyena-based long-context RNA foundation model trained on full-length transcriptome architecture data to predict isoform abundance, isoform structure, and variant effects.

- **DGRNA** — [DGRNA: a long-context RNA foundation model with bidirectional attention Mamba2](https://doi.org/10.1101/2024.10.31.621427) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1101/2024.10.31.621427) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.10.31.621427)

  > Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.

- **AIDO.RNA** — [A Large-Scale Foundation Model for RNA Function and Structure Prediction](https://doi.org/10.1101/2024.11.28.625345) (2024.11, preprint) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://doi.org/10.1101/2024.11.28.625345) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.1101/2024.11.28.625345) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)

  > Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.

- **MP-RNA** — [MP-RNA: Unleashing Multi-species RNA Foundation Model via Calibrated Secondary Structure Prediction](https://aclanthology.org/2024.findings-emnlp.304/) (2024.11) [![abs](https://img.shields.io/badge/abs-2024.11-b31b1b.svg)](https://aclanthology.org/2024.findings-emnlp.304/) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/MP-RNA)

  > Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.

- **RNAGenesis** — [RNAGenesis: A Generalist Foundation Model for Functional RNA Therapeutics](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) (2024.12, preprint) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Zaixi/RNAGenesis)

  > Proposes RNAGenesis, a 1B-parameter generative RNA model that integrates sequence representation, structure prediction, and de novo functional design, listed here as an adapted / derived RNA design model rather than a core ncRNA pre-training-only FM.

- **PlantRNA-FM** — [An interpretable RNA foundation model for exploring functional RNA motifs in plants](https://www.nature.com/articles/s42256-024-00946-z) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00946-z) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/PlantRNA-FM)

  > Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.

- **OmniGenome** — [Bridging Sequence-Structure Alignment in RNA Foundation Models](https://ojs.aaai.org/index.php/AAAI/article/view/35500) (2025.04) [![abs](https://img.shields.io/badge/abs-2025.04-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/35500) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/yangheng/OmniGenome-186M)

  > Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.

- **LucaOne** — [Generalized biological foundation model with unified nucleic acid and protein language](https://www.nature.com/articles/s42256-025-01044-4) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s42256-025-01044-4) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/LucaOne/LucaOneApp) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/LucaGroup/LucaOne-default-step36M)

  > Introduces LucaOne, a unified biological foundation model trained on nucleic acid (DNA and RNA) and protein sequences from 169,861 species, supporting reusable embeddings and downstream tasks involving DNA, RNA, proteins, and their interrelated pairs.

- **RiNALMo** — [RiNALMo: general-purpose RNA language models can generalize well on structure prediction tasks](https://www.nature.com/articles/s41467-025-60872-5) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-60872-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/lbcb-sci/RiNALMo)

  > Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.

- **StructRFM** — [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) (2025.08, preprint) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/heqin-zhu/structRFM)

  > Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.

- **ProtRNA** — [ProtRNA: A protein-derived RNA language model by cross-modality transfer learning](https://www.sciencedirect.com/science/article/pii/S2405471225002042) (2025.09) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S2405471225002042) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/roxie-zhang/ProtRNA)

  > Adapts the protein language model ESM-2 to RNA through cross-modality transfer learning on 6M RNAcentral sequences, providing a parameter- and data-efficient RNA language model.

- **ERNIE-RNA** — [ERNIE-RNA: an RNA language model with structure-enhanced representations](https://www.nature.com/articles/s41467-025-64972-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-64972-0) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/multimolecule/ernierna-ss)

  > Develops ERNIE-RNA with base-pairing-aware attention bias for structure-enhanced pre-training on RNAcentral ncRNAs, improving structure and function prediction tasks.

- **HydraRNA** — [HydraRNA: a hybrid architecture based full-length RNA language model](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/GuipengLi/HydraRNA)

  > Introduces HydraRNA, a full-length RNA language model using a hybrid bidirectional state space and attention architecture for both coding and non-coding RNA tasks.

- **G4mer** — [G4mer: An RNA language model for transcriptome-wide identification of G-quadruplexes and disease variants from population-scale genetic data](https://www.nature.com/articles/s41467-025-65020-7) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65020-7) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Biociphers/g4mer)

  > Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.

- **RNAElectra** — [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://doi.org/10.64898/2026.03.15.711950) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://doi.org/10.64898/2026.03.15.711950) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://doi.org/10.64898/2026.03.15.711950)

  > Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.

- **Evo 2** — [Genome Modeling and Design Across All Domains of Life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s41586-026-10176-5) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ArcInstitute/evo2) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/arcinstitute/evo2_40b)

  > Introduces Evo 2, an open biological sequence foundation model trained on OpenGenome2 across all domains of life; the released OpenGenome2 composition includes eukaryotic mRNAs and ncRNA sources such as RNAcentral and Rfam, enabling broad nucleotide-sequence prediction and generation.

- **miRBind2** — [miRBind2 enables sequence-only prediction of miRNA binding and transcript repression](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1)

  > MotivationMicroRNAs (miRNAs) regulate gene expression by guiding Argonaute proteins to partially complementary sites on target RNAs.

- **Orthrus** — [Orthrus: toward evolutionary and functional RNA foundation models](https://www.nature.com/articles/s41592-026-03064-3) (2026.04) [![abs](https://img.shields.io/badge/abs-2026.04-b31b1b.svg)](https://www.nature.com/articles/s41592-026-03064-3) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/quietflamingo/orthrus-large-4-track)

  > Introduces Orthrus, a Mamba-based mature RNA foundation model using contrastive learning on transcript isoforms and cross-species orthologs to learn evolutionary and functional RNA representations.

</details>

<details open>
<summary><b>Codon-level Tokenization (11)</b></summary>

- **GenSLM** — [GenSLMs: Genome-scale language models reveal SARS-CoV-2 evolutionary dynamics](https://doi.org/10.1177/10943420231201154) (2023.11) [![abs](https://img.shields.io/badge/abs-2023.11-b31b1b.svg)](https://doi.org/10.1177/10943420231201154)

  > Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.

- **CaLM** — [Codon language embeddings provide strong signals for use in protein engineering](https://www.nature.com/articles/s42256-024-00791-0) (2024.02) [![abs](https://img.shields.io/badge/abs-2024.02-b31b1b.svg)](https://www.nature.com/articles/s42256-024-00791-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oxpig/CaLM)

  > Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.

- **CodonBERT** — [CodonBERT large language model for mRNA vaccines](https://doi.org/10.1101/gr.278870.123) (2024.08) [![abs](https://img.shields.io/badge/abs-2024.08-b31b1b.svg)](https://doi.org/10.1101/gr.278870.123) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Sanofi-Public/CodonBERT)

  > Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization for mRNA sequence representation and vaccine-related design tasks.

- **HELM** — [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) (2024.10, preprint) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://arxiv.org/abs/2410.12459) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2410.12459)

  > Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.

- **Life-Code** — [Life-Code: Central Dogma Modeling with Multi-Omics Sequence Unification](https://arxiv.org/abs/2502.07299) (2025.02, preprint) [![abs](https://img.shields.io/badge/abs-2025.02-b31b1b.svg)](https://arxiv.org/abs/2502.07299) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2502.07299)

  > Introduces Life-Code, a central-dogma sequence foundation framework that unifies DNA, RNA/cDNA, amino-acid, and multi-omics information into nucleotide-based sequences with codon tokenization and masked modeling over coding and non-coding regions.

- **Helix-mRNA** — [Helix-mRNA: A Hybrid Foundation Model For Full Sequence mRNA Therapeutics](https://openreview.net/forum?id=Ky0CkFiVhu) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=Ky0CkFiVhu) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/helical-ai/helix-mRNA)

  > Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.

- **CodonFM** — [Introducing the CodonFM Open Model for RNA Design and Analysis](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) (2025.10) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NVIDIA-Digital-Bio/CodonFM) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/nvidia/NV-CodonFM-Encodon-1B-v1)

  > Releases NVIDIA CodonFM / Encodon, a family of codon-level masked language models trained on 131M RefSeq protein-coding sequences for mRNA design, codon optimization, and synonymous or missense variant interpretation.

- **mRNA-GPT** — [Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) (2025.12, preprint) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/ZHymLumine/mRNA-GPT/)

  > Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.

- **codonGPT** — [codonGPT: reinforcement learning on a generative language model enables scalable mRNA design](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) (2025.12) [![abs](https://img.shields.io/badge/abs-2025.12-b31b1b.svg)](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/NanilTx/codonGPT_pub) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/naniltx/codonGPT)

  > Introduces codonGPT, a GPT-style generative language model trained exclusively on 338,417 coding mRNA sequences with codon-level tokenization, and demonstrates reinforcement learning for constrained mRNA sequence optimization.

- **NUWA** — [Large mRNA language foundation modeling with NUWA for unified sequence perception and generation](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) (2026.02, preprint) [![abs](https://img.shields.io/badge/abs-2026.02-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/zysxmu/NUWA)

  > Proposes NUWA, a large mRNA foundation model pre-trained on 115M multi-species coding sequences for unified mRNA sequence perception and generation.

- **RIBOSPAN** — [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](https://arxiv.org/abs/2608.22849v2) (2026.08, preprint) [![abs](https://img.shields.io/badge/abs-2026.08-b31b1b.svg)](https://arxiv.org/abs/2608.22849v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2608.22849v2)

  > Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution.

</details>

<details open>
<summary><b>K-mer Tokenization (3)</b></summary>

- **3UTRBERT** — [Deciphering 3'UTR Mediated Gene Regulation Using Interpretable Deep Representation Learning](https://doi.org/10.1002/advs.202407013) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1002/advs.202407013) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/yangyn533/3UTRBERT)

  > Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.

- **LncRNA-BERT** — [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/luukromeijn/lncRNA-Py)

  > Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.

- **RNAret** — [Retentive Network promotes efficient RNA language modeling of long sequences](https://www.nature.com/articles/s42003-026-09757-x) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.nature.com/articles/s42003-026-09757-x) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/DrBlackZJU/RNAret/)

  > Introduces RNAret, a Retentive Network-based RNA language model pre-trained with masked language modeling on 29.8M RNAcentral sequences, enabling efficient long-sequence RNA representation learning across interaction, structure, and classification tasks.

</details>

<details open>
<summary><b>Byte Pair Encoding (BPE) (6)</b></summary>

- **GenerRNA** — [GenerRNA: A generative pre-trained language model for de novo RNA design](https://doi.org/10.1371/journal.pone.0310814) (2024.10) [![abs](https://img.shields.io/badge/abs-2024.10-b31b1b.svg)](https://doi.org/10.1371/journal.pone.0310814) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/pfnet/GenerRNA)

  > Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.

- **METAGENE-1** — [METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring](https://arxiv.org/abs/2501.02045) (2025.01, preprint) [![abs](https://img.shields.io/badge/abs-2025.01-b31b1b.svg)](https://arxiv.org/abs/2501.02045) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2501.02045) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/metagene-ai/METAGENE-1)

  > Introduces METAGENE-1, a 7B autoregressive metagenomic foundation model pre-trained on diverse metagenomic DNA and RNA sequences, supporting genomic sequence embeddings, pathogen detection, biosurveillance, and pandemic monitoring tasks.

- **RNALens** — [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) (2025.07, preprint) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/oomics/RNALens)

  > Introduces RNALens, a 469M-parameter multi-task RNA foundation model pre-trained on multispecies genomic and 5'UTR sequences using BPE tokenization, supporting diverse RNA analysis tasks within a unified framework.

- **RNA-BERTa** — [DLRNA-BERTa: A transformer approach for RNA-drug binding affinity prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) (2025.09, preprint) [![abs](https://img.shields.io/badge/abs-2025.09-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/IlPakoZ/RNA-BERTa9700)

  > Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.

- **EVA** — [A Long-Context Generative Foundation Model Deciphers RNA Design Principles](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) (2026.03, preprint) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)

  > Introduces EVA, a Mixture-of-Experts decoder model for long-context RNA sequence generation, trained on 114M+ full-length RNA sequences for generating diverse functional RNA molecules at unprecedented lengths.

- **OmniNA** — [A foundation model for nucleotide sequences](https://academic.oup.com/nar/article/54/6/gkag083/8528802) (2026.03) [![abs](https://img.shields.io/badge/abs-2026.03-b31b1b.svg)](https://academic.oup.com/nar/article/54/6/gkag083/8528802) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/xilinshen/OmniNA) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/XLS/OmniNA-1.7B)

  > Introduces OmniNA, an annotation-aware generative foundation model for nucleic acid sequences trained on NCBI NT nucleotide sequences and annotations spanning genomic DNA and RNA, with reusable representations for genomics and transcriptomics tasks.

</details>

<details open>
<summary><b>Learnable / Adaptive Tokenization (3)</b></summary>

- **ChaRNABERT** — [Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models](https://openreview.net/forum?id=cAiECLDjzF) (2025.03, workshop) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://openreview.net/forum?id=cAiECLDjzF)

  > Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.

- **BiRNA-BERT** — [BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization](https://www.nature.com/articles/s42003-025-08982-0) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s42003-025-08982-0) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/buetnlpbio/BiRNA-BERT)

  > Introduces BiRNA-BERT, a 117M-parameter encoder trained on 36M ncRNA sequences with adaptive dual tokenization combining nucleotide-level and BPE representations.

- **mRNABERT** — [mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset](https://www.nature.com/articles/s41467-025-65340-8) (2025.11) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65340-8) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)

  > Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.

</details>

</blockquote>

</details>

</blockquote>

</details>

<details open>
<summary><b>Other Materials</b></summary>

<blockquote>

<details open>
<summary><b>Benchmarks & Evaluations (12)</b></summary>

- **GUE** — [DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genome](https://arxiv.org/abs/2306.15006) (2023.06, preprint) [![abs](https://img.shields.io/badge/abs-2023.06-b31b1b.svg)](https://arxiv.org/abs/2306.15006) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2306.15006)

  > Introduces DNABERT-2 along with GUE (Genome Understanding Evaluation), a benchmark of 36 datasets across 9 task categories for evaluating genome foundation models.

- **BEND** — [BEND: Benchmarking DNA Language Models on biologically meaningful tasks](https://proceedings.iclr.cc/paper_files/paper/2024/hash/429e7b31625a8b7839f9e4d6e2aa9bb9-Abstract-Conference.html) (2024.05) [![abs](https://img.shields.io/badge/abs-2024.05-b31b1b.svg)](https://proceedings.iclr.cc/paper_files/paper/2024/hash/429e7b31625a8b7839f9e4d6e2aa9bb9-Abstract-Conference.html) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/frederikkemarin/BEND)

  > Proposes BEND, a benchmark of biologically meaningful tasks for evaluating DNA language models, covering gene regulation, chromatin accessibility, and conservation prediction.

- **BEACON** — [BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html) (2024.12) [![abs](https://img.shields.io/badge/abs-2024.12-b31b1b.svg)](https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/terry-r123/RNABenchmark)

  > Introduces BEACON, a comprehensive benchmark covering 13 RNA tasks across structural, functional, and engineering categories for systematic evaluation of RNA language models.

- **RNA LLM Folding** — [Comprehensive benchmarking of large language models for RNA secondary structure prediction](https://academic.oup.com/bib/article/26/2/bbaf137/8109668) (2025.03) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://academic.oup.com/bib/article/26/2/bbaf137/8109668) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/sinc-lab/rna-llm-folding)

  > Systematically benchmarks 6 RNA large language models on RNA secondary structure prediction across 4 datasets, revealing performance gaps and limitations of current LLM-based folding approaches.

- **RNA 3D Benchmark** — [Comprehensive Benchmark for RNA 3D Structure-Function Modeling](https://arxiv.org/abs/2503.21681) (2025.03, preprint) [![abs](https://img.shields.io/badge/abs-2025.03-b31b1b.svg)](https://arxiv.org/abs/2503.21681) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2503.21681)

  > Presents a comprehensive benchmark for RNA 3D structure-function modeling with 7 tasks across 9 datasets, evaluating how well models capture tertiary structural information for functional prediction.

- **RNAGym** — [RNAGym: A Benchmark for RNA Fitness and Structure Prediction](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1) (2025.06, preprint) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1)

  > Presents RNAGym, a benchmark for evaluating RNA foundation models on fitness landscape prediction and 2D/3D structure prediction tasks with standardized evaluation protocols.

- **DNALongBench** — [DNALongBench: Benchmarking Long-range Genomic Tasks](https://www.nature.com/articles/s41467-025-65077-4) (2025.06) [![abs](https://img.shields.io/badge/abs-2025.06-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65077-4)

  > Introduces DNALongBench, a benchmark of 5 long-range genomic tasks with sequences up to 1M base pairs for evaluating foundation models on long-context genomic understanding.

- **mRNABench** — [mRNABench: Benchmarking Nucleotide FMs on Mature mRNA Tasks](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) (2025.07, preprint) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1) [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/morrislab/mRNABench)

  > Proposes mRNABench with 10 datasets, 59 tasks, and 135K experiments for benchmarking nucleotide foundation models specifically on mature mRNA prediction tasks including stability and translation efficiency.

- **DNA FM Benchmark** — [Benchmarking DNA Foundation Models for Genomic and Genetic Tasks](https://www.nature.com/articles/s41467-025-65823-8) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://www.nature.com/articles/s41467-025-65823-8)

  > Provides a systematic benchmark of DNA foundation models across genomic and genetic tasks, including RNA-relevant tasks, evaluating representational capabilities and transfer learning performance.

- **Genomic LM RNA Eval** — [Benchmarking Pre-trained Genomic Language Models for RNA Predictive Tasks](https://www.nature.com/articles/s41467-025-66899-y) (2025.08) [![abs](https://img.shields.io/badge/abs-2025.08-b31b1b.svg)](https://www.nature.com/articles/s41467-025-66899-y)

  > Systematically benchmarks 11 pre-trained genomic language models on 4 RNA-specific tasks including ncRNA classification, m6A modification, splicing, and translation efficiency prediction.

- **RNAscope** — [RNAscope: Comprehensive Benchmark for RNA Foundation Models](https://openreview.net/forum?id=zYAuJxcl2E) (2025.10, preprint) [![abs](https://img.shields.io/badge/abs-2025.10-b31b1b.svg)](https://openreview.net/forum?id=zYAuJxcl2E) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://openreview.net/forum?id=zYAuJxcl2E)

  > Introduces RNAscope, a comprehensive benchmark with 15 tasks and 1,253 experiments for evaluating RNA foundation models across structure prediction, interaction, and function annotation.

- **NABench** — [NABench: Large-Scale Benchmarks of Nucleotide Foundation Models for Fitness Prediction](https://arxiv.org/html/2511.02888v1) (2025.11, preprint) [![abs](https://img.shields.io/badge/abs-2025.11-b31b1b.svg)](https://arxiv.org/html/2511.02888v1) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/html/2511.02888v1)

  > Introduces NABench, a nucleic acid fitness prediction benchmark with 2.6M+ mutated sequences and 160+ experimental conditions for evaluating foundation models on RNA and DNA fitness landscapes.

</details>

<details open>
<summary><b>Surveys & Reviews (3)</b></summary>

- **Comparative Review of RNA LMs** — [A Comparative Review of RNA Language Models](https://arxiv.org/abs/2505.09087) (2025.05, preprint) [![abs](https://img.shields.io/badge/abs-2025.05-b31b1b.svg)](https://arxiv.org/abs/2505.09087) [![preprint](https://img.shields.io/badge/preprint-gray.svg)](https://arxiv.org/abs/2505.09087)

  > Provides a comparative review of 13 RNA language models, 3 DNA language models, and 1 protein language model, analyzing their architectures, pre-training strategies, and performance across RNA downstream tasks.

- **LLMs in Bioinformatics** — [Large Language Models in Bioinformatics: A Survey](https://aclanthology.org/2025.findings-acl.184/) (2025.07) [![abs](https://img.shields.io/badge/abs-2025.07-b31b1b.svg)](https://aclanthology.org/2025.findings-acl.184/)

  > Comprehensive survey of large language models applied to bioinformatics including DNA, RNA, and protein domains, covering model architectures, training paradigms, and applications across biological sequences.

- **Genome LM Survey** — [A Comprehensive Survey of Genome Language Models in Bioinformatics](https://academic.oup.com/bib/article/27/1/bbaf724/8426124) (2026.01) [![abs](https://img.shields.io/badge/abs-2026.01-b31b1b.svg)](https://academic.oup.com/bib/article/27/1/bbaf724/8426124)

  > Surveys genome language models for DNA and RNA, discussing architectural innovations, pre-training strategies, limitations in long-range modeling, and future directions for biological sequence understanding.

</details>

</blockquote>

</details>

## Detailed Tables

<details open>
<summary><b>RNA Sequence Models</b></summary>

<blockquote>

<details open>
<summary><b>ncRNA Sequence Models</b></summary>

Models primarily focused on non-coding RNA sequences (from RNAcentral, Rfam, etc.).

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**RNABert**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1093/nargab/lqac012)</nobr> | <nobr>[Code](https://github.com/mana438/RNABERT)</nobr> | <nobr>2022.01</nobr> | <nobr>Encoder-only</nobr> | <nobr>0.5M</nobr> | <nobr>Rfam seed alignments + ncRNA</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAFM**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://arxiv.org/abs/2204.00300)</nobr> | <nobr>[Code](https://huggingface.co/multimolecule/rnafm)</nobr> | <nobr>2022.04<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>100M</nobr> | <nobr>RNAcentral (23M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAMSM**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1093/nar/gkad1031)</nobr> | <nobr>[Code](https://github.com/yikunpku/RNA-MSM)</nobr> | <nobr>2024.01</nobr> | <nobr>Encoder-only</nobr> | <nobr>95M</nobr> | <nobr>Rfam families + MSA homologs</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNA-km**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.01.27.577533)</nobr> | <nobr>[Code](https://github.com/gongtiansu/RNA-km)</nobr> | <nobr>2024.01<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>152M</nobr> | <nobr>RNAcentral (23M ncRNA seqs)</nobr> | <nobr>SNT + k-mer masking</nobr> |
| <nobr>**RNAErnie**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00836-4)</nobr> | <nobr>[Code](https://huggingface.co/LLM-EDA/RNAErnie)</nobr> | <nobr>2024.05</nobr> | <nobr>Encoder-only</nobr> | <nobr>105M</nobr> | <nobr>RNAcentral (23M seqs)</nobr> | <nobr>Nucleotide + motif</nobr> |
| <nobr>**DGRNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.10.31.621427)</nobr> | - | <nobr>2024.10<br><sub>preprint</sub></nobr> | <nobr>Hybrid (SSM)</nobr> | <nobr>100M</nobr> | <nobr>MARS (100M RNA seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**AIDO.RNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.11.28.625345)</nobr> | <nobr>[Code](https://huggingface.co/genbio-ai/AIDO.RNA-1.6B)</nobr> | <nobr>2024.11<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>650M / 1.6B</nobr> | <nobr>RNAcentral (42M seqs, ~30B nt)</nobr> | <nobr>SNT</nobr> |
| <nobr>**ChaRNABERT**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://openreview.net/forum?id=cAiECLDjzF)</nobr> | - | <nobr>2025.03<br><sub>workshop</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>8M-650M</nobr> | <nobr>RNAcentral + NCBI (62M seqs)</nobr> | <nobr>Learnable (GBST)</nobr> |
| <nobr>**RiNALMo**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-60872-5)</nobr> | <nobr>[Code](https://github.com/lbcb-sci/RiNALMo)</nobr> | <nobr>2025.07</nobr> | <nobr>Encoder-only</nobr> | <nobr>135M-650M</nobr> | <nobr>RNAcentral (36M ncRNA seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNA-BERTa**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1)</nobr> | <nobr>[Code](https://huggingface.co/IlPakoZ/RNA-BERTa9700)</nobr> | <nobr>2025.09<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>55.9M</nobr> | <nobr>Public RNA collections (9.76M seqs)</nobr> | <nobr>BPE</nobr> |
| <nobr>**ProtRNA**</nobr> | <nobr>Adapted / Derived RNA Models</nobr> | <nobr>[Paper](https://www.sciencedirect.com/science/article/pii/S2405471225002042)</nobr> | <nobr>[Code](https://github.com/roxie-zhang/ProtRNA)</nobr> | <nobr>2025.09</nobr> | <nobr>Encoder-only</nobr> | <nobr>ESM-2 derived</nobr> | <nobr>RNAcentral (6M representative seqs)</nobr> | <nobr>RNA tokens</nobr> |
| <nobr>**ERNIE-RNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-64972-0)</nobr> | <nobr>[Code](https://huggingface.co/multimolecule/ernierna-ss)</nobr> | <nobr>2025.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>86M</nobr> | <nobr>RNAcentral (20.4M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**BiRNA-BERT**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42003-025-08982-0)</nobr> | <nobr>[Code](https://github.com/buetnlpbio/BiRNA-BERT)</nobr> | <nobr>2025.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>117M</nobr> | <nobr>RNAcentral (36M seqs, ~26.4B nt)</nobr> | <nobr>Dual (NUC + BPE)</nobr> |
| <nobr>**HydraRNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7)</nobr> | <nobr>[Code](https://github.com/GuipengLi/HydraRNA)</nobr> | <nobr>2025.11</nobr> | <nobr>Hybrid (SSM+Attention)</nobr> | <nobr>84M</nobr> | <nobr>28.1M RNAs (ncRNA + coding)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAElectra**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.64898/2026.03.15.711950)</nobr> | - | <nobr>2026.03<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | - | <nobr>RNAcentral ncRNAs</nobr> | <nobr>SNT</nobr> |
| <nobr>**RNAret**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42003-026-09757-x)</nobr> | <nobr>[Code](https://github.com/DrBlackZJU/RNAret/)</nobr> | <nobr>2026.03</nobr> | <nobr>Hybrid (RetNet)</nobr> | <nobr>12M</nobr> | <nobr>RNAcentral (29.8M ncRNA seqs)</nobr> | <nobr>1/3/5-mer</nobr> |

</details>

<details open>
<summary><b>mRNA / CDS Sequence Models</b></summary>

Models focused on messenger RNA coding sequences or full mRNA sequences.

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**GenSLM**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1177/10943420231201154)</nobr> | - | <nobr>2023.11</nobr> | <nobr>Decoder-only</nobr> | <nobr>2.5B-25B</nobr> | <nobr>110M+ gene seqs + 1.5M SARS-CoV-2 genomes</nobr> | <nobr>Codon-level</nobr> |
| <nobr>**CaLM**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00791-0)</nobr> | <nobr>[Code](https://github.com/oxpig/CaLM)</nobr> | <nobr>2024.02</nobr> | <nobr>Encoder-only</nobr> | <nobr>86M</nobr> | <nobr>~9M non-redundant CDS</nobr> | <nobr>Codon-level (triplet)</nobr> |
| <nobr>**mRNA-FM**</nobr> | <nobr>Adapted / Derived RNA Models</nobr> | <nobr>[Paper](https://github.com/ml4bio/RNA-FM)</nobr> | <nobr>[Code](https://github.com/ml4bio/RNA-FM)</nobr> | <nobr>2024.03</nobr> | <nobr>Encoder-only</nobr> | <nobr>239M</nobr> | <nobr>mRNA CDS (45M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**CodonBERT**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1101/gr.278870.123)</nobr> | <nobr>[Code](https://github.com/Sanofi-Public/CodonBERT)</nobr> | <nobr>2024.08</nobr> | <nobr>Encoder-only</nobr> | <nobr>110M</nobr> | <nobr>NCBI (10M mRNA CDS)</nobr> | <nobr>Codon-aware</nobr> |
| <nobr>**HELM**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://arxiv.org/abs/2410.12459)</nobr> | - | <nobr>2024.10<br><sub>preprint</sub></nobr> | <nobr>Encoder-Decoder</nobr> | - | <nobr>mRNA coding sequences</nobr> | <nobr>Codon-hierarchical</nobr> |
| <nobr>**Helix-mRNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://openreview.net/forum?id=Ky0CkFiVhu)</nobr> | <nobr>[Code](https://huggingface.co/helical-ai/helix-mRNA)</nobr> | <nobr>2025.03<br><sub>workshop</sub></nobr> | <nobr>Hybrid (SSM+Attention)</nobr> | <nobr>Compact</nobr> | <nobr>mRNA sequences</nobr> | <nobr>SNT + codon markers</nobr> |
| <nobr>**CodonFM**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/)</nobr> | <nobr>[Code](https://github.com/NVIDIA-Digital-Bio/CodonFM)</nobr> | <nobr>2025.10</nobr> | <nobr>Encoder-only</nobr> | <nobr>80M / 600M / 1B</nobr> | <nobr>RefSeq CDS (131M seqs, 22K+ species)</nobr> | <nobr>Codon-level</nobr> |
| <nobr>**mRNABERT**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65340-8)</nobr> | <nobr>[Code](https://huggingface.co/Taykhoom/mRNABERT-no-flashattention)</nobr> | <nobr>2025.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>114M</nobr> | <nobr>18M mRNA seqs (NCBI, MG-RAST, GWH, MGnify)</nobr> | <nobr>Dual tokenization</nobr> |
| <nobr>**mRNA-GPT**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1)</nobr> | <nobr>[Code](https://github.com/ZHymLumine/mRNA-GPT/)</nobr> | <nobr>2025.12<br><sub>preprint</sub></nobr> | <nobr>Decoder-only</nobr> | <nobr>302M</nobr> | <nobr>NCBI CDS (80M bact. + 83M euk. + 2M arch.)</nobr> | <nobr>Codon / nucleotide</nobr> |
| <nobr>**codonGPT**</nobr> | <nobr>Adapted / Derived RNA Models</nobr> | <nobr>[Paper](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118)</nobr> | <nobr>[Code](https://github.com/NanilTx/codonGPT_pub)</nobr> | <nobr>2025.12</nobr> | <nobr>Decoder-only</nobr> | <nobr>GPT-2 based</nobr> | <nobr>Model-organism CDS (338K seqs)</nobr> | <nobr>Codon-level</nobr> |
| <nobr>**NUWA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3)</nobr> | <nobr>[Code](https://github.com/zysxmu/NUWA)</nobr> | <nobr>2026.02<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | - | <nobr>Multi-species mRNA CDS (115M seqs)</nobr> | <nobr>Codon tokens</nobr> |
| <nobr>**RIBOSPAN**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://arxiv.org/abs/2608.22849v2)</nobr> | - | <nobr>2026.08<br><sub>preprint</sub></nobr> | <nobr>Specialized</nobr> | - | - | <nobr>Codon-level</nobr> |

</details>

<details open>
<summary><b>UTR Sequence Models</b></summary>

Models focused on untranslated regions (5'UTR, 3'UTR).

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**UTR-LM**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00823-9)</nobr> | <nobr>[Code](https://huggingface.co/multimolecule/utrlm-te_el)</nobr> | <nobr>2024.04</nobr> | <nobr>Encoder-only</nobr> | <nobr>1M</nobr> | <nobr>Ensembl 5'UTR (>214K seqs + synthetic)</nobr> | <nobr>SNT</nobr> |
| <nobr>**3UTRBERT**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1002/advs.202407013)</nobr> | <nobr>[Code](https://github.com/yangyn533/3UTRBERT)</nobr> | <nobr>2024.10</nobr> | <nobr>Encoder-only</nobr> | <nobr>86M</nobr> | <nobr>GENCODE 3'UTR (20K seqs)</nobr> | <nobr>3-mer</nobr> |
| <nobr>**miRBind2**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2026.03.19.712027v1)</nobr> | - | <nobr>2026.03<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | - | - | <nobr>SNT</nobr> |

</details>

<details open>
<summary><b>Specific RNA Type Models</b></summary>

Models targeting specific RNA types or species (splicing, lncRNA, G-quadruplex, plant RNA, RNA families).

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**SpliceBERT**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1093/bib/bbae163)</nobr> | <nobr>[Code](https://github.com/chenkenbio/SpliceBERT)</nobr> | <nobr>2024.03</nobr> | <nobr>Encoder-only</nobr> | <nobr>20M</nobr> | <nobr>UCSC pre-mRNA (72 species, >2M seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**RFamLlama**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://openreview.net/forum?id=dXnQedxEJD)</nobr> | <nobr>[Code](https://huggingface.co/jinyuan22/RFamLlama-base)</nobr> | <nobr>2024.06<br><sub>workshop</sub></nobr> | <nobr>Decoder-only</nobr> | <nobr>13-88M</nobr> | <nobr>Rfam (>4,000 families, 0.6M seqs)</nobr> | <nobr>Nucleotide + family</nobr> |
| <nobr>**PlantRNA-FM**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-024-00946-z)</nobr> | <nobr>[Code](https://huggingface.co/yangheng/PlantRNA-FM)</nobr> | <nobr>2024.12</nobr> | <nobr>Encoder-only</nobr> | <nobr>35M</nobr> | <nobr>OneKP (1,124 plant species transcriptomes)</nobr> | <nobr>SNT</nobr> |
| <nobr>**LncRNA-BERT**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1)</nobr> | <nobr>[Code](https://github.com/luukromeijn/lncRNA-Py)</nobr> | <nobr>2025.01<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | - | <nobr>GENCODE + RefSeq + NONCODE (536K seqs)</nobr> | <nobr>CSE / k-mer / nt</nobr> |
| <nobr>**G4mer**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65020-7)</nobr> | <nobr>[Code](https://huggingface.co/Biociphers/g4mer)</nobr> | <nobr>2025.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>46M</nobr> | <nobr>Human transcriptome (G-quadruplex)</nobr> | <nobr>SNT</nobr> |
| <nobr>**Orthrus**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41592-026-03064-3)</nobr> | <nobr>[Code](https://huggingface.co/quietflamingo/orthrus-large-4-track)</nobr> | <nobr>2026.04</nobr> | <nobr>Hybrid (SSM)</nobr> | <nobr>1.3M / 10.1M</nobr> | <nobr>GENCODE + RefSeq + Zoonomia (32M transcripts)</nobr> | <nobr>SNT</nobr> |

</details>

<details open>
<summary><b>Structure-aware RNA Models</b></summary>

Models incorporating RNA secondary or tertiary structure information during pre-training or inference.

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**ATOM-1**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1101/2023.12.13.571579)</nobr> | - | <nobr>2023.12<br><sub>preprint</sub></nobr> | <nobr>Encoder-decoder</nobr> | - | <nobr>Chemical mapping sequencing data</nobr> | <nobr>SNT</nobr> |
| <nobr>**MP-RNA**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://aclanthology.org/2024.findings-emnlp.304/)</nobr> | <nobr>[Code](https://huggingface.co/yangheng/MP-RNA)</nobr> | <nobr>2024.11</nobr> | <nobr>Encoder-only</nobr> | <nobr>52-186M</nobr> | <nobr>OneKP (seq + structure)</nobr> | <nobr>SNT</nobr> |
| <nobr>**OmniGenome**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/35500)</nobr> | <nobr>[Code](https://huggingface.co/yangheng/OmniGenome-186M)</nobr> | <nobr>2025.04</nobr> | <nobr>Encoder-only</nobr> | <nobr>52M / 186M</nobr> | <nobr>OneKP (seq-structure pairs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**StructRFM**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1)</nobr> | <nobr>[Code](https://github.com/heqin-zhu/structRFM)</nobr> | <nobr>2025.08<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | - | <nobr>21M seq-structure pairs</nobr> | <nobr>SNT</nobr> |

</details>

<details open>
<summary><b>RNA Generative Models</b></summary>

Models focused on RNA sequence generation or generative transcript modeling.

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**GenerRNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1371/journal.pone.0310814)</nobr> | <nobr>[Code](https://huggingface.co/pfnet/GenerRNA)</nobr> | <nobr>2024.10</nobr> | <nobr>Decoder-only</nobr> | <nobr>350M</nobr> | <nobr>RNAcentral (16.09M seqs, ~17.4B nt)</nobr> | <nobr>BPE</nobr> |
| <nobr>**RNAGenesis**</nobr> | <nobr>Adapted / Derived RNA Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2)</nobr> | <nobr>[Code](https://huggingface.co/Zaixi/RNAGenesis)</nobr> | <nobr>2024.12<br><sub>preprint</sub></nobr> | <nobr>Encoder + Diffusion</nobr> | <nobr>1B</nobr> | <nobr>RNAcentral clustered ncRNA</nobr> | <nobr>Hybrid N-gram</nobr> |
| <nobr>**EVA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2)</nobr> | - | <nobr>2026.03<br><sub>preprint</sub></nobr> | <nobr>Decoder-only (MoE)</nobr> | - | <nobr>114M+ full-length RNA seqs</nobr> | - |

</details>

<details open>
<summary><b>General / Other RNA Models</b></summary>

General-purpose RNA models covering multiple RNA types.

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**Uni-RNA**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1)</nobr> | <nobr>[Code](https://github.com/ComDec/unirna_tf)</nobr> | <nobr>2023.07<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>400M</nobr> | <nobr>RNAcentral + MG-RAST + MGnify (1B seqs)</nobr> | <nobr>SNT</nobr> |
| <nobr>**LoRNA SH**</nobr> | <nobr>Specialized RNA Foundation Models</nobr> | <nobr>[Paper](https://doi.org/10.1101/2024.08.26.609813)</nobr> | - | <nobr>2024.08<br><sub>preprint</sub></nobr> | <nobr>Hybrid (StripedHyena)</nobr> | <nobr>6.5M</nobr> | <nobr>Full-length transcriptome architecture data</nobr> | <nobr>Specialized nt + region</nobr> |
| <nobr>**RNALens**</nobr> | <nobr>Core RNA Foundation Models</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1)</nobr> | <nobr>[Code](https://github.com/oomics/RNALens)</nobr> | <nobr>2025.07<br><sub>preprint</sub></nobr> | <nobr>Encoder-only</nobr> | <nobr>469M</nobr> | <nobr>Multispecies genomic + 5'UTR sequences</nobr> | <nobr>BPE</nobr> |

</details>

</blockquote>

</details>

<details open>
<summary><b>Broad RNA-Inclusive Nucleotide / Multi-modal Models</b></summary>

Broad sequence foundation models whose pre-training explicitly includes RNA or transcript sequences alongside DNA, protein, or other biological sequence modalities.

| Model <img width=180/> | Scope <img width=190/> | Paper <img width=110/> | Code <img width=110/> | Date / Status <img width=90/> | Architecture <img width=150/> | Params <img width=90/> | Pre-training Data <img width=240/> | Tokenization <img width=130/> |
|:------|:------|:-----:|:----:|:----:|:-------------|:-------|:------------------|:-------------|
| <nobr>**METAGENE-1**</nobr> | <nobr>Broad RNA-Inclusive Foundation Models</nobr> | <nobr>[Paper](https://arxiv.org/abs/2501.02045)</nobr> | <nobr>[Code](https://huggingface.co/metagene-ai/METAGENE-1)</nobr> | <nobr>2025.01<br><sub>preprint</sub></nobr> | <nobr>Decoder-only</nobr> | <nobr>7B</nobr> | <nobr>Metagenomic DNA + RNA sequences (1.5T bp)</nobr> | <nobr>BPE</nobr> |
| <nobr>**Life-Code**</nobr> | <nobr>Broad RNA-Inclusive Foundation Models</nobr> | <nobr>[Paper](https://arxiv.org/abs/2502.07299)</nobr> | - | <nobr>2025.02<br><sub>preprint</sub></nobr> | <nobr>Hybrid long-sequence</nobr> | - | <nobr>DNA + RNA/cDNA + amino-acid sequences unified into nucleotide-based sequences</nobr> | <nobr>Codon-level</nobr> |
| <nobr>**LucaOne**</nobr> | <nobr>Broad RNA-Inclusive Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s42256-025-01044-4)</nobr> | <nobr>[Code](https://github.com/LucaOne/LucaOneApp)</nobr> | <nobr>2025.06</nobr> | <nobr>Encoder-only</nobr> | <nobr>1.8B</nobr> | <nobr>RefSeq DNA/RNA + UniRef50/UniProt/ColabFoldDB proteins</nobr> | <nobr>Nucleotide + amino-acid tokens</nobr> |
| <nobr>**Evo 2**</nobr> | <nobr>Broad RNA-Inclusive Foundation Models</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41586-026-10176-5)</nobr> | <nobr>[Code](https://github.com/ArcInstitute/evo2)</nobr> | <nobr>2026.03</nobr> | <nobr>Hybrid (StripedHyena 2)</nobr> | <nobr>7B / 40B</nobr> | <nobr>OpenGenome2 DNA + eukaryotic mRNA + ncRNA (RNAcentral/Rfam/Ensembl/NCBI)</nobr> | <nobr>SNT</nobr> |
| <nobr>**OmniNA**</nobr> | <nobr>Broad RNA-Inclusive Foundation Models</nobr> | <nobr>[Paper](https://academic.oup.com/nar/article/54/6/gkag083/8528802)</nobr> | <nobr>[Code](https://github.com/xilinshen/OmniNA)</nobr> | <nobr>2026.03</nobr> | <nobr>Decoder-only</nobr> | <nobr>66M / 1.7B</nobr> | <nobr>NCBI NT DNA + RNA sequences + annotations (91.7M seqs, 1.076T bases)</nobr> | <nobr>BPE + annotation prompts</nobr> |

</details>

<details open>
<summary><b>Other Materials</b></summary>

<blockquote>

<details open>
<summary><b>Benchmarks & Evaluations</b></summary>

Benchmark datasets and systematic evaluations of RNA / nucleotide foundation models.

| Benchmark <img width=200/> | Paper <img width=120/> | Code <img width=120/> | Date / Status <img width=90/> | Focus <img width=300/> | Scale <img width=220/> |
|:----------|:-----:|:----:|:----:|:------|:------|
| <nobr>**GUE**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2306.15006)</nobr> | - | <nobr>2023.06<br><sub>preprint</sub></nobr> | <nobr>Genome understanding evaluation</nobr> | <nobr>36 datasets, 9 tasks</nobr> |
| <nobr>**BEND**</nobr> | <nobr>[Paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/429e7b31625a8b7839f9e4d6e2aa9bb9-Abstract-Conference.html)</nobr> | <nobr>[Code](https://github.com/frederikkemarin/BEND)</nobr> | <nobr>2024.05</nobr> | <nobr>DNA LM biologically meaningful tasks</nobr> | <nobr>Multiple tasks</nobr> |
| <nobr>**BEACON**</nobr> | <nobr>[Paper](https://papers.nips.cc/paper_files/paper/2024/hash/a8ea503d91320fcfe12cba61c8a6d285-Abstract-Datasets_and_Benchmarks_Track.html)</nobr> | <nobr>[Code](https://github.com/terry-r123/RNABenchmark)</nobr> | <nobr>2024.12</nobr> | <nobr>RNA (structural, functional, engineering)</nobr> | <nobr>13 tasks</nobr> |
| <nobr>**RNA LLM Folding**</nobr> | <nobr>[Paper](https://academic.oup.com/bib/article/26/2/bbaf137/8109668)</nobr> | <nobr>[Code](https://github.com/sinc-lab/rna-llm-folding)</nobr> | <nobr>2025.03</nobr> | <nobr>RNA secondary structure prediction</nobr> | <nobr>6 RNA LLMs, 4 datasets</nobr> |
| <nobr>**RNA 3D Benchmark**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2503.21681)</nobr> | - | <nobr>2025.03<br><sub>preprint</sub></nobr> | <nobr>RNA 3D structure-function</nobr> | <nobr>7 tasks, 9 datasets</nobr> |
| <nobr>**RNAGym**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.06.16.660049v1)</nobr> | - | <nobr>2025.06<br><sub>preprint</sub></nobr> | <nobr>RNA fitness & structure prediction (2D/3D)</nobr> | <nobr>Fitness + structure tasks</nobr> |
| <nobr>**DNALongBench**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65077-4)</nobr> | - | <nobr>2025.06</nobr> | <nobr>Long-range genomic tasks</nobr> | <nobr>5 tasks, up to 1M bp</nobr> |
| <nobr>**mRNABench**</nobr> | <nobr>[Paper](https://www.biorxiv.org/content/10.1101/2025.07.05.662870v1)</nobr> | <nobr>[Code](https://github.com/morrislab/mRNABench)</nobr> | <nobr>2025.07<br><sub>preprint</sub></nobr> | <nobr>Mature mRNA prediction tasks</nobr> | <nobr>10 datasets, 59 tasks, 135K experiments</nobr> |
| <nobr>**DNA FM Benchmark**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-65823-8)</nobr> | - | <nobr>2025.07</nobr> | <nobr>Genomic & genetic tasks (incl. RNA-relevant)</nobr> | <nobr>Multiple tasks</nobr> |
| <nobr>**Genomic LM RNA Eval**</nobr> | <nobr>[Paper](https://www.nature.com/articles/s41467-025-66899-y)</nobr> | - | <nobr>2025.08</nobr> | <nobr>RNA processes (ncRNA, m6A, splicing, TE)</nobr> | <nobr>11 genomic LMs, 4 RNA tasks</nobr> |
| <nobr>**RNAscope**</nobr> | <nobr>[Paper](https://openreview.net/forum?id=zYAuJxcl2E)</nobr> | - | <nobr>2025.10<br><sub>preprint</sub></nobr> | <nobr>RNA (structure, interaction, function)</nobr> | <nobr>15 tasks, 1,253 experiments</nobr> |
| <nobr>**NABench**</nobr> | <nobr>[Paper](https://arxiv.org/html/2511.02888v1)</nobr> | - | <nobr>2025.11<br><sub>preprint</sub></nobr> | <nobr>Nucleic acid fitness prediction</nobr> | <nobr>2.6M+ mutated seqs, 160+ experiments</nobr> |

</details>

<details open>
<summary><b>Surveys & Reviews</b></summary>

| Title <img width=350/> | Paper <img width=120/> | Date / Status <img width=90/> | Scope <img width=400/> |
|:------|:-----:|:----:|:------|
| <nobr>**A Comparative Review of RNA Language Models**</nobr> | <nobr>[Paper](https://arxiv.org/abs/2505.09087)</nobr> | <nobr>2025.05<br><sub>preprint</sub></nobr> | <nobr>Compares 13 RNA LMs + 3 DNA LMs + 1 protein LM</nobr> |
| <nobr>**Large Language Models in Bioinformatics: A Survey**</nobr> | <nobr>[Paper](https://aclanthology.org/2025.findings-acl.184/)</nobr> | <nobr>2025.07</nobr> | <nobr>LLMs for DNA, RNA, proteins (ACL 2025 Findings, updated 2026)</nobr> |
| <nobr>**A Comprehensive Survey of Genome Language Models in Bioinformatics**</nobr> | <nobr>[Paper](https://academic.oup.com/bib/article/27/1/bbaf724/8426124)</nobr> | <nobr>2026.01</nobr> | <nobr>DNA/RNA genome LMs: limitations, long-range modeling</nobr> |

</details>

</blockquote>

</details>

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


## Contributing

Contributions are welcome! If you find a missing RNA foundation model, benchmark, or survey paper, please:

1. Open an issue with the model/paper details
2. Or submit a pull request following the existing table format

**What to include**: reusable sequence foundation models with explicit RNA, mRNA, CDS, UTR, transcript, ncRNA, RNA metagenomic, or RNA/transcript-derived sequence pre-training / large-scale training signal that can support embedding extraction, fine-tuning, generation, or broad transfer to RNA downstream tasks.

**What NOT to include**: downstream-only predictors/designers, reverse-translation or inverse-folding pipelines, RNA 3D prediction systems, DNA/protein/multi-omics FMs with no explicit RNA/transcript sequence pre-training signal, expression-profile/RNA-seq feature models, single-cell foundation models, protein-only models, non-model datasets/benchmarks/surveys as model entries, or papers with no reusable sequence model.

**Metadata workflow**: confirmed entries live in `data/papers.yaml`, temporary discoveries go to `data/candidates.yaml`, and intentionally excluded items are tracked in `data/excluded.yaml`. A scheduled GitHub Action scans recent arXiv, bioRxiv, and Crossref metadata, auto-classifies promotable RNA-sequence or RNA-inclusive sequence foundation model candidates into draft `data/papers.yaml` records, regenerates `README.md` and `assets/model_timeline.svg`, and opens a review PR. After editing confirmed metadata, run `python generate_paper_list.py` and `python scripts/validate_papers.py`; CI also checks that generated README content is committed.


*Last updated: May 2026*
