#! /bin/python3
# for linux users who like cli

# I do understand that there are libs for parsing cli,
#   but I think taking the time to figure out how to do it on my own is
#   probably better for me personally

from sys import argv  # Array of cli args
import json as js

_debug = __debug__  # pycharm is shortening my life

argc = len(argv)  # Count of cli args (including ___.py)
__filename__ = 'main'
resources_dir: str = "/git/repos/english_sort/resources"


def main(_argv, _argc):
    # check if cli args passed
    if not _argc > 1:
        print(f"""
        USAGE: {__filename__}.py -S --required= --optional=
            Operations:
                -P      --Parse     reparse dict file (can be used to add different dict) [ie --Parse=FILENAME]
                -S      --Sort      sorts words based on given requirements
                -R      --Remove    removes a word from the dictionary
                
            Options:
                -r      --required  required char for parsing
                -o      --optional  optional chars, no separation (ie. 'asdfer')
        """)

        exit(0)


if __name__ == '__main__':
    with open(f'{resources_dir}/settings.json', 'r') as f:
        json_settings = js.load(f)

    json_settings['globals']['debug'] = _debug

    with open(f'{resources_dir}/settings.json', 'w') as f:
        js.dump(json_settings, f, indent=2)


    # main(argv, argc)

# TODO: make filename checking dynamic
