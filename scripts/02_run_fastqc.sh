#!/usr/bin/env bash
set -e

echo "[*] Running FastQC on downloaded reads..."
mkdir -p fastqc_out
fastqc SRR292770_1.fastq SRR292770_2.fastq -o fastqc_out/
echo "[+] Quality control complete. Results in fastqc_out/"
