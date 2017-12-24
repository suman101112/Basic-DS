
def extract_the_best_DA_tag_to_test(nlu_output,final_utterance_list_with_tag):
    max_count = -100
    best_match_utterance = ''
    best_tag = ''
    for item in final_utterance_list_with_tag:
        count = 0.0
        tag = item[-1]
        train_utterance = item[0:-1]
        #print tag
        #print train_utterance
        
        for test_item in nlu_output:
            if test_item in train_utterance:
                count+=1.0
        count = count - len(train_utterance)
        if count >= max_count:
            max_count = count
            #print max_count
            best_match_utterance = train_utterance
            best_tag = tag
    #print best_match_utterance
    #print best_tag        
    return best_tag                

def predict_answer_DA_tag(best_tag,dict_uni,dict_bi):
    
    dict_bi_keys = dict_bi.keys()
    max_count = 0
    answer_tag = ''
    for item in dict_bi_keys:
        count = 0
        if best_tag == item[0]:
            #print item
            count = dict_bi[item]
            if(count > max_count):
                max_count = count
                #print item
                answer_tag = item[1]
    return answer_tag


def dialog_manager(nlu_output,dict_uni,dict_bi,final_utterance_list_with_tag):
    best_tag = extract_the_best_DA_tag_to_test(nlu_output,final_utterance_list_with_tag)
    answer_tag = predict_answer_DA_tag(best_tag,dict_uni,dict_bi)
    print answer_tag
