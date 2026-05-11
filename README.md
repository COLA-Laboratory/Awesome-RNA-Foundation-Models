# Strict RNA Foundation Models

This file is a conservative RNA foundation-model-only view of the current repository entries. It keeps models that introduce or release a reusable pretrained RNA, mRNA, CDS, codon, UTR, or RNA-structure-aware backbone.

## Boundary

Included:

- Models with their own RNA/mRNA/CDS/UTR sequence pre-training or released reusable checkpoint.
- Subtype-specific RNA language models when the pretrained backbone can be reused beyond one benchmark.
- Adapted models only when the adaptation yields a reusable RNA language model.

Excluded from this strict view:

- Downstream predictors or design pipelines that mainly consume an existing foundation model.
- Reverse-translation, inverse-folding, RNA 3D prediction, or aptamer-design systems whose main output is task-specific.
- DNA-only, broad nucleotide, central-dogma, multi-omics, or expression-profile foundation models.

## Core RNA / mRNA Foundation Models

- **RNAFM** - [Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions](https://arxiv.org/abs/2204.00300) (2022.04, preprint)
- **Uni-RNA** - [Uni-RNA: Universal Pre-trained Models for RNA across Species](https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1) (2023.07, preprint)
- **RNAErnie** - [Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning](https://www.nature.com/articles/s42256-024-00836-4) (2024.05)
- **DGRNA** - [DGRNA: a long-context RNA foundation model with bidirectional attention Mamba2](https://doi.org/10.1101/2024.10.31.621427) (2024.10, preprint)
- **HELM** - [HELM: Hierarchical Encoding for mRNA Language Modeling](https://arxiv.org/abs/2410.12459) (2024.10, preprint)
- **GenerRNA** - [GenerRNA: A generative pre-trained language model for de novo RNA design](https://doi.org/10.1371/journal.pone.0310814) (2024.10)
- **AIDO.RNA** - [A Large-Scale Foundation Model for RNA Function and Structure Prediction](https://doi.org/10.1101/2024.11.28.625345) (2024.11, preprint)
- **ChaRNABERT** - [Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models](https://openreview.net/forum?id=cAiECLDjzF) (2025.03, workshop)
- **Helix-mRNA** - [Helix-mRNA: A Hybrid Foundation Model For Full Sequence mRNA Therapeutics](https://openreview.net/forum?id=Ky0CkFiVhu) (2025.03, workshop)
- **RiNALMo** - [RiNALMo: general-purpose RNA language models can generalize well on structure prediction tasks](https://www.nature.com/articles/s41467-025-60872-5) (2025.07)
- **RNALens** - [RNALens: A Multi-task RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1) (2025.07, preprint)
- **RNA-BERTa** - [DLRNA-BERTa: A transformer approach for RNA-drug binding affinity prediction](https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1) (2025.09, preprint)
- **CodonFM** - [Introducing the CodonFM Open Model for RNA Design and Analysis](https://developer.nvidia.com/blog/introducing-the-codonfm-open-model-for-rna-design-and-analysis/) (2025.10)
- **ERNIE-RNA** - [ERNIE-RNA: an RNA language model with structure-enhanced representations](https://www.nature.com/articles/s41467-025-64972-0) (2025.11)
- **BiRNA-BERT** - [BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization](https://www.nature.com/articles/s42003-025-08982-0) (2025.11)
- **HydraRNA** - [HydraRNA: a hybrid architecture based full-length RNA language model](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7) (2025.11)
- **mRNABERT** - [mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset](https://www.nature.com/articles/s41467-025-65340-8) (2025.11)
- **mRNA-GPT** - [Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT](https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1) (2025.12, preprint)
- **NUWA** - [Large mRNA language foundation modeling with NUWA for unified sequence perception and generation](https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3) (2026.02, preprint)
- **RNAElectra** - [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://doi.org/10.64898/2026.03.15.711950) (2026.03, preprint)
- **RNAret** - [Retentive Network promotes efficient RNA language modeling of long sequences](https://www.nature.com/articles/s42003-026-09757-x) (2026.03)
- **EVA** - [EVA: Evolutionary Versatile Architect for Long-context RNA Generation](https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2) (2026.03, preprint)

## Specialized RNA Foundation Models

- **RNABert** - [Informative RNA base embedding for RNA structural alignment and clustering by deep representation learning](https://doi.org/10.1093/nargab/lqac012) (2022.01)
- **GenSLM** - [GenSLMs: Genome-scale language models reveal SARS-CoV-2 evolutionary dynamics](https://doi.org/10.1177/10943420231201154) (2023.11)
- **ATOM-1** - [ATOM-1: A Foundation Model for RNA Structure and Function Built on Chemical Mapping Data](https://doi.org/10.1101/2023.12.13.571579) (2023.12, preprint)
- **RNAMSM** - [Multiple sequence alignment-based RNA language model and its application to structural inference](https://doi.org/10.1093/nar/gkad1031) (2024.01)
- **RNA-km** - [Language models enable zero-shot prediction of RNA secondary structures including pseudoknots](https://doi.org/10.1101/2024.01.27.577533) (2024.01, preprint)
- **CaLM** - [Codon language embeddings provide strong signals for use in protein engineering](https://www.nature.com/articles/s42256-024-00791-0) (2024.02)
- **SpliceBERT** - [Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction](https://doi.org/10.1093/bib/bbae163) (2024.03)
- **UTR-LM** - [A 5' UTR language model for decoding untranslated regions of mRNA and function predictions](https://www.nature.com/articles/s42256-024-00823-9) (2024.04)
- **RFamLlama** - [RFamLlama: an efficient conditional language model for RNA sequence generation across diverse structural families](https://openreview.net/forum?id=dXnQedxEJD) (2024.06, workshop)
- **OmniGenome** - [Bridging Sequence-Structure Alignment in RNA Foundation Models](https://arxiv.org/abs/2407.11242) (2024.07, preprint)
- **CodonBERT** - [CodonBERT large language model for mRNA vaccines](https://doi.org/10.1101/gr.278870.123) (2024.08)
- **LoRNA SH** - [A long-context RNA foundation model for predicting transcriptome architecture](https://doi.org/10.1101/2024.08.26.609813) (2024.08, preprint)
- **3UTRBERT** - [Deciphering 3'UTR Mediated Gene Regulation Using Interpretable Deep Representation Learning](https://doi.org/10.1002/advs.202407013) (2024.10)
- **MP-RNA** - [MP-RNA: Unleashing Multi-species RNA Foundation Model via Calibrated Secondary Structure Prediction](https://aclanthology.org/2024.findings-emnlp.304/) (2024.11)
- **PlantRNA-FM** - [An interpretable RNA foundation model for exploring functional RNA motifs in plants](https://www.nature.com/articles/s42256-024-00946-z) (2024.12)
- **LncRNA-BERT** - [LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification](https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1) (2025.01, preprint)
- **StructRFM** - [StructRFM: Structure-guided RNA Foundation Model](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1) (2025.08, preprint)
- **G4mer** - [G4mer: An RNA language model for transcriptome-wide identification of G-quadruplexes and disease variants from population-scale genetic data](https://www.nature.com/articles/s41467-025-65020-7) (2025.11)
- **Orthrus** - [Orthrus: toward evolutionary and functional RNA foundation models](https://www.nature.com/articles/s41592-026-03064-3) (2026.04)

## Adapted But Reusable RNA Language Models

- **mRNA-FM** - [RNA-FM: The RNA Foundation Model](https://github.com/ml4bio/RNA-FM) (2024.03)
- **RNAGenesis** - [RNAGenesis: A Generalist Foundation Model for Functional RNA Therapeutics](https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2) (2024.12, preprint)
- **ProtRNA** - [ProtRNA: A protein-derived RNA language model by cross-modality transfer learning](https://www.sciencedirect.com/science/article/pii/S2405471225002042) (2025.09)
- **codonGPT** - [codonGPT: reinforcement learning on a generative language model enables scalable mRNA design](https://academic.oup.com/nar/article/53/22/gkaf1345/8384118) (2025.12)
