# qwerty_word.py

from sys import argv

programmer = """
Programmed by Kyle Connolly\
"""
print(programmer)

qwerty = ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p")
word_given = argv[1]
word_checked = word_given.lower()
is_not = "{} is not a Qwerty word.".format(word_given)
is_so = "{} is a Qwerty word.".format(word_given)


def test():
    for i in word_checked:
        word = True
        if i in qwerty:
            continue
        else:
            word = False
            break
    if word is True:
        print(is_so)
    else:
        print(is_not)


test()
