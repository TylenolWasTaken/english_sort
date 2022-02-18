#! /bin/python3
# for linux users who like cli

# I do understand that there are libs for parsing cli,
#   but I think taking the time to figure out how to do it on my own is
#   probably better for me personally


from sys import argv  # Array of cli args
argc = len(argv)  # Count of cli args (including ___.py)
__filename__ = 'main'
#    main.py -S -R G -O abcdef


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
    main(argv, argc)


