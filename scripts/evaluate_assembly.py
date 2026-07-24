#!/usr/bin/env python3
import sys

def evaluate_fasta(fasta_file):
    lengths = []
    current_len = 0
    
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if current_len > 0:
                    lengths.append(current_len)
                current_len = 0
            else:
                current_len += len(line.strip())
        if current_len > 0:
            lengths.append(current_len)

    if not lengths:
        print("[-] No sequences found in input file.")
        return

    lengths.sort(reverse=True)
    total_bp = sum(lengths)
    count = len(lengths)

    cumsum = 0
    n50 = 0
    for l in lengths:
        cumsum += l
        if cumsum >= total_bp / 2.0:
            n50 = l
            break

    print("=== Assembly Summary Metrics ===")
    print(f"Total Contigs  : {count}")
    print(f"Total Genome   : {total_bp:,} bp")
    print(f"Max Contig Len : {lengths[0]:,} bp")
    print(f"Min Contig Len : {lengths[-1]:,} bp")
    print(f"Calculated N50 : {n50:,} bp")

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "megahit_output/final.contigs.fa"
    evaluate_fasta(filepath)
