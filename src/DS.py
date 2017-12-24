from NLU import nlu
from DM import dialog_manager
from NLG import nlg

#knowledge_base

from n_grams_for_tags import *
from train_utterance_with_tag import *
from scipy.odr.odrpack import Output

data_dir = "../data_tagged/"

list_uni_bi = extract_tag_n_grams_and_add_to_dict(data_dir)
dict_uni = list_uni_bi[0]
dict_bi = list_uni_bi[1]

#print_dict(dict_uni)
#print_dict(dict_bi)

final_utterance_list_with_tag_dict = tokenize_stem_and_pos_tag_data(data_dir)
final_utterance_list_with_tag = final_utterance_list_with_tag_dict.values()

#print_line_with_tag(final_utterance_list_with_tag)

#start of conversation

def greet():
    greet = "hello, how can I help you?"
    return greet

if __name__ == '__main__':
    print greet()
    flag_eoc = False
    while(not flag_eoc):
        input = raw_input("Student:")
        nlu_output = nlu(input)
        print nlu_output
        expected_next_state_tag = dialog_manager(nlu_output,dict_uni,dict_bi,final_utterance_list_with_tag)
        nlg_output = nlg(expected_next_state_tag,final_utterance_list_with_tag)
        print nlg_output
        if("thank you" in input.lower() or "thanks" in input.lower()):
            flag_eoc = True
            
        
    