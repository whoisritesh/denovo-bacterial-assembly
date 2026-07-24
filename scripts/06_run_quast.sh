#!/usr/bin/env bash
set -e

echo "[*] Running QUAST evaluation..."
quast.py megahit_output/final.contigs.fa -o quast_output --min-contig 200

echo "=== Summary Report ==="
cat quast_output/report.txt
