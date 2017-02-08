# qwerty_word.py

from sys import argv

programmer = """
Programmed by Kyle Connolly\
"""
print(programmer)

word_given = argv[1].lower()
# word_given.split()
qwerty = ("q", "w", e, r, t, y, u, i, o, p)
is_not = "{} is not a Qwerty word.".format(word_given)
is_so = "{} is a Qwerty word.".format(word_given)


def test_word():
    if word_given.startswith(qwerty, word_given[0], len(word_given)):
        print(is_so)
    else:
        print(is_not)


test_word()
