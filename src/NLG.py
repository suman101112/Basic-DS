from nltk.tokenize import wordpunct_tokenize

def nlg(expected_next_state_tag,final_utterance_list_with_tag_dict):
    for key,value in final_utterance_list_with_tag_dict.iteritems():
        #print value
        if(expected_next_state_tag == value[-1]):
            utterance_list = wordpunct_tokenize(key)
            modified_utterance_list = utterance_list[2:-2]
            generated_string = " ".join(modified_utterance_list)
            return generated_string