__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
import string
from collections import defaultdict

def returnwords(source):
    src=open(source,"r")
    words = []
    while True:
        line = src.readline()
        if line == "":
            break
        if line == "\n" or '#' in line:
            continue
        else:
            words.append(line.strip())
    return words

def anagram_sort(source, destination):
    words=returnwords(source)
    anagrams=defaultdict(list)
    for word in words:
        key=list(word.lower())
        key.sort()
        key="".join(key)
        try:
            anagrams[key].append(word)
        except AttributeError:
            anagrams[key]=word
    words=[]
    etc=[]
    for word in anagrams.values():
        word=sorted(word,key=lambda s:s.lower())
        if word.__len__()!=1:
            words.append(word)
        else:
            etc.append(word[0])
    words=sorted(words,key=lambda s:s[0].upper())
    words.sort(key=len,reverse=True)
    etc.sort(key=lambda s:s.swapcase())
    words=words+[etc]
    dest=open(destination,"w")
    for word in words:
        for w in word:
            dest.write(w)
            dest.write("\n")
    dest.close()

def test_anagram_sort():
    source=sys.argv[1]
    destination=source[:-4]+"-results"+source[-4:]
    anagram_sort(source, destination)

if __name__ == "__main__":
    test_anagram_sort()
    #sys.exit(main())