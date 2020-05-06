#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tuple_sent = (length, 'None')
    else:
        tuple_sent = (length, sentence[0])
    return (tuple_sent)
