import json as js


# Setup Json to append to
words = dict({"word": []})

# File formatting
resources_dir: str = "/git/repos/english_sort/resources"
with open(f'{resources_dir}/words_alpha.txt', 'r') as stage1:
    Lines = stage1.readlines()
    for line in Lines:
        words['word'].append(line.strip())

with open(f'{resources_dir}/words.json', 'w') as f:
    js.dump(words, f)
