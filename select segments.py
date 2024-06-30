#let's select 100 random segments of our conllu files
import random
from conllu import parse

path_en_train = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_English-EWT/en_ewt-ud-train.conllu"
path_ja_train = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Japanese-GSD/ja_gsd-ud-train.conllu"
path_vi_train = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Vietnamese-VTB/vi_vtb-ud-train.conllu"

path_en_test = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_English-EWT/en_ewt-ud-test.conllu"
path_ja_test = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Japanese-GSD/ja_gsd-ud-test.conllu"
path_vi_test = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Vietnamese-VTB/vi_vtb-ud-test.conllu"

path_en_dev = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_English-EWT/en_ewt-ud-dev.conllu"
path_ja_dev = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Japanese-GSD/ja_gsd-ud-dev.conllu"
path_vi_dev = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Vietnamese-VTB/vi_vtb-ud-dev.conllu"



def generate_rand_values(file_path, n):
    l = []
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        length = len(parse(file_content))
    
    while len(l)<n:
        a = random.randint(0, length)
        if a not in l:
            l.append(a)
    return l



def choose_segments(file_path, n):
    result_data = []
    index = generate_rand_values(file_path, n)
    item_count = 0
    inside_item = False

    with open(file_path, 'r', encoding='utf-8') as file:    
        for line in file:
            line = line.strip()
            if line.startswith('# sent_id'):
                # New item starts
                inside_item = True
                if item_count in index:
                    result_data.append(line)
            elif line == '' and inside_item:
                # Empty line marks the end of the item
                item_count += 1
                inside_item = False
                if item_count in index:
                    result_data.append(line)
            else:
                if item_count in index:
                    result_data.append(line)
    return result_data



train_data_en = choose_segments(path_en_train, 12000) 
train_data_ja = choose_segments(path_ja_train, 6000) 
train_data_vi = choose_segments(path_vi_train, 1200) 
test_data_en = choose_segments(path_en_test, 740) 
test_data_ja = choose_segments(path_ja_test, 470) 
test_data_vi = choose_segments(path_vi_test, 590) 
dev_data_en = choose_segments(path_en_dev, 740) 
dev_data_ja = choose_segments(path_ja_dev, 470) 
dev_data_vi = choose_segments(path_vi_dev, 590) 


with open("en_ud-train.conllu", "w", encoding="utf-8") as new_file:
    for line in train_data_en:
        new_file.write(line+"\n")
with open("ja_ud-train.conllu", "w", encoding="utf-8") as new_file:
    for line in train_data_ja:
        new_file.write(line+"\n")
with open("vi_ud-train.conllu", "w", encoding="utf-8") as new_file:
    for line in train_data_vi:
        new_file.write(line+"\n")
with open("en_ud-test.conllu", "w", encoding="utf-8") as new_file:
    for line in test_data_en:
        new_file.write(line+"\n")
with open("ja_ud-test.conllu", "w", encoding="utf-8") as new_file:
    for line in test_data_ja:
        new_file.write(line+"\n")
with open("vi_ud-test.conllu", "w", encoding="utf-8") as new_file:S
    for line in test_data_vi:
        new_file.write(line+"\n")
with open("en_ud-dev.conllu", "w", encoding="utf-8") as new_file:
    for line in dev_data_en:
        new_file.write(line+"\n")
with open("ja_ud-dev.conllu", "w", encoding="utf-8") as new_file:
    for line in dev_data_ja:
        new_file.write(line+"\n")
with open("vi_ud-dev.conllu", "w", encoding="utf-8") as new_file:
    for line in dev_data_vi:
        new_file.write(line+"\n")


#python predict.py logs/udapter/2024.06.12_22.28.41_ultimate_en33_ja33_vi33/model.tar.gz data/ud/multilingual_ultimate_en33_ja33_vi33/dev.conllu ultimate_en33_ja33_vi33_dev.conllu --eval_file ultimate_en33_ja33_vi33_dev.json
#python predict.py logs/udapter/2024.06.12_22.28.41_ultimate_en33_ja33_vi33/model.tar.gz data/ud/multilingual_ultimate_en33_ja33_vi33/test.conllu ultimate_en33_ja33_vi33_test.conllu --eval_file ultimate_en33_ja33_vi33_test.json
#python predict.py logs/udapter/2024.06.12_22.28.41_ultimate_en33_ja33_vi33/model.tar.gz data/ud/multilingual_ultimate_en33_ja33_vi33/test_33_33_33.conllu ultimate_en33_ja33_vi33_test33.conllu --eval_file ultimate_en33_ja33_vi33_test33.json

