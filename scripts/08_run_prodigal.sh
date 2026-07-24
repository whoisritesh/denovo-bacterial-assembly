#!/usr/bin/env bash
set -e

echo "[*] Predicting Open Reading Frames (ORFs) with Prodigal..."
./Prodigal-2.6.3/prodigal \
  -i megahit_output/final.contigs.fa \
  -a predicted_proteins.faa \
  -d predicted_genes.fna \
  -o genes.gff \
  -f gff

echo "=== Annotation Summary ==="
echo -n "Total CDS Predicted: "
grep -c $'\tCDS\t' genes.gff
