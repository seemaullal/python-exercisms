from collections import Counter

# to be backwards compatible with the old Python 2.X
def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


def word_count(text):
