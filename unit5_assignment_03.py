__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if type(first).__name__=="NoneType" or type(second).__name__=="NoneType":
        return False
    else:
        l1=list(first.lower())
        l2=list(second.lower())
        l1.sort()
        l2.sort()
        if l1==l2:
            return True
        return False

# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False == are_anagrams(None, None)
    assert False == are_anagrams(None, "hello")
    assert False == are_anagrams("hello", None)
    assert False == are_anagrams("bigg", "big")
    assert False == are_anagrams("bigg", "biig")
    assert False == are_anagrams("big", "small")

    assert True == are_anagrams("vile", "live")
    assert True == are_anagrams("Slate", "Least")

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)

test_are_anagrams_student()