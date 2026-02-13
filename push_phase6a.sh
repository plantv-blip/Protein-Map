#!/bin/bash
# UFoE_Phase6A_ColabFold.ipynb 를 GitHub plantv-blip/Protein-Map 에 푸시하는 스크립트
# 터미널에서 이 스크립트가 있는 폴더(Protein-Map)의 상위 폴더에서 실행하세요.
set -e
REPO="/Users/youngkang/Library/Mobile Documents/com~apple~CloudDocs/UFoE Layered 4old Structure"
cd "$REPO"
cp -v "UFoE_Phase6A_ColabFold.ipynb" "Protein-Map/"
cd Protein-Map
git add UFoE_Phase6A_ColabFold.ipynb
git status
git commit -m "Add UFoE_Phase6A_ColabFold.ipynb"
git push origin main
echo "Done. Check https://github.com/plantv-blip/Protein-Map"
