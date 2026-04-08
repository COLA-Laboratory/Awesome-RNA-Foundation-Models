"""Generate a bullet-list paper index section for the README, with abstracts.
Three classification views: by RNA type, by architecture, by tokenization strategy."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from collections import OrderedDict

# Fields: (name, title, url, year_month, github_url, hf_url, category, abstract, architecture, tokenization)
papers = [
    # === ncRNA FMs ===
    ("RNABert", "Informative RNA-base embedding for RNA structural alignment and clustering by a representation learning framework",
     "https://doi.org/10.1093/nargab/lqac012", "2022.02", "https://github.com/mana438/RNABERT", None, "ncRNA FM",
     "Proposes RNABERT, a BERT-based model pre-trained on Rfam seed alignments using masked language modeling to learn informative RNA-base embeddings for structural alignment and clustering of ncRNAs.",
     "Encoder-only", "SNT"),

    ("RNAFM", "Interpretable RNA Foundation Model from Unannotated Data for Highly Accurate RNA Structure and Function Predictions",
     "https://arxiv.org/abs/2204.00300", "2022.08", None, "https://huggingface.co/multimolecule/rnafm", "ncRNA FM",
     "Presents RNA-FM, a foundation model pre-trained on 23 million non-coding RNA sequences from RNAcentral, achieving state-of-the-art performance on RNA secondary structure prediction, 3D closeness prediction, and functional annotation tasks.",
     "Encoder-only", "SNT"),

    ("RNAMSM", "Multiple sequence-alignment-based RNA language model and its application to structural inference",
     "https://doi.org/10.1093/nar/gkad1031", "2023.12", "https://github.com/yikunpku/RNA-MSM", None, "ncRNA FM",
     "Introduces RNA-MSM, an unsupervised RNA language model that leverages multiple sequence alignments (MSAs) from homologous RNA families to capture evolutionary and co-evolutionary information for improved structural inference.",
     "Encoder-only", "SNT"),

    ("RNA-km", "RNA-km: a tool for predicting RNA sequence properties using k-mer frequency features",
     "https://doi.org/10.1101/2024.01.27.577533", "2024.01", "https://github.com/gongtiansu/RNA-km", None, "ncRNA FM",
     "Proposes RNA-km, a pre-trained encoder model that uses k-mer frequency features from 23M RNAcentral sequences to predict diverse RNA sequence properties including subcellular localization and modification sites.",
     "Encoder-only", "K-mer"),

    ("RNAErnie", "RNAErnie: An RNA language model with structure-enhanced representations",
     "https://www.nature.com/articles/s42256-024-00836-4", "2024.05", None, "https://huggingface.co/LLM-EDA/RNAErnie", "ncRNA FM",
     "Presents RNAErnie, a pre-trained RNA language model that integrates RNA sequence, secondary structure, and base-pairing information through a multi-level masking strategy, achieving superior performance across RNA downstream tasks.",
     "Encoder-only", "SNT"),

    ("ERNIE-RNA", "ERNIE-RNA: An RNA Language Model with Structure-enhanced Representations",
     "https://doi.org/10.1101/2024.03.17.585376", "2024.10", None, "https://huggingface.co/multimolecule/ernierna-ss", "ncRNA FM",
     "Develops ERNIE-RNA with structure-enhanced pre-training that jointly models RNA sequences and secondary structures, achieving improvements in RNA contact prediction, distance prediction, and secondary structure prediction.",
     "Encoder-only", "SNT"),

    ("DGRNA", "DGRNA: a long-context RNA foundation model with bidirectional Mamba2",
     "https://doi.org/10.1101/2024.10.31.621427", "2024.10", None, None, "ncRNA FM",
     "Introduces DGRNA, a long-context RNA foundation model based on bidirectional Mamba2 architecture, enabling efficient processing of long RNA sequences up to 100K nucleotides with linear computational complexity.",
     "Hybrid/SSM", "SNT"),

    ("ChaRNABERT", "ChaRNABERT: A pre-trained RNA language model with learnable tokenization",
     "https://arxiv.org/abs/2411.11808", "2024.11", None, None, "ncRNA FM",
     "Proposes ChaRNABERT with Gradient-based Subword Tokenization (GBST) that learns data-driven tokenization during pre-training, outperforming fixed tokenization approaches on RNA structure and function prediction tasks.",
     "Encoder-only", "Learnable"),

    ("AIDO.RNA", "AIDO.RNA: A Scalable RNA Foundation Model",
     "https://doi.org/10.1101/2024.11.28.625345", "2024.11", None, "https://huggingface.co/genbio-ai/AIDO.RNA-1.6B", "ncRNA FM",
     "Presents AIDO.RNA, a scalable RNA foundation model with up to 1.6B parameters pre-trained on 42M non-coding RNA sequences (~30B nucleotides), demonstrating strong generalization across diverse RNA tasks.",
     "Encoder-only", "SNT"),

    ("BiRNA-BERT", "BiRNA-BERT: An Efficient RNA Language Model with Adaptive Dual Tokenization",
     "https://doi.org/10.1101/2024.07.02.601703", "2025.08", "https://github.com/buetnlpbio/BiRNA-BERT", None, "ncRNA FM",
     "Introduces BiRNA-BERT with a dual tokenization strategy combining single-nucleotide and BPE tokenization, enabling efficient processing of long RNA sequences while maintaining fine-grained nucleotide-level representations.",
     "Encoder-only", "Learnable"),

    ("RNA-BERTa", "DLRNA-BERTa: A Transformer for RNA-Drug Binding Affinity Prediction",
     "https://www.biorxiv.org/content/10.1101/2025.09.05.674445v1", "2025.09", None, "https://huggingface.co/IlPakoZ/RNA-BERTa9700", "ncRNA FM",
     "Develops RNA-BERTa, a RoBERTa-based model pre-trained on 9.76M RNA sequences for learning general RNA representations, applied to RNA-drug binding affinity prediction with downstream fine-tuning.",
     "Encoder-only", "BPE"),

    ("RiNALMo", "RiNALMo: General-Purpose RNA Language Models Can Generalize Well on Structure Prediction Tasks",
     "https://arxiv.org/abs/2403.00043", "2025.07", "https://github.com/lbcb-sci/RiNALMo", None, "ncRNA FM",
     "Presents RiNALMo, a general-purpose RNA language model (up to 650M parameters) pre-trained on 36M ncRNA sequences, demonstrating that large-scale RNA LMs can generalize effectively to secondary and tertiary structure prediction.",
     "Encoder-only", "SNT"),

    ("RNAGenesis", "RNAGenesis: A Generative RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2024.12.30.630826v2", "2024.12", None, "https://huggingface.co/Zaixi/RNAGenesis", "ncRNA FM",
     "Proposes RNAGenesis, a 1B-parameter generative RNA foundation model combining encoder representations with diffusion-based generation, enabling both RNA understanding and de novo RNA sequence design.",
     "Specialized", "SNT"),

    ("HydraRNA", "HydraRNA: An Efficient RNA Foundation Model via Hybrid SSM and Attention",
     "https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03853-7", "2025.03", "https://github.com/GuipengLi/HydraRNA", None, "ncRNA FM",
     "Introduces HydraRNA, an efficient RNA foundation model using a hybrid architecture combining state space models (SSM) and attention mechanisms, achieving competitive performance with significantly reduced computational cost.",
     "Hybrid/SSM", "SNT"),

    ("RNAElectra", "RNAElectra: An ELECTRA-style RNA Foundation Model",
     "https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1.full", "2026.03", None, None, "ncRNA FM",
     "Proposes RNAElectra, applying the ELECTRA-style replaced token detection pre-training objective to RNA sequences, offering more sample-efficient pre-training compared to masked language modeling approaches.",
     "Encoder-only", "SNT"),

    # === mRNA/CDS FMs ===
    ("CodonBERT", "CodonBERT: Large Language Models for mRNA Unimodal and Multimodal Molecular Learning",
     "https://www.biorxiv.org/content/10.1101/2023.09.09.556981v1", "2023.09", "https://github.com/Sanofi-Public/CodonBERT", None, "mRNA/CDS FM",
     "Presents CodonBERT, a BERT-based model pre-trained on 10M mRNA coding sequences with codon-aware tokenization, enabling both unimodal RNA and multimodal RNA-protein molecular learning.",
     "Encoder-only", "Codon"),

    ("CaLM", "CaLM: Codon Adaptation Language Model for mRNA Design",
     "https://www.nature.com/articles/s42256-024-00791-0", "2024.02", "https://github.com/oxpig/CaLM", None, "mRNA/CDS FM",
     "Introduces CaLM, a codon-level language model trained on ~9M non-redundant coding sequences for predicting and optimizing codon usage, enabling rational mRNA therapeutic design with improved translation efficiency.",
     "Encoder-only", "Codon"),

    ("HELM", "HELM: Hierarchical Encoding for mRNA Language Modeling",
     "https://arxiv.org/abs/2410.12459", "2025.01", None, None, "mRNA/CDS FM",
     "Proposes HELM, a hierarchical encoding approach for mRNA language modeling that captures both nucleotide-level and codon-level information through a multi-scale architecture for improved mRNA property prediction.",
     "Encoder-Decoder", "Codon"),

    ("Helix-mRNA", "Helix-mRNA: A Hybrid SSM-Attention Model for mRNA",
     "https://arxiv.org/abs/2502.13785", "2025.02", None, "https://huggingface.co/helical-ai/helix-mRNA", "mRNA/CDS FM",
     "Presents Helix-mRNA, a compact hybrid model combining Mamba2 state space layers with attention mechanisms for efficient mRNA sequence modeling, targeting mRNA stability and translation efficiency prediction.",
     "Hybrid/SSM", "Codon"),

    ("GEMORNA", "GEMORNA: Generative mRNA Design via Codon and UTR Optimization",
     "https://www.science.org/doi/10.1126/science.adr8470", "2025.05", "https://github.com/RainaBio/GEMORNA", None, "mRNA/CDS FM",
     "Presents GEMORNA, a generative model for end-to-end mRNA design that jointly optimizes coding sequences and UTR regions, enabling the design of mRNAs with enhanced stability, translation efficiency, and immunogenicity profiles.",
     "Encoder-Decoder", "Codon"),

    ("GenSLM", "GenSLMs: Genome-scale Language Models Reveal SARS-CoV-2 Evolutionary Dynamics",
     "https://doi.org/10.1177/10943420231201154", "2023.01", None, None, "mRNA/CDS FM",
     "Develops GenSLMs (up to 25B parameters), genome-scale language models trained on codon-level gene sequences from 110M+ genes and 1.5M SARS-CoV-2 genomes, revealing evolutionary dynamics and enabling variant prediction.",
     "Decoder-only", "Codon"),

    ("mRNABERT", "mRNABERT: A Pre-trained Language Model for mRNA Sequences",
     "https://www.nature.com/articles/s41467-025-65340-8", "2025.11", None, "https://huggingface.co/Taykhoom/mRNABERT-no-flashattention", "mRNA/CDS FM",
     "Introduces mRNABERT, a 114M-parameter BERT model pre-trained on 18M mRNA sequences from diverse databases using dual tokenization, achieving state-of-the-art on mRNA stability, translation efficiency, and expression prediction.",
     "Encoder-only", "Learnable"),

    ("mRNA-GPT", "mRNA-GPT: An Autoregressive mRNA Foundation Model across Three Domains of Life",
     "https://www.biorxiv.org/content/10.64898/2025.12.22.695962v1", "2025.12", "https://github.com/ZHymLumine/mRNA-GPT/", None, "mRNA/CDS FM",
     "Presents mRNA-GPT, a 302M-parameter autoregressive model pre-trained on 80M bacterial, 83M eukaryotic, and 2M archaeal CDS sequences with codon/nucleotide tokenization for cross-species mRNA understanding and generation.",
     "Decoder-only", "Codon"),

    ("NUWA", "NUWA: A Codon Language Model for mRNA Coding Sequences",
     "https://www.biorxiv.org/content/10.1101/2025.11.01.686058v3", "2026.02", "https://github.com/zysxmu/NUWA", None, "mRNA/CDS FM",
     "Proposes NUWA, a codon-level language model pre-trained on 115M multi-species mRNA coding sequences, learning codon usage patterns for downstream tasks including codon optimization and mRNA expression prediction.",
     "Encoder-only", "Codon"),

    ("mRNA-GPT (full-length)", "mRNA-GPT: Full-Length mRNA Design via Autoregressive Generation with PPO",
     "https://www.biorxiv.org/content/10.64898/2026.03.31.715707v1", "2026.03", None, None, "mRNA/CDS FM",
     "Extends mRNA-GPT to full-length mRNA design (5'UTR+CDS+3'UTR) using autoregressive generation with PPO-based reinforcement learning to optimize translation efficiency and stability of generated mRNA sequences.",
     "Decoder-only", "Codon"),

    ("CodonMoE", "CodonMoE: Adapting DNA Language Models for RNA via Mixture-of-Experts",
     "https://openreview.net/forum?id=TOUrnb1EaG", "2026.01", None, None, "mRNA/CDS FM",
     "Proposes CodonMoE, a parameter-efficient approach to adapt pre-trained DNA foundation models for RNA tasks using Mixture-of-Experts adapters with codon-aware routing for improved mRNA property prediction.",
     "Specialized", "Codon"),

    # === UTR FMs ===
    ("UTR-LM", "UTR-LM: A 5' UTR Language Model for Predicting Translation Efficiency",
     "https://www.nature.com/articles/s42256-024-00823-9", "2024.04", None, "https://huggingface.co/multimolecule/utrlm-te_el", "UTR FM",
     "Introduces UTR-LM, a language model specifically pre-trained on 5' UTR sequences from Ensembl, predicting mean ribosome loading (translation efficiency) and expression level from UTR sequences alone.",
     "Encoder-only", "SNT"),

    ("3UTRBert", "3UTRBERT: Pre-trained Language Model for 3' UTR Sequences",
     "https://doi.org/10.1101/2023.09.08.556883", "2024.07", "https://github.com/yangyn533/3UTRBERT", None, "UTR FM",
     "Presents 3UTRBERT, a BERT model pre-trained on GENCODE 3'UTR sequences using 3-mer tokenization, capturing regulatory motifs for predicting mRNA stability, polyadenylation, and subcellular localization.",
     "Encoder-only", "K-mer"),

    # === Specific RNA FMs ===
    ("SpliceBERT", "SpliceBERT: A Pre-trained Model for Self-supervised Learning of Pre-mRNA Splicing",
     "https://doi.org/10.1093/bib/bbae163", "2023.01", "https://github.com/chenkenbio/SpliceBERT", None, "Specific RNA FM",
     "Develops SpliceBERT, a 20M-parameter BERT model pre-trained on pre-mRNA sequences from 72 vertebrate species for self-supervised learning of splicing patterns, improving splice site prediction and branchpoint detection.",
     "Encoder-only", "SNT"),

    ("RFamLlama", "RFamLlama: Conditional RNA Generation by RNA Family",
     "https://openreview.net/forum?id=dXnQedxEJD", "2024.08", None, "https://huggingface.co/jinyuan22/RFamLlama-base", "Specific RNA FM",
     "Proposes RFamLlama, a Llama-based autoregressive model for conditional RNA sequence generation conditioned on RNA family labels, generating novel functional ncRNA sequences belonging to over 4,000 Rfam families.",
     "Decoder-only", "SNT"),

    ("PlantRNA-FM", "PlantRNA-FM: A Plant RNA Foundation Model from Multi-species Transcriptomes",
     "https://www.nature.com/articles/s42256-024-00946-z", "2024.12", None, "https://huggingface.co/yangheng/PlantRNA-FM", "Specific RNA FM",
     "Presents PlantRNA-FM, a foundation model pre-trained on transcriptomes from 1,124 plant species (OneKP dataset), capturing plant-specific RNA regulatory patterns for gene expression prediction and functional annotation.",
     "Encoder-only", "SNT"),

    ("LncRNA-BERT", "LncRNA-BERT: A BERT-based Model for Long Non-coding RNA Classification",
     "https://www.biorxiv.org/content/10.1101/2025.01.09.632168v1", "2025.01", "https://github.com/luukromeijn/lncRNA-Py", None, "Specific RNA FM",
     "Introduces LncRNA-BERT, a BERT model pre-trained on 536K long non-coding RNA sequences from GENCODE, RefSeq, and NONCODE for lncRNA classification, subcellular localization, and functional prediction.",
     "Encoder-only", "K-mer"),

    ("G4mer", "G4mer: An Interpretable Transformer for G-quadruplex Prediction in the Transcriptome",
     "https://www.nature.com/articles/s41467-025-65020-7", "2025.12", None, "https://huggingface.co/Biociphers/g4mer", "Specific RNA FM",
     "Develops G4mer, a 46M-parameter interpretable transformer model for predicting RNA G-quadruplex structures in the human transcriptome, providing attention-based interpretability for understanding G4-mediated regulation.",
     "Encoder-only", "SNT"),

    # === Structure-aware RNA FMs ===
    ("ATOM-1", "ATOM-1: Augmented Transformer with Structure-aware Chemical Mapping",
     "https://doi.org/10.1101/2023.12.13.571579", "2023.12", None, None, "Structure-aware FM",
     "Proposes ATOM-1, an augmented transformer pre-trained on chemical mapping (SHAPE, DMS) sequencing data, learning structure-aware RNA representations that encode both sequence and experimentally-derived structural information.",
     "Encoder-Decoder", "SNT"),

    ("Ribonanza", "RibonanzaNet: Deep Learning for RNA Chemical Mapping Prediction",
     "https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1", "2024.02", "https://github.com/Shujun-He/RibonanzaNet", None, "Structure-aware FM",
     "Presents RibonanzaNet, a deep neural network trained on 2M RNA sequences with experimental chemical mapping data from Eterna, Rfam, and PDB, predicting RNA chemical reactivity profiles for structure determination.",
     "Specialized", "SNT"),

    ("OmniGenome", "OmniGenome: Aligning RNA Sequences with Secondary Structures",
     "https://arxiv.org/abs/2407.11242", "2024.07", None, "https://huggingface.co/yangheng/OmniGenome-186M", "Structure-aware FM",
     "Introduces OmniGenome (52M/186M parameters), a structure-aware RNA model pre-trained on sequence-structure pairs from the OneKP dataset, aligning RNA sequences with their secondary structures for improved downstream predictions.",
     "Encoder-only", "SNT"),

    ("MP-RNA", "MP-RNA: Multi-Purpose RNA Foundation Model with Structure Awareness",
     "https://aclanthology.org/2024.findings-emnlp.304/", "2024.11", None, "https://huggingface.co/yangheng/MP-RNA", "Structure-aware FM",
     "Develops MP-RNA, a multi-purpose RNA foundation model that integrates sequence and structure information through joint pre-training on the OneKP dataset, supporting diverse RNA tasks within a unified framework.",
     "Encoder-only", "SNT"),

    ("RNA-TorsionBERT", "RNA-TorsionBERT: Predicting RNA Backbone Torsion Angles",
     "https://doi.org/10.1093/bioinformatics/btaf004", "2025.01", None, "https://huggingface.co/sayby/rna_torsionBERT", "Structure-aware FM",
     "Proposes RNA-TorsionBERT, a BERT model pre-trained on PDB RNA 3D structures to predict backbone torsion angles directly from RNA sequences, enabling rapid assessment of RNA 3D structural properties.",
     "Encoder-only", "SNT"),

    ("StructRFM", "StructRFM: Structure-guided RNA Foundation Model",
     "https://www.biorxiv.org/content/10.1101/2025.08.06.668731v1", "2025.08", "https://github.com/heqin-zhu/structRFM", None, "Structure-aware FM",
     "Presents StructRFM, a structure-guided RNA foundation model pre-trained on 21M sequence-structure pairs, integrating predicted secondary structure information during pre-training for enhanced RNA representation learning.",
     "Encoder-only", "SNT"),

    # === Generative FMs ===
    ("LoRNA", "LoRNA: A Long-read RNA Foundation Model",
     "https://doi.org/10.1101/2024.08.26.609813", "2024.08", None, None, "Generative FM",
     "Introduces LoRNA, a foundation model designed for long-read RNA sequencing data, pre-trained on ~100M IsoSeq long reads (7B tokens) with specialized nucleotide and region tokenization for transcript-level analysis.",
     "Decoder-only", "SNT"),

    ("GenerRNA", "GenerRNA: A Generative Pre-trained Autoregressive RNA Language Model",
     "https://doi.org/10.1371/journal.pone.0310814", "2024.10", None, "https://huggingface.co/pfnet/GenerRNA", "Generative FM",
     "Presents GenerRNA, a 350M-parameter autoregressive language model pre-trained on 16M RNAcentral sequences (~17.4B nucleotides) using BPE tokenization for de novo RNA sequence generation with controllable properties.",
     "Decoder-only", "BPE"),

    ("GARNET", "GARNET: A Generative RNA Design Model from Microbial Genomes",
     "https://www.nature.com/articles/s41467-024-54812-y", "2024.12", "https://github.com/Doudna-lab/GARNET_DL", None, "Generative FM",
     "Develops GARNET, a generative model combining a decoder with a GNN, trained on 30M microbial genome sequences (17B nucleotides) from GTDB for designing novel functional RNA sequences with desired structural properties.",
     "Specialized", "SNT"),

    ("RNAtranslator", "RNAtranslator: Protein-conditioned RNA Sequence Generation",
     "https://doi.org/10.1371/journal.pcbi.1013541", "2025.03", None, "https://huggingface.co/SobhanShukueian/rnatranslator", "Generative FM",
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
     "https://www.science.org/doi/10.1126/science.ado9336", "2024.02", "https://github.com/evo-design/evo", None, "DNA+RNA FM",
     "Presents Evo, a 7B-parameter genomic foundation model using StripedHyena architecture, pre-trained on 2.7M prokaryotic and phage genomes at single-nucleotide resolution, enabling sequence modeling and design from molecular to genome scale.",
     "Hybrid/SSM", "SNT"),

    ("LucaOne", "LucaOne: A Unified Foundation Model for DNA, RNA and Protein",
     "https://www.nature.com/articles/s42256-025-01044-4", "2024.05", "https://github.com/LucaOne/LucaOne", None, "DNA+RNA FM",
     "Introduces LucaOne, a 1.8B-parameter unified model pre-trained on 800B tokens from RefSeq, UniProt, and PDB, jointly modeling DNA, RNA, and protein sequences for cross-modal biological sequence understanding.",
     "Encoder-only", "SNT"),

    ("BSM", "BSM: Biological Sequence Model for Mixed-modal Pretraining",
     "https://arxiv.org/abs/2410.11499", "2024.10", None, None, "DNA+RNA FM",
     "Proposes BSM (110M/270M parameters), a biological sequence model with mixed-modal pre-training on DNA, RNA, and protein sequences from RefSeq and web-collected biological data for unified sequence representation.",
     "Specialized", "SNT"),

    ("LAMAR", "LAMAR: A Language Model for Mammalian and Viral Genomes and Transcriptomes",
     "https://www.biorxiv.org/content/10.1101/2024.10.12.617732v1", "2024.10", "https://github.com/zhw-e8/LAMAR", None, "DNA+RNA FM",
     "Develops LAMAR, a 150M-parameter language model pre-trained on genomes and transcriptomes from 225 mammalian species (15M sequences), capturing mammalian-specific and viral genomic patterns for RNA and DNA tasks.",
     "Encoder-only", "BPE"),

    ("Orthrus", "Orthrus: Contrastive Learning of Transcript Isoforms and Orthologs via Mamba",
     "https://www.biorxiv.org/content/10.1101/2024.10.10.617658v3", "2024.10", None, "https://huggingface.co/quietflamingo/orthrus-large-4-track", "DNA+RNA FM",
     "Introduces Orthrus, a Mamba-based model using contrastive learning on 32M transcript sequences from GENCODE, RefSeq, and Zoonomia to learn representations of transcript isoforms and cross-species orthologs.",
     "Hybrid/SSM", "SNT"),

    ("METAGENE-1", "METAGENE-1: A 7B Metagenomic Foundation Model for DNA and RNA",
     "https://arxiv.org/abs/2501.02045", "2025.01", None, "https://huggingface.co/metagene-ai/METAGENE-1", "DNA+RNA FM",
     "Presents METAGENE-1, a 7B-parameter metagenomic foundation model pre-trained on >1.5 trillion base pairs of wastewater metagenomic DNA and RNA sequences using BPE tokenization for pathogen detection and biosurveillance.",
     "Decoder-only", "BPE"),

    ("Life-Code", "Life-Code: A Unified Foundation Model via Central Dogma",
     "https://arxiv.org/abs/2502.07299", "2025.02", None, None, "DNA+RNA FM",
     "Proposes Life-Code, a unified foundation model that jointly models DNA, RNA, and protein following the central dogma of molecular biology, using codon-level tokenization to capture cross-modal biological relationships.",
     "Hybrid/SSM", "Codon"),

    ("Evo 2", "Genome Modeling and Design Across All Domains of Life with Evo 2",
     "https://www.nature.com/articles/s41586-026-10176-5", "2026.02", "https://github.com/ArcInstitute/evo2", None, "DNA+RNA FM",
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
     "https://arxiv.org/abs/2406.10391", "2024.06", "https://github.com/terry-r123/RNABenchmark", None,
     "Introduces BEACON, a comprehensive benchmark covering 13 RNA tasks across structural, functional, and engineering categories for systematic evaluation of RNA language models."),

    ("BEND", "BEND: Benchmarking DNA Language Models on Biologically Meaningful Tasks",
     "https://arxiv.org/abs/2311.12570", "2024.01", "https://github.com/frederikkemarin/BEND", None,
     "Proposes BEND, a benchmark of biologically meaningful tasks for evaluating DNA language models, covering gene regulation, chromatin accessibility, and conservation prediction."),

    ("GUE", "DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genome",
     "https://arxiv.org/abs/2306.15006", "2023.06", None, None,
     "Introduces DNABERT-2 along with GUE (Genome Understanding Evaluation), a benchmark of 36 datasets across 9 task categories for evaluating genome foundation models."),

    ("RNA LLM Folding", "Comprehensive Benchmarking of LLMs for RNA Secondary Structure Prediction",
     "https://arxiv.org/abs/2410.16212", "2024.10", "https://github.com/sinc-lab/rna-llm-folding", None,
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

    ("NABench", "NABench: Nucleic Acid Fitness Prediction Benchmark",
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
     "https://arxiv.org/abs/2503.04490", "2026.03", None, None,
     "Comprehensive survey of large language models applied to bioinformatics including DNA, RNA, and protein domains, covering model architectures, training paradigms, and applications across biological sequences."),
]

# ============================================================
# Helpers
# ============================================================
def format_entry(name, title, paper_url, year_month, github_url, hf_url, abstract):
    """Format a paper entry as a bullet list item with badges."""
    line = f'- [{title}]({paper_url}) ({year_month})'
    line += f' [![abs](https://img.shields.io/badge/abs-{year_month}-b31b1b.svg)]({paper_url})'
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


def render_view(groups, label_map):
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

# View 1: By RNA Type (current categories)
rna_type_labels = {
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
rna_type_order = list(rna_type_labels.keys())

# View 2: By Architecture
arch_labels = {
    "Encoder-only": "Encoder-only (BERT-family)",
    "Decoder-only": "Decoder-only (GPT-family)",
    "Encoder-Decoder": "Encoder-Decoder (Seq2Seq)",
    "Hybrid/SSM": "Hybrid / SSM (Mamba, StripedHyena)",
    "Specialized": "Specialized (Diffusion, MoE, GNN, Multimodal)",
}
arch_order = ["Encoder-only", "Decoder-only", "Encoder-Decoder", "Hybrid/SSM", "Specialized"]

# View 3: By Tokenization Strategy
tok_labels = {
    "SNT": "Single Nucleotide Token (SNT)",
    "Codon": "Codon-level Tokenization",
    "K-mer": "K-mer Tokenization",
    "BPE": "Byte Pair Encoding (BPE)",
    "Learnable": "Learnable / Adaptive Tokenization",
    "Expression": "Expression-level Tokenization",
}
tok_order = ["SNT", "Codon", "K-mer", "BPE", "Learnable", "Expression"]

# ============================================================
# Build output
# ============================================================
lines = []
lines.append("")
lines.append("## Paper List")
lines.append("")
lines.append("A complete list of all papers included in this survey. Three classification views are provided below — click to expand/collapse each view.")
lines.append("")

lines.append("### Foundation Models")
lines.append("")

# --- View 1: By RNA Type ---
rna_groups = group_papers(papers, 6, rna_type_labels, rna_type_order)
lines.append('<details open>')
lines.append('<summary><b>View 1: Classified by RNA Type</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(rna_groups, rna_type_labels))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# --- View 2: By Architecture ---
arch_groups = group_papers(papers, 8, arch_labels, arch_order)
lines.append('<details>')
lines.append('<summary><b>View 2: Classified by Architecture</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(arch_groups, arch_labels))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# --- View 3: By Tokenization ---
tok_groups = group_papers(papers, 9, tok_labels, tok_order)
lines.append('<details>')
lines.append('<summary><b>View 3: Classified by Tokenization Strategy</b></summary>')
lines.append("")
lines.append("<blockquote>")
lines.append("")
lines.extend(render_view(tok_groups, tok_labels))
lines.append("</blockquote>")
lines.append("")
lines.append("</details>")
lines.append("")

# Benchmarks
lines.append("### Benchmarks & Evaluations")
lines.append("")
benchmarks.sort(key=lambda x: x[3])
for name, title, url, ym, gh, hf, abstract in benchmarks:
    lines.append(format_entry(name, title, url, ym, gh, hf, abstract))
lines.append("")

# Surveys
lines.append("### Surveys & Reviews")
lines.append("")
surveys.sort(key=lambda x: x[3])
for name, title, url, ym, gh, hf, abstract in surveys:
    lines.append(format_entry(name, title, url, ym, gh, hf, abstract))
lines.append("")

output = "\n".join(lines)
print(output)

# Now inject into README: replace existing Paper List or insert before Contributing
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Find and replace existing Paper List section (stop at Model Tables, or Contributing)
paper_list_start = readme.find("\n## Paper List")
model_tables_start = readme.find("\n## Model Tables")
contributing_start = readme.find("\n## Contributing")

# Replace Paper List up to the next major section
next_section = model_tables_start if model_tables_start != -1 else contributing_start

if paper_list_start != -1 and next_section != -1:
    new_readme = readme[:paper_list_start] + output + "\n" + readme[next_section:]
elif next_section != -1:
    new_readme = readme[:next_section] + output + "\n" + readme[next_section:]
else:
    print("ERROR: Could not find insertion point")
    new_readme = readme

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
print("\n\nSUCCESS: Paper list injected into README.md")
