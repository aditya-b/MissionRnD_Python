__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
import string
def prune_either_or(sentence):
    words=sentence.split()
    try:
        start = words.index("either")
        end=words.index("or")
        if start+1!=end:
            return (" ".join(words[:start])+" "+" ".join(words[start+1:end]))
        else:
            return sentence
    except ValueError:
        return sentence

def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert "we could either or a hotel" == prune_either_or("we could either or a hotel")
    assert "we could or a hotel" == prune_either_or("we could or a hotel")
    assert "we could either a hotel" == prune_either_or("we could either a hotel")
    assert "It is neither here nor there" == prune_either_or("It is neither here nor there")

test_prune_either_or_student()

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
