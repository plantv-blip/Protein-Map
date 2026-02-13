#!/usr/bin/env python3
"""Copy UFoE_Phase6A_ColabFold.ipynb into this folder (Protein-Map)."""
import os
import sys
base = "/Users/youngkang/Library/Mobile Documents/com~apple~CloudDocs/UFoE Layered 4old Structure"
src = os.path.join(base, "UFoE_Phase6A_ColabFold.ipynb")
dst = os.path.join(base, "Protein-Map", "UFoE_Phase6A_ColabFold.ipynb")
log = os.path.join(base, "Protein-Map", "copy_result.txt")
try:
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    with open(log, "w") as f:
        f.write("OK %d bytes -> %s\n" % (len(data), dst))
except Exception as e:
    with open(log, "w") as f:
        f.write("Error: %s\n" % e)
    sys.exit(1)
