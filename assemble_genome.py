#!/usr/bin/env python3
import os
import glob

def load_fastq_reads(directory):
    """Loads forward and reverse FASTQ reads from the specified directory."""
    reads = []
    fastq_files = glob.glob(os.path.join(directory, "*.fastq"))
    for f_path in fastq_files:
        print(f"[*] Reading file: {os.path.basename(f_path)}")
        with open(f_path, 'r') as f:
            lines = f.readlines()
            for i in range(1, len(lines), 4):
                seq = lines[i].strip()
                reads.append(seq)
    return reads

def build_de_bruijn_graph(reads, k):
    """Builds a De Bruijn graph from reads using k-mers."""
    graph = {}
    for read in reads:
        if len(read) < k:
            continue
        for i in range(len(read) - k + 1):
            kmer1 = read[i:i+k-1]
            kmer2 = read[i+1:i+k]
            if kmer1 not in graph:
                graph[kmer1] = []
            graph[kmer1].append(kmer2)
    return graph

def generate_contigs(graph, k):
    """Simple path traversal to extract contigs from the De Bruijn graph."""
    contigs = []
    visited_edges = set()
    
    for node in graph:
        for neighbor in graph[node]:
            edge = (node, neighbor)
            if edge not in visited_edges:
                curr_path = [node, neighbor]
                visited_edges.add(edge)
                curr = neighbor
                
                while curr in graph and len(graph[curr]) == 1:
                    nxt = graph[curr][0]
                    next_edge = (curr, nxt)
                    if next_edge in visited_edges:
                        break
                    visited_edges.add(next_edge)
                    curr_path.append(nxt)
                    curr = nxt
                
                contig_str = curr_path[0]
                for p in curr_path[1:]:
                    contig_str += p[-1]
                contigs.append(contig_str)
                
    return contigs

def calculate_quast_metrics(contigs):
    """Calculates standard assembly metrics (Total length, Contig count, N50)."""
    if not contigs:
        return {"Total Length": 0, "Contig Count": 0, "Max Contig": 0, "N50": 0}
        
    lengths = sorted([len(c) for c in contigs], reverse=True)
    total_length = sum(lengths)
    contig_count = len(lengths)
    max_contig = lengths[0]
    
    half_total = total_length / 2.0
    running_sum = 0
    n50 = 0
    for length in lengths:
        running_sum += length
        if running_sum >= half_total:
            n50 = length
            break
            
    return {
        "Total Length": total_length,
        "Contig Count": contig_count,
        "Max Contig": max_contig,
        "N50": n50
    }

if __name__ == "__main__":
    print("[*] Scanning directory for FASTQ files...")
    reads = load_fastq_reads(".")
    print(f"[*] Loaded {len(reads)} total read fragments.")
    
    K = 31
    print(f"[*] Building De Bruijn graph using k-mer size K={K}...")
    graph = build_de_bruijn_graph(reads, K)
    
    print("[*] Traversing graph paths to generate contigs...")
    contigs = generate_contigs(graph, K)
    
    print("[*] Computing assembly metrics...")
    metrics = calculate_quast_metrics(contigs)
    
    print("\n--- ASSEMBLY EVALUATION REPORT ---")
    for metric_name, val in metrics.items():
        print(f"{metric_name}: {val}")
        
    with open("assembly_quast_report.txt", "w") as report_file:
        report_file.write("--- DE NOVO ASSEMBLY REPORT ---\n")
        for metric_name, val in metrics.items():
            report_file.write(f"{metric_name}: {val}\n")
    print("\n[+] Report successfully saved to assembly_quast_report.txt")
