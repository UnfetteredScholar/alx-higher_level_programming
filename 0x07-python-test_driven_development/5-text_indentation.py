#!/usr/bin/python3
"""Defines the text_indentation function"""


def text_indentation(text):
    """Prints a text with new lines after . ? and :

    Args:
        text (str): the txt to be indented

    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    text1 = text.replace('.', '.\3')
    text1 = text1.replace('?', '?\3');
    text1 = text1.replace(':', ':\3');

    lines = text1.split('\3')

    for line in lines:
        sline = line.strip(' ')
        if len(sline) < 1:
            continue
        print(sline, end='')
        if sline[-1] in '.?:':
            print('\n\n', end='')
