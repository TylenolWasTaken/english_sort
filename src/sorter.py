import json as js

# TODO: USER INPUT
# TODO: REFACTORING VAR & FUNCTIONS

# Loads json file as a dict
resources_dir: str = "/git/repos/english_sort/resources"
with open(f'{resources_dir}/words.json', 'r') as f:
    words_dict = js.load(f)


# Empty array to store the 'Can contain' & return
word_array = []
final_array = []

# English alphabet
alpha_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
REQUIRED = 'f'
# 'Can contain these'
char_array = ['o', 'x', 'a', 'b', 't', 'r']

for char in char_array:
    alpha_array.remove(char)  # this filters out the WANTED letters, so we can check the UNWANTED against the words

alpha_array.remove(REQUIRED)

print(alpha_array)
#  HAS TO CONTAIN 'F'
for word in words_dict['word']:
    if word.count(REQUIRED) > 0:
        word_array.append(word)

del words_dict  # Cleanup unused dict for mem

array_len = len(word_array)  # count of words in new array
print(f"words: {word_array}, array len: {array_len}")


# CAN CONTAIN [o, x, a, b, t, or r]
for word in word_array:
    i = 0  # resets to zero on every new word
    fails = 0
    for char in alpha_array:  # checks each char for each iter of loop against current word
        i += 1
        if word.count(alpha_array[i - 1]) != 0:
            print(f'fail: {i}, {word}, {alpha_array[i -1]}')
            fails += 1
            break
        else:
            print(f'pass: {i}, {word}, {alpha_array[i - 1]}')

    if fails == 0:
        final_array.append(word)

print(final_array)

