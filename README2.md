# DAP-Project

ACHTUNG! Hier sind meine Treebanks drin, nicht die von udapter! Das betrifft:
1. die Files in DATA:
    Unter UD\MULTILINGUAL die 3 Daten sets
    Unter VOCAB\TEST die datei langs.txt
    Außerdem ist die Chinese Treebank hier, weil ich dachte ich brauch sie noch...

2. im Ordner LANGUAGES die Files "in-lang.txt" und "oov-langs.txt" und 

3 zum predicten: python predict.py logs/udapter/2024.05.23_13.30.07/model.tar.gz data/ud/multilingual/test.conllu output.conllu --eval_file results.json
