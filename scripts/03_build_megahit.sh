#!/usr/bin/env bash
set -e

echo "[*] Cloning MEGAHIT repository..."
if [ ! -d "megahit" ]; then
    git clone https://github.com/voutcn/megahit.git
fi

cd megahit
mkdir -p build && cd build
cmake ..
make -j8
echo "[+] MEGAHIT successfully compiled."
