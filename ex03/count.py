import sys
import string


def text_analyzer(*params):
    """Counts the number of upper, lower, punctuation and space characters
        in a given text."""
    nb_upper = 0
    nb_lower = 0
    nb_punctuation = 0
    nb_space = 0
    if len(params) > 1:
        print("ERROR")
        return
    if (len(params) == 0):
        str = input("What is the text to analyse?\n")
    else:
        str = params[0]

    for i in range(len(str)):
        if str[i] in (' ', '\t', '\n', '\r', '\v', '\f'):
            nb_space = nb_space + 1
        elif str[i] in (string.punctuation):
            nb_punctuation = nb_punctuation + 1
        elif str[i].isupper():
            nb_upper = nb_upper + 1
        elif str[i].islower():
            nb_lower = nb_lower + 1
    print("The text contains {} characters:".format(len(str))+"\n")
    print("- {} upper letters".format(nb_upper)+"\n")
    print("- {} lower letters".format(nb_lower)+"\n")
    print("- {} punctuation marks".format(nb_punctuation)+"\n")
    print("- {} spaces".format(nb_space)+"\n")
