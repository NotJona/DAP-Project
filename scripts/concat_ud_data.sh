#!/usr/bin/env bash
DATASET_DIR="data/ud-treebanks-v2.3"

python concat_treebanks.py data/ud/multilingual --dataset_dir ${DATASET_DIR} --add_lang_id

DATASET_DIR1="data/ud-treebanks-v2.3_en20_ja20_vi60"
DATASET_DIR2="data/ud-treebanks-v2.3_en20_ja40_vi40"
DATASET_DIR3="data/ud-treebanks-v2.3_en20_ja60_vi20"
DATASET_DIR4="data/ud-treebanks-v2.3_en25_ja25_vi50"
DATASET_DIR5="data/ud-treebanks-v2.3_en25_ja50_vi25"
DATASET_DIR6="data/ud-treebanks-v2.3_en33_ja33_vi33"
DATASET_DIR7="data/ud-treebanks-v2.3_en40_ja20_vi40"
DATASET_DIR8="data/ud-treebanks-v2.3_en40_ja40_vi20"
DATASET_DIR9="data/ud-treebanks-v2.3_en50_ja25_vi25"
DATASET_DIR10="data/ud-treebanks-v2.3_en60_ja20_vi20"
DATASET_DIR11="data/ud-treebanks-v2.3_en20_ja20_vi60_big"
DATASET_DIR12="data/ud-treebanks-v2.3_en20_ja60_vi20_big"
DATASET_DIR13="data/ud-treebanks-v2.3_en60_ja20_vi20_big"
DATASET_DIR14="data/ud-treebanks-v2.3_en33_ja33_vi33_big"
DATASET_DIR21="data/ud-treebanks-v2.3_ultimate_en33_ja33_vi33"
DATASET_DIR22="data/ud-treebanks-v2.3_ultimate_en50_ja25_vi25"
DATASET_DIR23="data/ud-treebanks-v2.3_ultimate_en33_ja50_vi17"
DATASET_DIR24="data/ud-treebanks-v2.3_ultimate_en33_ja17_vi50"

echo "Generating multilingual dataset..."

mkdir -p "data/ud"
mkdir -p "data/ud/multilingual_en20_ja20_vi60"
mkdir -p "data/ud/multilingual_en20_ja40_vi40"
mkdir -p "data/ud/multilingual_en20_ja60_vi20"
mkdir -p "data/ud/multilingual_en25_ja25_vi50"
mkdir -p "data/ud/multilingual_en25_ja50_vi25"
mkdir -p "data/ud/multilingual_en33_ja33_vi33"
mkdir -p "data/ud/multilingual_en40_ja20_vi40"
mkdir -p "data/ud/multilingual_en40_ja40_vi20"
mkdir -p "data/ud/multilingual_en50_ja25_vi25"
mkdir -p "data/ud/multilingual_en60_ja20_vi20"
mkdir -p "data/ud/multilingual_en33_ja33_vi33_big"
mkdir -p "data/ud/multilingual_en60_ja20_vi20_big"
mkdir -p "data/ud/multilingual_en20_ja60_vi20_big"
mkdir -p "data/ud/multilingual_en20_ja20_vi60_big"
mkdir -p "data/ud/multilingual_ultimate_en33_ja33_vi33"
mkdir -p "data/ud/multilingual_ultimate_en50_ja25_vi25"
mkdir -p "data/ud/multilingual_ultimate_en33_ja50_vi17"
mkdir -p "data/ud/multilingual_ultimate_en33_ja17_vi50"


python concat_treebanks.py data/ud/multilingual_en20_ja20_vi60 --dataset_dir ${DATASET_DIR1} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en20_ja40_vi40 --dataset_dir ${DATASET_DIR2} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en20_ja60_vi20 --dataset_dir ${DATASET_DIR3} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en25_ja25_vi50 --dataset_dir ${DATASET_DIR4} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en25_ja50_vi25 --dataset_dir ${DATASET_DIR5} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en33_ja33_vi33 --dataset_dir ${DATASET_DIR6} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en40_ja20_vi40 --dataset_dir ${DATASET_DIR7} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en40_ja40_vi20 --dataset_dir ${DATASET_DIR8} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en50_ja25_vi25 --dataset_dir ${DATASET_DIR9} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en60_ja20_vi20 --dataset_dir ${DATASET_DIR10} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en33_ja33_vi33_big --dataset_dir ${DATASET_DIR11} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en60_ja20_vi20_big --dataset_dir ${DATASET_DIR12} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en20_ja60_vi20_big --dataset_dir ${DATASET_DIR13} --add_lang_id
python concat_treebanks.py data/ud/multilingual_en20_ja20_vi60_big --dataset_dir ${DATASET_DIR14} --add_lang_id
python concat_treebanks.py data/ud/multilingual_ultimate_en33_ja50_vi17 --dataset_dir ${DATASET_DIR21} --add_lang_id
python concat_treebanks.py data/ud/multilingual_ultimate_en33_ja17_vi50 --dataset_dir ${DATASET_DIR22} --add_lang_id
python concat_treebanks.py data/ud/multilingual_ultimate_en33_ja50_vi17 --dataset_dir ${DATASET_DIR23} --add_lang_id
python concat_treebanks.py data/ud/multilingual_ultimate_en33_ja17_vi50 --dataset_dir ${DATASET_DIR24} --add_lang_id

