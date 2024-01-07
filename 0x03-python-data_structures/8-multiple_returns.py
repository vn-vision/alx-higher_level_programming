#!/usr/bin/python3

def multiple_returns(sentence):

    f_chr = ''
    ln = len(sentence)

    if sentence == '':
        f_chr += str(None)
    else:
        f_chr = sentence[0]

    return (ln, f_chr)
