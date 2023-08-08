#!/usr/bin/env python3
import argparse


def convert_one_line(filepath):
    file_input = open(filepath, 'r')

    output = ''
    for line in file_input.readlines():
        if line.isspace():
            continue
        if line.lstrip().startswith('#'):
            continue

        line_stripped = line.rstrip()
        if line_stripped.endswith(('do', 'done', 'then', 'else', 'fi')):
            output = output + line_stripped + ' '
        elif line_stripped.endswith(';'):
            output = output + line_stripped + ' '
        else:
            output = output + line_stripped + '; '

    print(output)

    file_input.close()


def main():
    parser = argparse.ArgumentParser(description='convert a multiline shell script to a single line')
    parser.add_argument("-f", "--filepath", type=str,
                        help="full path to the multiline shell script")
    args = parser.parse_args()

    convert_one_line(filepath=args.filepath)
    return


if __name__ == "__main__":
    main()
