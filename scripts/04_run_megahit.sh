#!/usr/bin/env bash
set -e

echo "[*] Cleaning old assembly directories if present..."
rm -rf megahit_output

echo "[*] Executing MEGAHIT Assembly..."
./megahit/build/megahit \
  -1 SRR292770_1.fastq \
  -2 SRR292770_2.fastq \
  -o megahit_output \
  -t 8

echo "[+] De novo assembly complete. Results in megahit_output/final.contigs.fa"
