#!/usr/bin/env bash
set -e

echo "[*] Downloading SRA Toolkit..."
wget -q https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sra-toolkit.current-ubuntu64.tar.gz
tar -xzf sra-toolkit.current-ubuntu64.tar.gz
export PATH=$PATH:$(pwd)/sratoolkit.3.0.0-ubuntu64/bin # adapt version if needed

echo "[*] Downloading SRA dataset SRR292770..."
prefetch SRR292770

echo "[*] Converting SRA to FASTQ..."
fastq-dump --split-files SRR292770
echo "[+] FASTQ extraction complete."
