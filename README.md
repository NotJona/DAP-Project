# Data Analysis Project
This repository contains the project resulting from the course "Data Analysis Project" at the University of Vienna (2024).

# Project Motivation
Recent advancements in universal dependency parsing, specifically Udapter (see citation below), have yielded valuable insights into the parsing of low resource languages. Without being trained on them, this universal dependency parser is able to successfully parse various languages that themselves lack the data to successfully train a dependency parser. Hence, universal dependency parsers like Udapter provide a viable option for the parsing of low resource languages. 

Udapter, however, was meant to be universal and the results on non-training languages vary considerably. To analyze its performance when utilized for a specific target language, I trained the Udapter model on three languages (English, Japanese, Russian) that share different typological similarities with a chosen target language (Mandarin Chinese). This is done due to the unique architecture of Udapter, specifically the so-called Contextual Parameter Generator, which enables Udapter to learn parameters depending on the typologies of the in-training languages. Hence, with the major typological characteristics of the target language shared by one or several of the training languages, the resulting model should – in theory – be able to successfully parse the target language.   

Going one step further, I also wanted to analyze the impact of the training set composition. For the original Udapter model the percentages in which the individual languages occurred during training were given by the size of their treebanks. To see whether different compositions of language occurrences, i.e. their weight, have an effect on the resulting parser, I trained Udapter on four different datasets instead of one (see below) and compared the performance of the four resulting models.

# Methodology
The project relies on the code of the original Udapter. Several models varying both in size and dataset configuration were trained. Detailed information can be found at:
- DAP_Project.ipynb
- Project_Report.pdf

# Findings
While I did not succeed in training a working parser for Mandarin Chinese, I was able to show that upsampling of underrepresented languages' datasets can significantly improve modle performance. Considering the main goal was to investigate the possibilities of using universal dependency parsers for low resource languages, these findings still provide valueable insights.

# Citation
The project was based on the work of
```latex
@inproceedings{ustun-etal-2020-udapter,
    title = {{UD}apter: Language Adaptation for Truly {U}niversal {D}ependency Parsing},
    author = {{\"U}st{\"u}n, Ahmet  and
      Bisazza, Arianna  and
      Bouma, Gosse  and
      van Noord, Gertjan},
    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    month = nov,
    year = {2020},
    address = {Online},
    publisher = {Association for Computational Linguistics},
    url = {https://www.aclweb.org/anthology/2020.emnlp-main.180},
    pages = {2302--2315},
    abstract = {Recent advances in multilingual dependency parsing have brought the idea of a truly universal parser closer to reality. However, cross-language interference and restrained model capacity remain major obstacles. To address this, we propose a novel multilingual task adaptation approach based on contextual parameter generation and adapter modules. This approach enables to learn adapters via language embeddings while sharing model parameters across languages. It also allows for an easy but effective integration of existing linguistic typology features into the parsing network. The resulting parser, UDapter, outperforms strong monolingual and multilingual baselines on the majority of both high-resource and low-resource (zero-shot) languages, showing the success of the proposed adaptation approach. Our in-depth analyses show that soft parameter sharing via typological features is key to this success.},
}


