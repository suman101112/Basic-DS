import os

from nltk.tokenize import wordpunct_tokenize
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english", ignore_stopwords=True)

from collections import defaultdict

dict_unigram = defaultdict(int)
dict_bigram = defaultdict(int)

def add_to_dict_n_gram_tags(dict_temp,n_grams_list):
    for n_gram in n_grams_list:
        dict_temp[n_gram]+=1

def extract_tag_n_grams_and_add_to_dict(data_dir):
    listing = os.listdir(data_dir)
    list = []
    for filename in listing:
        with open(data_dir+filename,'r') as f:
            tag_list_for_line = []
            for line in f:
                if(':' in line):
                    line_list = wordpunct_tokenize(line)
                    tag = line_list[-1]
                    tag_list_for_line.append(tag)
                else:
                    if(len(tag_list_for_line)>0):
                        add_to_dict_n_gram_tags(dict_unigram,tag_list_for_line)
                        bigrams = ngrams(tag_list_for_line,2)
                        add_to_dict_n_gram_tags(dict_bigram,bigrams) 
                    tag_list_for_line = []
    
    list.append(dict_unigram)
    list.append(dict_bigram)
    return list

def print_dict(dict_temp):
    for key,value in dict_temp.iteritems():
        print key,value
