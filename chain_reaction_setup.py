import random
from string import punctuation
from nltk.corpus import wordnet as wn
import json
import pickle
def sort_dict_by_value_len(dict_):
    return sorted(dict_.items(), key=lambda kv: (len(kv[1]), kv[0]), reverse=True)
def strip_punctuation(s):
    for c in s:
    	if c  in punctuation:
    		return ''
    return s.lower()
file_string = ""
with open("moby10b.txt", 'r') as content_file:
    file_string = content_file.read()
bad_words = ['the', 'is', 'of', 'and', 'to', 'a', 'in', 'that', 'his', 'I',
'with', 'as', 'was', 'it', 'he', 'she', 'her', 'for', 'am', 'all', 'at', 'this', 'by', 'from',
'but', 'not', 'be', 'on','so',
'you',
'one',
'have',
'had',
'or',
'were',
'But',
'their',
'an',
'are',
'some',
'they',
'my',
'him',
'which',
'like',
'The',
'upon',
'into',
'when',
'if',
'no',
'yes',
'there',
'here',
'',
'then'
 ]

nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
file_string = file_string.split()

#full stop in dictionary to handle end cases
chain = {}
chain['.'] = [' ']

#More efficient algorith. O(n)
for i in range(0, len(file_string)):
    key = strip_punctuation(file_string[i])
    if key in bad_words or key not in nouns:
    	continue
    if key not in chain:
        chain[key] = []
        if(i+1 < len(file_string)):
            chain[key].append(file_string[i+1])
        else:
            chain[key].append('.')
    else:
        #already exists in chain
        if(i+1 < len(file_string)):
            chain[key].append(file_string[i+1])
        else:
            chain[key].append('.')

with open('chain.pkl', 'wb') as f:
    pickle.dump(chain, f, pickle.HIGHEST_PROTOCOL)
