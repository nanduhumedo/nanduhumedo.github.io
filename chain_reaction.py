

import random
from string import punctuation
from nltk.corpus import wordnet as wn
import curses
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

#Prediction
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
if valid_chain or not valid_chain:
	result = ''
	for word in final_word_list:
	    result+= str(word) + "\n"
	print(result)
else:
	print('No chain :(')

# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(1)

# stdscr.addch(5, 5, final_word_list[0][0])

# stdscr.addch(15, 5, final_word_list[-1][0])

# ch_in = stdscr.getch()
# while(ch_in != ord('`')):
# 	ch_in = stdscr.getch()
# 	stdscr.addch(ch_in)
# 	stdscr.refresh()



# curses.nocbreak(); stdscr.keypad(0); curses.echo();curses.endwin()