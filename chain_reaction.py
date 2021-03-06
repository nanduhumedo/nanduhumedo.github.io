import pickle

import random
def sort_dict_by_value_len(dict_):
    return sorted(dict_.items(), key=lambda kv: (len(kv[1]), kv[0]), reverse=True)
def get_chain():
    #Prediction
    with open('/home/nfrancque/chain_reaction/chain.pkl', 'rb') as f:
    	chain = pickle.load(f)
    print(len(chain.keys()))

    # for bad_word in bad_words:
    # 	if bad_word in chain:
    # 		del chain[bad_word]
    chain_sorted_list_top_100 = sort_dict_by_value_len(chain)
    # for k, v in chain:
    # 	if len(v) > 200:
    # 		print(k)
    #Can move to dedicated function or something...
    WORD_LENGTH = 5
    final_word_list = []
    valid_chain = False
    for i in range(50):
    	if (len(final_word_list)) == WORD_LENGTH:
    		print('Got a chain!')
    		valid_chain = True
    		break
    	else:
    		final_word_list = []
    	start_word = random.choice(chain_sorted_list_top_100)[0]
    	final_word_list.append(start_word)
    	current_word = ''

    	for i in range(WORD_LENGTH):
    		timeout = False
    		current_word = final_word_list[i]
    		next_word = ''
    		try_counter = 0
    		while next_word not in chain:
    			if try_counter == len(chain[current_word]):
    				print("Invalid chain")
    				timeout = True
    				break
    			next_word = random.choice(chain[current_word])
    			try_counter += 1
    		if timeout:
    			break
    		final_word_list.append(next_word)

    #Formatting python list to a string for output
    if valid_chain:
    	result = ''
    	for word in final_word_list:
    	    result+= str(word) + "\n"

    	return result
    else:
    	return 'No chain :('

