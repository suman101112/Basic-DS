import os

from nltk.tokenize import wordpunct_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk

stemmer = SnowballStemmer("english", ignore_stopwords=True)

dict_map_line_to_pos_tagged_line = {}

def tokenize_stem_and_pos_tag_data(data_dir):
    listing = os.listdir(data_dir)
    final_list = []
    for filename in listing:
        with open(data_dir+filename,'r') as f:
            for line in f:
                if(':' in line):
                    #print line
                    utterance_list = wordpunct_tokenize(line)
                    modified_utterance_list = utterance_list[2:-2]
                    utterance_stem_list = [stemmer.stem(word) for word in modified_utterance_list]
                    string_stem = [str(word_stem) for word_stem in utterance_stem_list]
                    #print nltk.pos_tag(string_stem)
                    stem_pos_tag_with_DA_tag = nltk.pos_tag(string_stem)
                    stem_pos_tag_with_DA_tag.append(utterance_list[-1])
                    if not ( stem_pos_tag_with_DA_tag in final_list):
                        final_list.append(stem_pos_tag_with_DA_tag)
                        dict_map_line_to_pos_tagged_line[line] = stem_pos_tag_with_DA_tag
    
    return dict_map_line_to_pos_tagged_line
                 

def print_line_with_tag(list):
    for item in list:
        print item