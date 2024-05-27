""" Let's look at the different Treebanks. How much sentences are in each set? How much tokens?"""

def count_conllu_items_sentences(file_path):
    """Counts segments in a conllu file, which should (mostly) correspond to sentences"""
    item_count = 0
    inside_item = False
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('# sent_id'):
                # New item starts
                if inside_item:
                    item_count += 1
                inside_item = True
            elif line == '' and inside_item:
                # Empty line marks the end of the item
                item_count += 1
                inside_item = False

    return item_count

def count_conllu_items_tokens(file_path):
    """Counts 'sentence elements'. This is not the same as tokens, since sometimes a 'sentence element' is made of two words"""
    item_count = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Strip leading/trailing whitespace
            line = line.strip()
            # Ignore empty lines and comment lines
            if line and not line.startswith('#'):
                item_count += 1

    return item_count

file_path0 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_English-EWT/en_ewt-ud-dev.conllu"
item_count0 = count_conllu_items_sentences(file_path0)
item_count00 = count_conllu_items_tokens(file_path0)
file_path1 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_English-EWT/en_ewt-ud-test.conllu"
item_count1 = count_conllu_items_sentences(file_path1)
item_count11 = count_conllu_items_tokens(file_path1)
file_path2 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_English-EWT/en_ewt-ud-train.conllu"
item_count2 = count_conllu_items_sentences(file_path2)
item_count22 = count_conllu_items_tokens(file_path2)
print(f'The English CoNLL-U file contains {item_count0 + item_count1 + item_count2} items and {item_count00 + item_count11 + item_count22} tokens.')

file_path0 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Japanese-GSD/ja_gsd-ud-dev.conllu"
item_count0 = count_conllu_items_sentences(file_path0)
item_count00 = count_conllu_items_tokens(file_path0)
file_path1 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Japanese-GSD/ja_gsd-ud-test.conllu"
item_count1 = count_conllu_items_sentences(file_path1)
item_count11 = count_conllu_items_tokens(file_path1)
file_path2 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Japanese-GSD/ja_gsd-ud-train.conllu"
item_count2 = count_conllu_items_sentences(file_path2)
item_count22 = count_conllu_items_tokens(file_path2)
print(f'The Japanese CoNLL-U file contains {item_count0 + item_count1 + item_count2} items and {item_count00 + item_count11 + item_count22} tokens.')

file_path0 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Vietnamese-VTB/vi_vtb-ud-dev.conllu"
item_count0 = count_conllu_items_sentences(file_path0)
item_count00 = count_conllu_items_tokens(file_path0)
file_path1 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Vietnamese-VTB/vi_vtb-ud-test.conllu"
item_count1 = count_conllu_items_sentences(file_path1)
item_count11 = count_conllu_items_tokens(file_path1)
file_path2 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud-treebanks-v2.3/UD_Vietnamese-VTB/vi_vtb-ud-train.conllu"
item_count2 = count_conllu_items_sentences(file_path2)
item_count22 = count_conllu_items_tokens(file_path2)
print(f'The Vietnamese CoNLL-U file contains {item_count0 + item_count1 + item_count2} items and {item_count00 + item_count11 + item_count22} tokens.')




""" Now let's look at the combined set (the way udapter would do it if you just followed the code on the github). How many sentences are there of each language?"""

def count_conllu_items_with_label(file_path):
    item_count = 0
    inside_item = False
    language_counter = True
    language_counter_en = 0
    language_counter_ja = 0 
    language_counter_vi = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('# sent_id'):
                # New item starts
                if inside_item:
                    item_count += 1
                inside_item = True 
                language_counter = True
            if not line.startswith('#'):
                if language_counter:
                    if line.endswith('en'):
                        language_counter_en +=1
                    if line.endswith('ja'):
                        language_counter_ja +=1
                    if line.endswith('vi'):
                        language_counter_vi +=1
                    language_counter = False
            elif line == '' and inside_item:
                # Empty line marks the end of the item
                item_count += 1
                inside_item = False

    return item_count, language_counter_en, language_counter_ja, language_counter_vi

file_path0 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud/multilingual/train.conllu"
item_count0, item_count01, item_count02, item_count03 = count_conllu_items_with_label(file_path0)
file_path1 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud/multilingual/dev.conllu"
item_count1, item_count11, item_count12, item_count13 = count_conllu_items_with_label(file_path1)
file_path2 = "C:/Users/Jona/OneDrive - Cloudlifters/Uni/Sommersemester 2024/DAP/DAP CODE/udapter/data/ud/multilingual/test.conllu"
item_count2, item_count21, item_count22, item_count23 = count_conllu_items_with_label(file_path2)
print(f'The combined CoNLL-U file contains {item_count0 + item_count1 + item_count2} items.')
print(f'The CoNLL-U file contains {item_count01 + item_count11 + item_count21} english items.')
print(f'The CoNLL-U file contains {item_count02 + item_count12 + item_count22} japanese items.')
print(f'The CoNLL-U file contains {item_count03 + item_count13 + item_count23} vietnamese items.')


def count_conllu_items(file_path):
    item_count = 0
    inside_item = False
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('# sent_id'):
                # New item starts
                if inside_item:
                    item_count += 1
                inside_item = True
            elif line == '' and inside_item:
                # Empty line marks the end of the item
                item_count += 1
                inside_item = False

    return item_count



