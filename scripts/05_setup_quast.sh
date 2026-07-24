#!/usr/bin/env bash
set -e

echo "[*] Downloading QUAST..."
wget -q https://github.com/ablab/quast/releases/download/quast_5.3.0/quast-5.3.0.tar.gz
tar -xzf quast-5.3.0.tar.gz
cd quast-5.3.0
python3 setup.py install --user
echo "[+] QUAST installation complete."
