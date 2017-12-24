from nltk.tokenize import wordpunct_tokenize
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer
import nltk

stemmer = SnowballStemmer("english", ignore_stopwords=True)

def nlu(utterance):
    utterance_list = wordpunct_tokenize(utterance) #tokenizer
    #print utterance_list
    utterance_stem = [str(stemmer.stem(word)) for word in utterance_list] #morpher
    stem_pos_tag_with_DA_tag = nltk.pos_tag(utterance_stem) #pos_tag
    #line =  "you said: \"" + str(stem_pos_tag_with_DA_tag) + "\" "
    return stem_pos_tag_with_DA_tag
    
    