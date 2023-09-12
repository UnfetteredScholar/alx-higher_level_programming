#!/usr/bin/python3
"Defines the read_file function"""


def read_file(filename=""):
    "Reads a file and prints its contents to stdout"

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
