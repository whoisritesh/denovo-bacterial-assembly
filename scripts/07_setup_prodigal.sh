#!/usr/bin/env bash
set -e

echo "[*] Fetching Prodigal source..."
wget -q https://github.com/hyattpd/Prodigal/archive/refs/tags/v2.6.3.tar.gz
tar -xzf v2.6.3.tar.gz
cd Prodigal-2.6.3
make
echo "[+] Prodigal successfully compiled."
