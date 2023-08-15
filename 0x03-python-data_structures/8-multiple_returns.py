#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = 0
    if sentence is not None:
        lenght = len(sentence)
    if lenght == 0:
        return (lenght, None)
    else:
        return (lenght, sentence[0])
