# denovo-bacterial-assembly
de novo assembly of bacterial genome without reference genome 
# De Novo Bacterial Genome Assembly & Quality Evaluation

## Overview
This repository contains an end-to-end bioinformatics pipeline to perform *de novo* assembly of bacterial genome sequences from raw Illumina paired-end reads. It builds De Bruijn graphs, extracts continuous contigs, evaluates quality metrics (N50, Contig counts), and performs gene prediction.

---

## Repository Structure

```text
.
├── scripts/
│   ├── 01_fetch_data.sh       # SRA Download & FASTQ extraction
│   ├── 02_run_fastqc.sh       # Read Quality Control
│   ├── 03_build_megahit.sh    # Builds MEGAHIT Assembler
│   ├── 04_run_megahit.sh      # Executes MEGAHIT Assembly
│   ├── 05_setup_quast.sh      # Installs QUAST Evaluation Tool
│   ├── 06_run_quast.sh        # Generates QUAST Metrics Report
│   ├── 07_setup_prodigal.sh   # Builds Prodigal Gene Finder
│   └── 08_run_prodigal.sh     # Runs ORF and Protein Prediction
├── assemble_genome.py         # Pure Python De Bruijn Assembler
├── evaluate_assembly.py       # Custom fasta metric calculator
└── README.md                  # Project Documentation



Workflow Steps
1.Raw Read Ingestion: Downloading SRA datasets (SRR292770) and extracting FASTQ formats.

2.Quality Control: Running FastQC to evaluate base qualities and adaptor contents.

3.Graph Construction & Assembly: Constructing De Bruijn graphs ($k$-mer representation) to reconstruct contigs.

4.Assembly Evaluation: Computing statistical metrics like $N50$, contig distribution, and total genome coverage.

5.Gene Annotation: Identifying Coding Sequences (CDS) and functional proteins using Prodigal.




Step-by-Step Execution Sequence

Phase 1: Raw Data Retrieval & QC
Step 1: Download Raw Reads

Script: scripts/01_fetch_data.sh

Action: Downloads SRA Toolkit, fetches NCBI dataset SRR292770, and extracts FASTQ sequence files (SRR292770_1.fastq and SRR292770_2.fastq)

./scripts/01_fetch_data.sh



Step 2: Read Quality Control

Script: scripts/02_run_fastqc.sh

Action: Runs FastQC on the raw FASTQ files to assess read quality prior to assembly.

COMMAND 

./scripts/02_run_fastqc.sh


Phase 2: Assembly (Choose Option A or Option B)
Option A: Production Assembly (Recommended)

Step 3A: Install & Build MEGAHIT

Script: scripts/03_build_megahit.sh

Action: Clones and compiles the MEGAHIT assembler executable.

command 

./scripts/03_build_megahit.sh

Step 4A: Run MEGAHIT Assembly

Script: scripts/04_run_megahit.sh

Action: Assembles reads into contigs (megahit_output/final.contigs.fa) using De Bruijn graphs.

command 

./scripts/04_run_megahit.sh

Option B: Pure Python Assembly

Step 3B: Run Python AssemblerScript: assemble_genome.pyAction: Parses local FASTQ files, builds an in-memory De Bruijn graph ($K=31$), constructs contigs, and outputs a lightweight report.

command 


python3 assemble_genome.py


Phase 3: Assembly Evaluation & Metrics

Step 5: Quick Metric Verification
Script: evaluate_assembly.py

Action: Parses megahit_output/final.contigs.fa (or any FASTA file) to immediately compute contig counts, total genome size, min/max length, and N50 statistics.



command 


python3 evaluate_assembly.py megahit_output/final.contigs.fa


Step 6: Install QUAST

Script: scripts/05_setup_quast.sh

Action: Downloads and installs the QUAST evaluation tool


command 

./scripts/05_setup_quast.sh



Step 7: Full QUAST Evaluation

Script: scripts/06_run_quast.sh

Action: Evaluates final.contigs.fa and generates a detailed visual and textual report (quast_output/report.txt)

command 

./scripts/06_run_quast.sh




Phase 4: Downstream Gene Prediction

Step 8: Install Prodigal
Script: scripts/07_setup_prodigal.sh

Action: Downloads and compiles the Prodigal gene calling executable

command 

./scripts/07_setup_prodigal.sh


Step 9: Run Gene Annotation

Script: scripts/08_run_prodigal.sh

Action: Predicts Open Reading Frames (ORFs), generating genes.gff, gene sequences (predicted_genes.fna), and amino acid sequences (predicted_proteins.faa)


command 

./scripts/08_run_prodigal.sh


workflow map



[Step 1] scripts/01_fetch_data.sh
   └──> [Step 2] scripts/02_run_fastqc.sh
           └──> [Step 3] scripts/03_build_megahit.sh
                   └──> [Step 4] scripts/04_run_megahit.sh
                           └──> [Step 5] python3 evaluate_assembly.py
                                   └──> [Step 6] scripts/05_setup_quast.sh
                                           └──> [Step 7] scripts/06_run_quast.sh
                                                   └──> [Step 8] scripts/07_setup_prodigal.sh
                                                           └──> [Step 9] scripts/08_run_prodigal.sh

 
