"""Generate a bullet-list paper index section for the README, with abstracts.
Four classification views: by foundation-model scope, RNA/data focus, architecture,
and tokenization strategy."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from collections import OrderedDict

# Fields: (name, title, url, date, github_url, hf_url, category, abstract, architecture, tokenization)
# Date convention: use the official publication / conference date when available; otherwise
# use the linked preprint date and mark the entry as a preprint. Keep `title`
# as the paper title, not a synthetic "model: title" display string.
papers = [
    # === ncRNA FMs ===
    ("RNABert", "Informative RNA base embedding for RNA structural alignment and clustering by deep representation learning",
     "https://doi.org/10.1093/nargab/lqac012", "2022.01", "https://github.com/mana438/RNABERT", None, "ncRNA FM",
     "Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.",
     "Encoder-only", "SNT"),

    ("RNAFM", "Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions",
     "https://arxiv.org/abs/2204.00300", "2022.04", None, "https://huggingface.co/multimolecule/rnafm", "ncRNA FM",
     "Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.",
     "Encoder-only", "SNT"),

    ("RNAMSM", "Multiple sequence alignment-based RNA language model and its application to structural inference",
     "https://doi.org/10.1093/nar/gkad1031", "2024.01", "https://github.com/yikunpku/RNA-MSM", None, "ncRNA FM",
     "Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.",
     "Encoder-only", "SNT"),

    ("RNA-km", "Language models enable zero-shot prediction of RNA secondary structures including pseudoknots",
     "https://doi.org/10.1101/2024.01.27.577533", "2024.01", "https://github.com/gongtiansu/RNA-km", None, "ncRNA FM",
     "Proposes RNA-km, a self-supervised RNA language model trained on 23M ncRNA sequences with k-mer masking and relative positional encoding, enabling zero-shot RNA secondary structure prediction including pseudoknots.",
     "Encoder-only", "SNT"),

    ("RNAErnie", "Multi-purpose RNA language modelling with motif-aware pretraining and type-guided fine-tuning",
     "https://www.nature.com/articles/s42256-024-00836-4", "2024.05", None, "https://huggingface.co/LLM-EDA/RNAErnie", "ncRNA FM",
     "Presents RNAErnie, an RNA-focused pre-trained model that combines motif-aware pretraining with type-guided fine-tuning for diverse RNA sequence analysis tasks.",
     "Encoder-only", "SNT"),

    ("ERNIE-RNA", "ERNIE-RNA: an RNA language model with structure-enhanced representations",
     "https://www.nature.com/articles/s41467-025-64972-0", "2025.11", None, "https://huggingface.co/multimolecule/ernierna-ss", "ncRNA FM",
     "Develops ERNIE-RNA with base-pairing-aware attention bias for structure-enhanced pre-training on RNAcentral ncRNAs, improving structure and function prediction tasks.",
     "Encoder-only", "SNT"),

    ("DGRNA", "DGRNA: a long-context RNA foundation model with bidirectional attention Mamba2",
     "https://doi.org/10.1101/2024.10.31.621427", "2024.10", None, None, "ncRNA FM",
     "Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.",
     "Hybrid/SSM", "SNT"),

    ("ChaRNABERT", "Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models",
     "https://openreview.net/forum?id=cAiECLDjzF", "2025.03", None, None, "ncRNA FM",
     "Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.",
     "Encoder-only", "Learnable"),

    ("AIDO.RNA", "A Large-Scale Foundation Model for RNA Function and Structure Prediction",
     "https://doi.org/10.1101/2024.11.28.625345", "2024.11", None, "https://huggingface.co/genbio-ai/AIDO.RNA-1.6B", "ncRNA FM",
     "Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.",
     "Encoder-only", "SNT"),

    ("BiRNA-BERT", "BiRNA-BERT allows efficient RNA language modeling with adaptive tokenization",
     "https://www.nature.com/articles/s42003-025-08982-0", "2025.11", "https://github.com/buetnlpbio/BiRNA-BERT", None, "ncRNA FM",
     "Introduces BiRNA-BERT, a 117M-parameter encoder trained on 36M ncRNA sequences with adaptive dual tokenization combining nucleotide-level and BPE representations.",
     "Encoder-only", "Learnable"),

    ("RNA-BERTa", "DLRNA-BERTa: A transformer approach for RNA-drug binding affinity prediction",
     "https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1", "2025.09", None, "https://huggingface.co/IlPakoZ/RNA-BERTa9700", "ncRNA FM",
     "Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.",
     "Encoder-only", "BPE"),

    ("RiNALMo", "RiNALMo: general-purpose RNA language models can generalize well on structure prediction tasks",
     "https://www.nature.com/articles/s41467-025-60872-5", "2025.07", "https://github.com/lbcb-sci/RiNALMo", None, "ncRNA FM",
     "Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.",
     "Encoder-only", "SNT"),

    ("RNAGenesis", "RNAGenesis: A Generalist Foundation Model for Functional RNA Therapeutics",
     "https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2", "2024.12", None, "https://huggingface.co/Zaixi/RNAGenesis", "Generative FM",
     "Proposes RNAGenesis, a 1B-parameter generative RNA model that integrates sequence representation, structure prediction, and de novo functional design, listed here as an adapted / derived RNA design model rather than a core ncRNA pre-training-only FM.",
     "Specialized", "SNT"),

    ("HydraRNA", "HydraRNA: a hybrid architecture based full-length RNA language model",
     "https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7", "2025.11", "https://github.com/GuipengLi/HydraRNA", None, "ncRNA FM",
     "Introduces HydraRNA, a full-length RNA language model using a hybrid bidirectional state space and attention architecture for both coding and non-coding RNA tasks.",
     "Hybrid/SSM", "SNT"),

    ("RNAElectra", "RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference",
     "https://doi.org/10.64898/2026.03.15.711950", "2026.03", None, None, "ncRNA FM",
     "Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.",
     "Encoder-only", "SNT"),

    # === mRNA/CDS FMs ===
    ("CodonBERT", "CodonBERT large language model for mRNA vaccines",
     "https://doi.org/10.1101/gr.278870.123", "2024.08", "https://github.com/Sanofi-Public/CodonBERT", None, "mRNA/CDS FM",
     "Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization for mRNA sequence representation and vaccine-related design tasks.",
     "Encoder-only", "Codon"),

    ("CaLM", "Codon language embeddings provide strong signals for use in protein engineering",
     "https://www.nature.com/articles/s42256-024-00791-0", "2024.02", "https://github.com/oxpig/CaLM", None, "mRNA/CDS FM",
     "Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.",
     "Encoder-only", "Codon"),

    ("HELM", "HELM: Hierarchical Encoding for mRNA Language Modeling",
     "https://arxiv.org/abs/2410.12459", "2024.10", None, None, "mRNA/CDS FM",
     "Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.",
     "Encoder-Decoder", "Codon"),

    ("Helix-mRNA", "Helix-mRNA: A Hybrid Foundation Model For Full Sequence mRNA Therapeutics",
     "https://openreview.net/forum?id=Ky0CkFiVhu", "2025.03", None, "https://huggingface.co/helical-ai/helix-mRNA", "mRNA/CDS FM",
     "Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.",
     "Hybrid/SSM", "Codon"),

    ("GEMORNA", "Deep generative models design mRNA sequences with enhanced translational capacity and stability",
     "https://www.science.org/doi/10.1126/science.adr8470", "2025.11", "https://github.com/RainaBio/GEMORNA", None, "mRNA/CDS FM",
     "Presents GEMORNA, a deep generative model for designing mRNA CDS and UTR sequences with enhanced translational capacity and stability.",
     "Specialized", "Codon"),

    ("GenSLM", "GenSLMs: Genome-scale language models reveal SARS-CoV-2 evolutionary dynamics",
     "https://doi.org/10.1177/10943420231201154", "2023.11", None, None, "mRNA/CDS FM",
     "Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.",
     "Decoder-only", "Codon"),

    ("mRNABERT", "mRNABERT: advancing mRNA sequence design with a universal language model and comprehensive dataset",
     "https://www.nature.com/articles/s41467-025-65340-8", "2025.11", None, "https://huggingface.co/Taykhoom/mRNABERT-no-flashattention", "mRNA/CDS FM",
     "Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.",
     "Encoder-only", "Learnable"),

    ("mRNA-GPT", "Large generative mRNA language foundation model for efficient coding sequence generation and design with mRNA-GPT",
     "https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1", "2025.12", "https://github.com/ZHymLumine/mRNA-GPT/", None, "mRNA/CDS FM",
     "Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.",
     "Decoder-only", "Codon"),

    ("NUWA", "Large mRNA language foundation modeling with NUWA for unified sequence perception and generation",
     "https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3", "2026.02", "https://github.com/zysxmu/NUWA", None, "mRNA/CDS FM",
     "Proposes NUWA, a large mRNA foundation model pre-trained on 115M multi-species coding sequences for unified mRNA sequence perception and generation.",
     "Encoder-only", "Codon"),

    ("mRNA-GPT (full-length)", "mRNA-GPT: Full-Length mRNA Design via Autoregressive Generation with PPO",
     "https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1", "2026.03", None, None, "mRNA/CDS FM",
     "Extends mRNA-GPT to full-length mRNA design (5'UTR+CDS+3'UTR) using autoregressive generation with PPO-based reinforcement learning to optimize translation efficiency and stability of generated mRNA sequences.",
     "Decoder-only", "Codon"),

    ("CodonMoE", "DNA Language Models for RNA Analyses",
     "https://openreview.net/forum?id=TOUrnb1EaG", "2024.09", None, None, "mRNA/CDS FM",
     "Proposes CodonMoE, a parameter-efficient approach to adapt pre-trained DNA foundation models for RNA tasks using Mixture-of-Experts adapters with codon-aware routing for improved mRNA property prediction.",
     "Specialized", "Codon"),

    # === UTR FMs ===
    ("UTR-LM", "A 5′ UTR language model for decoding untranslated regions of mRNA and function predictions",
     "https://www.nature.com/articles/s42256-024-00823-9", "2024.04", None, "https://huggingface.co/multimolecule/utrlm-te_el", "UTR FM",
     "Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.",
     "Encoder-only", "SNT"),

    ("3UTRBERT", "Deciphering 3'UTR Mediated Gene Regulation Using Interpretable Deep Representation Learning",
     "https://doi.org/10.1002/advs.202407013", "2024.10", "https://github.com/yangyn533/3UTRBERT", None, "UTR FM",
     "Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.",
     "Encoder-only", "K-mer"),

    # === Specific RNA FMs ===
    ("SpliceBERT", "Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction",
     "https://doi.org/10.1093/bib/bbae163", "2024.03", "https://github.com/chenkenbio/SpliceBERT", None, "Specific RNA FM",
     "Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.",
     "Encoder-only", "SNT"),

    ("RFamLlama", "RFamLlama: an efficient conditional language model for RNA sequence generation across diverse structural families",
     "https://openreview.net/forum?id=dXnQedxEJD", "2024.06", None, "https://huggingface.co/jinyuan22/RFamLlama-base", "Specific RNA FM",
     "Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.",
     "Decoder-only", "SNT"),

    ("PlantRNA-FM", "An interpretable RNA foundation model for exploring functional RNA motifs in plants",
     "https://www.nature.com/articles/s42256-024-00946-z", "2024.12", None, "https://huggingface.co/yangheng/PlantRNA-FM", "Specific RNA FM",
     "Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.",
     "Encoder-only", "SNT"),

    ("LncRNA-BERT", "LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification",
     "https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1", "2025.01", "https://github.com/luukromeijn/lncRNA-Py", None, "Specific RNA FM",
     "Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.",
     "Encoder-only", "K-mer"),

    ("G4mer", "G4mer: An RNA language model for transcriptome-wide identification of G-quadruplexes and disease variants from population-scale genetic data",
     "https://www.nature.com/articles/s41467-025-65020-7", "2025.11", None, "https://huggingface.co/Biociphers/g4mer", "Specific RNA FM",
     "Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.",
     "Encoder-only", "SNT"),

    # === Structure-aware RNA FMs ===
    ("ATOM-1", "ATOM-1: A Foundation Model for RNA Structure and Function Built on Chemical Mapping Data",
     "https://doi.org/10.1101/2023.12.13.571579", "2023.12", None, None, "Structure-aware FM",
     "Proposes ATOM-1, a foundation model trained on chemical mapping data to learn RNA structure-aware representations for secondary and tertiary structure probing and RNA function prediction.",
     "Encoder-Decoder", "SNT"),

    ("RibonanzaNet", "Ribonanza: deep learning of RNA structure through dual crowdsourcing",
     "https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1", "2024.02", "https://github.com/Shujun-He/RibonanzaNet", None, "Structure-aware FM",
     "Presents RibonanzaNet, a deep neural network trained on 2M RNA sequences with experimental chemical mapping data from Eterna, Rfam, and PDB, predicting RNA chemical reactivity profiles for structure determination.",
     "Specialized", "SNT"),

    ("OmniGenome", "Bridging Sequence-Structure Alignment in RNA Foundation Models",
     "https://arxiv.org/abs/2407.11242", "2024.07", None, "https://huggingface.co/yangheng/OmniGenome-186M", "Structure-aware FM",
     "Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.",
     "Encoder-only", "SNT"),

    ("MP-RNA", "MP-RNA: Unleashing Multi-species RNA Foundation Model via Calibrated Secondary Structure Prediction",
     "https://aclanthology.org/2024.findings-emnlp.304/", "2024.11", None, "https://huggingface.co/yangheng/MP-RNA", "Structure-aware FM",
     "Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.",
     "Encoder-only", "SNT"),

    ("RNA-TorsionBERT", "RNA-TorsionBERT: leveraging language models for RNA 3D torsion angles prediction",
     "https://doi.org/10.1093/bioinformatics/btaf004", "2024.12", None, "https://huggingface.co/sayby/rna_torsionBERT", "Structure-aware FM",
     "Proposes RNA-TorsionBERT, a BERT model pre-trained on PDB RNA 3D structures to predict backbone torsion angles directly from RNA sequences, enabling rapid assessment of RNA 3D structural properties.",
     "Encoder-only", "SNT"),

    ("StructRFM", "StructRFM: Structure-guided RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1", "2025.08", "https://github.com/heqin-zhu/structRFM", None, "Structure-aware FM",
     "Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.",
     "Encoder-only", "SNT"),

    # === Generative FMs ===
    ("LoRNA SH", "A long-context RNA foundation model for predicting transcriptome architecture",
     "https://doi.org/10.1101/2024.08.26.609813", "2024.08", None, None, "General RNA FM",
     "Introduces LoRNA SH, a StripedHyena-based long-context RNA foundation model trained on full-length transcriptome architecture data to predict isoform abundance, isoform structure, and variant effects.",
     "Hybrid/SSM", "SNT"),

    ("GenerRNA", "GenerRNA: A generative pre-trained language model for de novo RNA design",
     "https://doi.org/10.1371/journal.pone.0310814", "2024.10", None, "https://huggingface.co/pfnet/GenerRNA", "Generative FM",
     "Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.",
     "Decoder-only", "BPE"),

    ("GARNET", "GARNET: A Generative RNA Design Model from Microbial Genomes",
     "https://www.nature.com/articles/s41467-024-54812-y", "2024.12", "https://github.com/Doudna-lab/GARNET_DL", None, "Generative FM",
     "Develops GARNET, a generative model combining a decoder with a GNN, trained on 30M microbial genome sequences (17B nucleotides) from GTDB for designing novel functional RNA sequences with desired structural properties.",
     "Specialized", "SNT"),

    ("RNAtranslator", "RNAtranslator: Modeling protein-conditional RNA design as sequence-to-sequence natural language translation",
     "https://doi.org/10.1371/journal.pcbi.1013541", "2025.10", None, "https://huggingface.co/SobhanShukueian/rnatranslator", "Generative FM",
     "Proposes RNAtranslator, a 41.4M-parameter encoder-decoder model trained on 26M RNA-protein interaction pairs for generating RNA sequences conditioned on protein binding partners, enabling rational RNA aptamer design.",
     "Encoder-Decoder", "SNT"),

    ("EVA", "EVA: Evolutionary Versatile Architect for Long-context RNA Generation",
     "https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2", "2026.03", None, None, "Generative FM",
     "Introduces EVA, a Mixture-of-Experts decoder model for long-context RNA sequence generation, trained on 114M+ full-length RNA sequences for generating diverse functional RNA molecules at unprecedented lengths.",
     "Specialized", "BPE"),

    # === General / Other ===
    ("Uni-RNA", "Uni-RNA: Universal Pre-trained Models for RNA across Species",
     "https://www.biorxiv.org/content/10.1101/2023.07.11.548588v1", "2023.07", "https://github.com/ComDec/unirna_tf", None, "General RNA FM",
     "Presents Uni-RNA, a 400M-parameter universal RNA model pre-trained on 1B sequences from RNAcentral, MG-RAST, and MGnify, covering RNA across diverse species for general-purpose RNA representation learning.",
     "Encoder-only", "SNT"),

    ("RNALens", "RNALens: A Multi-task RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2025.07.20.665722v1", "2025.07", "https://github.com/oomics/RNALens", None, "General RNA FM",
     "Introduces RNALens, a 469M-parameter multi-task RNA foundation model pre-trained on multispecies genomic and 5'UTR sequences using BPE tokenization, supporting diverse RNA analysis tasks within a unified framework.",
     "Encoder-only", "BPE"),

    # === DNA+RNA FMs ===
    ("Evo", "Sequence Modeling and Design from Molecular to Genome Scale with Evo",
     "https://www.science.org/doi/10.1126/science.ado9336", "2024.11", "https://github.com/evo-design/evo", None, "DNA+RNA FM",
     "Presents Evo, a 7B-parameter genomic foundation model using StripedHyena architecture, pre-trained on 2.7M prokaryotic and phage genomes at single-nucleotide resolution, enabling sequence modeling and design from molecular to genome scale.",
     "Hybrid/SSM", "SNT"),

    ("LucaOne", "Generalized biological foundation model with unified nucleic acid and protein language",
     "https://www.nature.com/articles/s42256-025-01044-4", "2025.06", "https://github.com/LucaOne/LucaOne", None, "DNA+RNA FM",
     "Introduces LucaOne, a 1.8B-parameter unified model pre-trained on 800B tokens from RefSeq, UniProt, and PDB, jointly modeling DNA, RNA, and protein sequences for cross-modal biological sequence understanding.",
     "Encoder-only", "SNT"),

    ("BSM", "BSM: Small but Powerful Biological Sequence Model for Genes and Proteins",
     "https://arxiv.org/abs/2410.11499", "2024.10", None, None, "DNA+RNA FM",
     "Proposes BSM (110M/270M parameters), a biological sequence model with mixed-modal pre-training on DNA, RNA, and protein sequences from RefSeq and web-collected biological data for unified sequence representation.",
     "Specialized", "SNT"),

    ("LAMAR", "LAMAR: A Language Model for Mammalian and Viral Genomes and Transcriptomes",
     "https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1", "2024.10", "https://github.com/zhw-e8/LAMAR", None, "DNA+RNA FM",
     "Develops LAMAR, a 150M-parameter language model pre-trained on genomes and transcriptomes from 225 mammalian species (15M sequences), capturing mammalian-specific and viral genomic patterns for RNA and DNA tasks.",
     "Encoder-only", "SNT"),

    ("Orthrus", "Orthrus: toward evolutionary and functional RNA foundation models",
     "https://www.nature.com/articles/s41592-026-03064-3", "2026.04", None, "https://huggingface.co/quietflamingo/orthrus-large-4-track", "Specific RNA FM",
     "Introduces Orthrus, a Mamba-based mature RNA foundation model using contrastive learning on transcript isoforms and cross-species orthologs to learn evolutionary and functional RNA representations.",
     "Hybrid/SSM", "SNT"),

    ("METAGENE-1", "METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring",
     "https://arxiv.org/abs/2501.02045", "2025.01", None, "https://huggingface.co/metagene-ai/METAGENE-1", "DNA+RNA FM",
     "Presents METAGENE-1, a 7B-parameter metagenomic foundation model pre-trained on >1.5 trillion base pairs of wastewater metagenomic DNA and RNA sequences using BPE tokenization for pathogen detection and biosurveillance.",
     "Decoder-only", "BPE"),

    ("Life-Code", "Life-Code: Central Dogma Modeling with Multi-Omics Sequence Unification",
     "https://arxiv.org/abs/2502.07299", "2025.02", None, None, "DNA+RNA FM",
     "Proposes Life-Code, a unified foundation model that jointly models DNA, RNA, and protein following the central dogma of molecular biology, using codon-level tokenization to capture cross-modal biological relationships.",
     "Hybrid/SSM", "Codon"),

    ("Evo 2", "Genome Modeling and Design Across All Domains of Life with Evo 2",
     "https://www.nature.com/articles/s41586-026-10176-5", "2026.03", "https://github.com/ArcInstitute/evo2", None, "DNA+RNA FM",
     "Presents Evo 2 (7B/40B parameters), a next-generation genomic foundation model trained on 9 trillion nucleotides from 128K genomes spanning all domains of life, enabling genome-scale modeling, understanding, and design.",
     "Hybrid/SSM", "SNT"),

    ("OmniNA", "OmniNA: A Foundation Model for Nucleotide Sequences and Annotations",
     "https://academic.oup.com/nar/article/54/6/gkag083/8528802", "2026.01", None, None, "DNA+RNA FM",
     "Introduces OmniNA, a generative foundation model pre-trained on 91.7M nucleotide sequences with annotations (1076B bases), jointly modeling sequences and functional annotations for unified nucleotide analysis.",
     "Decoder-only", "BPE"),

    ("EDEN", "EDEN: A 28B Foundation Model for Programmable Gene Insertion",
     "https://www.biorxiv.org/content/10.64898/2026.01.12.699009v1", "2026.01", None, None, "DNA+RNA FM",
     "Develops EDEN, a 28B-parameter foundation model pre-trained on 9.7 trillion biological tokens (DNA+RNA+Protein) for programmable gene insertion, enabling precise genome engineering guided by learned sequence representations.",
     "Decoder-only", "BPE"),

    # === Expression-based FMs ===
    ("BulkRNABert", "BulkRNABert: A Pre-trained Model for Bulk RNA-seq Expression Data",
     "https://www.biorxiv.org/content/10.1101/2024.06.18.599483v2", "2024.06", None, "https://huggingface.co/InstaDeepAI/BulkRNABert", "Expression FM",
     "Presents BulkRNABert, a 6M-parameter encoder model pre-trained on bulk RNA-seq gene expression profiles from TCGA, GTEx, and ENCODE using expression bin tokens for cancer classification and gene expression analysis.",
     "Specialized", "Expression"),

    ("MOJO", "MOJO: A Multi-omics Foundation Model for RNA-seq and Methylation",
     "https://www.biorxiv.org/content/10.1101/2025.06.25.661237v1", "2025.06", None, "https://huggingface.co/InstaDeepAI/MOJO", "Expression FM",
     "Introduces MOJO, a 52.3M-parameter multimodal encoder pre-trained on TCGA RNA-seq expression and DNA methylation data, enabling joint multi-omics analysis for cancer subtyping and biomarker discovery.",
     "Specialized", "Expression"),
]

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
scope_by_name = {
    "RNABert": "specialized_rna_fm",
    "RNAFM": "core_rna_fm",
    "RNAMSM": "specialized_rna_fm",
    "RNA-km": "specialized_rna_fm",
    "RNAErnie": "core_rna_fm",
    "ERNIE-RNA": "core_rna_fm",
    "DGRNA": "core_rna_fm",
    "ChaRNABERT": "core_rna_fm",
    "AIDO.RNA": "core_rna_fm",
    "BiRNA-BERT": "core_rna_fm",
    "RNA-BERTa": "core_rna_fm",
    "RiNALMo": "core_rna_fm",
    "HydraRNA": "core_rna_fm",
    "RNAElectra": "core_rna_fm",
    "CodonBERT": "specialized_rna_fm",
    "CaLM": "specialized_rna_fm",
    "HELM": "core_rna_fm",
    "Helix-mRNA": "core_rna_fm",
    "GenSLM": "specialized_rna_fm",
    "mRNABERT": "core_rna_fm",
    "mRNA-GPT": "core_rna_fm",
    "NUWA": "core_rna_fm",
    "GenerRNA": "core_rna_fm",
    "EVA": "core_rna_fm",
    "Uni-RNA": "core_rna_fm",
    "RNALens": "core_rna_fm",
    "UTR-LM": "specialized_rna_fm",
    "3UTRBERT": "specialized_rna_fm",
    "SpliceBERT": "specialized_rna_fm",
    "RFamLlama": "specialized_rna_fm",
    "PlantRNA-FM": "specialized_rna_fm",
    "LncRNA-BERT": "specialized_rna_fm",
    "G4mer": "specialized_rna_fm",
    "ATOM-1": "specialized_rna_fm",
    "OmniGenome": "specialized_rna_fm",
    "MP-RNA": "specialized_rna_fm",
    "RNA-TorsionBERT": "specialized_rna_fm",
    "StructRFM": "specialized_rna_fm",
    "LoRNA SH": "specialized_rna_fm",
    "Orthrus": "specialized_rna_fm",
    "RNAGenesis": "adapted_derived",
    "CodonMoE": "adapted_derived",
    "mRNA-GPT (full-length)": "adapted_derived",
    "GEMORNA": "task_design",
    "RibonanzaNet": "task_design",
    "GARNET": "task_design",
    "RNAtranslator": "task_design",
    "Evo": "related_nucleotide",
    "LucaOne": "related_nucleotide",
    "BSM": "related_nucleotide",
    "LAMAR": "related_nucleotide",
    "METAGENE-1": "related_nucleotide",
    "Life-Code": "related_nucleotide",
    "Evo 2": "related_nucleotide",
    "OmniNA": "related_nucleotide",
    "EDEN": "related_nucleotide",
    "BulkRNABert": "expression_profile",
    "MOJO": "expression_profile",
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

# Detailed table metadata. The compact paper tuples above carry the common fields;
# this mapping keeps table-only fields in the same generated source of truth.
model_details = {
    "RNABert": {"params": "0.5M", "data": "Rfam seed alignments + ncRNA"},
    "RNAFM": {"params": "100M", "data": "RNAcentral (23M seqs)"},
    "RNAMSM": {"params": "95M", "data": "Rfam families + MSA homologs"},
    "RNA-km": {"params": "152M", "data": "RNAcentral (23M ncRNA seqs)", "token": "SNT + k-mer masking"},
    "RNAErnie": {"params": "105M", "data": "RNAcentral (23M seqs)", "token": "Nucleotide + motif"},
    "ERNIE-RNA": {"params": "86M", "data": "RNAcentral (20.4M seqs)"},
    "DGRNA": {"params": "100M", "data": "MARS (100M RNA seqs)", "arch": "Hybrid (SSM)"},
    "ChaRNABERT": {"params": "8M-650M", "data": "RNAcentral + NCBI (62M seqs)", "token": "Learnable (GBST)"},
    "AIDO.RNA": {"params": "650M / 1.6B", "data": "RNAcentral (42M seqs, ~30B nt)"},
    "BiRNA-BERT": {"params": "117M", "data": "RNAcentral (36M seqs, ~26.4B nt)", "token": "Dual (NUC + BPE)"},
    "RNA-BERTa": {"params": "55.9M", "data": "Public RNA collections (9.76M seqs)"},
    "RiNALMo": {"params": "135M-650M", "data": "RNAcentral (36M ncRNA seqs)"},
    "RNAGenesis": {"params": "1B", "data": "RNAcentral clustered ncRNA", "arch": "Encoder + Diffusion", "token": "Hybrid N-gram"},
    "HydraRNA": {"params": "84M", "data": "28.1M RNAs (ncRNA + coding)", "arch": "Hybrid (SSM+Attention)"},
    "RNAElectra": {"params": "-", "data": "RNAcentral ncRNAs"},
    "CodonBERT": {"params": "110M", "data": "NCBI (10M mRNA CDS)", "token": "Codon-aware"},
    "CaLM": {"params": "86M", "data": "~9M non-redundant CDS", "token": "Codon-level (triplet)"},
    "HELM": {"params": "-", "data": "mRNA coding sequences", "token": "Codon-hierarchical"},
    "Helix-mRNA": {"params": "Compact", "data": "mRNA sequences", "arch": "Hybrid (SSM+Attention)", "token": "SNT + codon markers"},
    "GEMORNA": {"params": "-", "data": "mRNA CDS + UTR", "arch": "Specialized generative", "token": "Codon / nucleotide"},
    "GenSLM": {"params": "2.5B-25B", "data": "110M+ gene seqs + 1.5M SARS-CoV-2 genomes", "token": "Codon-level"},
    "mRNABERT": {"params": "114M", "data": "18M mRNA seqs (NCBI, MG-RAST, GWH, MGnify)", "token": "Dual tokenization"},
    "mRNA-GPT": {"params": "302M", "data": "NCBI CDS (80M bact. + 83M euk. + 2M arch.)", "token": "Codon / nucleotide"},
    "NUWA": {"params": "-", "data": "Multi-species mRNA CDS (115M seqs)", "token": "Codon tokens"},
    "mRNA-GPT (full-length)": {"params": "-", "data": "30M full-length mRNAs (5'UTR+CDS+3'UTR)", "token": "Nucleotide"},
    "CodonMoE": {"params": "-", "data": "DNA FM + RNA adaptation", "arch": "Decoder-only (MoE)", "token": "Codon-aware"},
    "UTR-LM": {"params": "1M", "data": "Ensembl 5'UTR (>214K seqs + synthetic)"},
    "3UTRBERT": {"params": "86M", "data": "GENCODE 3'UTR (20K seqs)", "token": "3-mer"},
    "SpliceBERT": {"params": "20M", "data": "UCSC pre-mRNA (72 species, >2M seqs)"},
    "RFamLlama": {"params": "13-88M", "data": "Rfam (>4,000 families, 0.6M seqs)", "token": "Nucleotide + family"},
    "PlantRNA-FM": {"params": "35M", "data": "OneKP (1,124 plant species transcriptomes)"},
    "LncRNA-BERT": {"params": "-", "data": "GENCODE + RefSeq + NONCODE (536K seqs)", "token": "CSE / k-mer / nt"},
    "G4mer": {"params": "46M", "data": "Human transcriptome (G-quadruplex)"},
    "ATOM-1": {"params": "-", "data": "Chemical mapping sequencing data", "arch": "Encoder-decoder"},
    "RibonanzaNet": {"params": "-", "data": "Eterna + Rfam + PDB (2M seqs)", "arch": "CNN + Attention", "token": "-"},
    "OmniGenome": {"params": "52M / 186M", "data": "OneKP (seq-structure pairs)"},
    "MP-RNA": {"params": "52-186M", "data": "OneKP (seq + structure)"},
    "RNA-TorsionBERT": {"params": "86.9M", "data": "PDB RNA 3D structures"},
    "StructRFM": {"params": "-", "data": "21M seq-structure pairs"},
    "LoRNA SH": {"params": "6.5M", "data": "Full-length transcriptome architecture data", "arch": "Hybrid (StripedHyena)", "token": "Specialized nt + region"},
    "GenerRNA": {"params": "350M", "data": "RNAcentral (16.09M seqs, ~17.4B nt)"},
    "GARNET": {"params": "-", "data": "GTDB (30M seqs, 17B nt, 400K genomes)", "arch": "Decoder + GNN", "token": "Overlapping triplet"},
    "RNAtranslator": {"params": "41.4M", "data": "RNAInter (26M interaction pairs)", "arch": "Encoder-decoder", "token": "Nucleotide + AA"},
    "EVA": {"params": "-", "data": "114M+ full-length RNA seqs", "arch": "Decoder-only (MoE)", "token": "-"},
    "Uni-RNA": {"params": "400M", "data": "RNAcentral + MG-RAST + MGnify (1B seqs)"},
    "RNALens": {"params": "469M", "data": "Multispecies genomic + 5'UTR sequences"},
    "Evo": {"params": "7B", "data": "OpenGenome (2.7M prokaryotic + phage genomes)", "arch": "Hybrid (StripedHyena)"},
    "LucaOne": {"params": "1.8B", "data": "RefSeq + UniProt/PDB (800B tokens)", "token": "SNT / amino acid"},
    "BSM": {"params": "110M / 270M", "data": "RefSeq + web bio-seqs (DNA+RNA+Prot)", "arch": "Decoder-only", "token": "Mixed"},
    "LAMAR": {"params": "150M", "data": "Genome + transcriptome (225 mammals, 15M)"},
    "Orthrus": {"params": "1.3M / 10.1M", "data": "GENCODE + RefSeq + Zoonomia (32M transcripts)", "arch": "Hybrid (SSM)"},
    "METAGENE-1": {"params": "7B", "data": "Wastewater metagenomic DNA/RNA (>1.5T bp)"},
    "Life-Code": {"params": "-", "data": "Multi-omics (DNA/RNA/Prot unified)", "arch": "Hybrid (SSM+Attention)"},
    "Evo 2": {"params": "7B / 40B", "data": "OpenGenome2 (9T nt, 128K genomes)", "arch": "Hybrid (StripedHyena)"},
    "OmniNA": {"params": "-", "data": "91.7M seqs + annotations (1076B bases)"},
    "EDEN": {"params": "28B", "data": "9.7T biological tokens (DNA+RNA+Protein)"},
    "BulkRNABert": {"params": "6.01M", "data": "TCGA + GTEx + ENCODE (RNA-seq expr.)", "arch": "Encoder-only", "token": "Expression bin tokens"},
    "MOJO": {"params": "52.3M", "data": "TCGA (RNA-seq + DNA methylation)", "arch": "Encoder (multimodal)", "token": "Expression bin tokens"},
}

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
lines.append("")
lines.append("## Paper List")
lines.append("")
lines.append("A complete list of model papers and related resources included in this survey. Each entry shows the model/resource name separately from the official paper title. Four classification views are provided below — click to expand/collapse each view.")
lines.append("")
lines.append("> **Date convention**: Dates shown in this section use the official publication or conference month when available; otherwise they use the linked preprint month and are marked `preprint`. Workshop-only entries are marked `workshop`.")
lines.append("")

# Model entries (collapsible wrapper with 4 views inside)
lines.append('<details open>')
lines.append('<summary><b>Models & Related Resources</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")

# --- Classification rules ---
lines.append('<details open>')
lines.append('<summary><b>Classification Rules</b></summary>')
lines.append("")
lines.append("- **Core RNA Foundation Models**: reusable RNA or mRNA sequence backbones pre-trained on raw nucleotide sequences for broad downstream transfer or generation.")
lines.append("- **Specialized RNA Foundation Models**: RNA-specific pre-trained models whose scope is limited to a subtype, species, structural modality, or narrow biological question.")
lines.append("- **Adapted / Derived RNA Models**: models that mainly adapt, extend, fine-tune, or compose existing foundation models / pre-trained components for RNA tasks.")
lines.append("- **Task-specific / Design-oriented RNA Models**: predictors or designers for a specific RNA task, useful to RNA FM research but not primarily general reusable backbones.")
lines.append("- **RNA-related Nucleotide / Multi-omics FMs** and **Expression-profile Related Models**: related resources whose pre-training data are not pure raw RNA sequence.")
lines.append("")
lines.append("</details>")
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
paper_list_start = readme.find("\n## Paper List")
contributing_start = readme.find("\n## Contributing")

next_section = contributing_start

if paper_list_start != -1 and next_section != -1:
    new_readme = readme[:paper_list_start] + output + "\n" + readme[next_section:]
elif next_section != -1:
    new_readme = readme[:next_section] + output + "\n" + readme[next_section:]
else:
    print("ERROR: Could not find insertion point")
    new_readme = readme

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
print("\n\nSUCCESS: Paper list and detailed tables injected into README.md")
