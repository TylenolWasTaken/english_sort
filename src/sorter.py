import json as js

# TODO: USER INPUT
# TODO: REFACTORING VAR & FUNCTIONS

# Loads json file as a dict
resources_dir: str = "/git/repos/english_sort/resources"
with open(f'{resources_dir}/words.json', 'r') as f:
    dict_words = js.load(f)

with open(f'{resources_dir}/settings.json', 'r') as f:
    dict_settings = js.load(f)

    json_globals = dict_settings['globals']
    json_locals = dict_settings['sorter']
    del dict_settings

    _debug = json_globals['debug']

# Empty array to store the 'Can contain' & return
array_words = []
array_final = []

# English alphabet
array_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_required = 'o'
# 'Can contain these'
array_char_optional = ['g', 'n', 'p', 'i', 'w', 'h']

for char in array_char_optional:
    array_alphabet.remove(char)  # this filters out the WANTED letters, so we can check the UNWANTED against the words

array_alphabet.remove(char_required)

print(array_alphabet)
#  HAS TO CONTAIN 'F'
for word in dict_words['word']:
    if word.count(char_required) > 0:
        array_words.append(word)

del dict_words  # Cleanup unused dict for mem

len_array = len(array_words)  # count of words in new array
print(f"words: {array_words}, array len: {len_array}")

del len_array

# CAN CONTAIN [o, x, a, b, t, or r]
for word in array_words:
    i = 0  # resets to zero on every new word
    fails = 0
    for char in array_alphabet:  # checks each char for each iter of loop against current word
        i += 1
        if word.count(array_alphabet[i - 1]) != 0:
            print(f'fail: {i}, {word}, {array_alphabet[i - 1]}')
            fails += 1
            break
        else:
            print(f'pass: {i}, {word}, {array_alphabet[i - 1]}')

    if fails == 0:
        array_final.append(word)

del array_words

for word in array_final:
    len_word = len(word)
    if not 4 > len_word:
        print(f'pass: {word}, {len_word}')
        array_final.remove(word)
    else:
        print(f'fail: {word}, {len_word}')

print(array_final)

