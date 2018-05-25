__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
vowels=['a','e','i','o','u']
punctuations=[',','.']

def get_last_consonant_place(word):
    i=0
    while word[i] not in vowels:
        i=i+1
    return i

def pig_latin_word(word):
    punc=''
    for i in punctuations:
        if i in word:
            word=word[:-1]
            punc=i
    if word[0] in vowels:
        return word+'ay'+punc
    else:
        i=get_last_consonant_place(word)
        flag = 0
        res=''
        result=''
        if word[0].isupper():
            flag = 1
            res+=word[0].lower()+word[1:i]
        else:
            res+=word[:i]
        if flag==1:
            result+=word[i].upper()+word[i+1:]
        else:
            result+=word[i:]
        return result+res+'ay'+punc

def pig_latin(input):
    words=input.split(" ")
    result=[]
    for word in words:
        result.append(pig_latin_word(word))
    return ' '.join(result)

if __name__ == "__main__":
    result=pig_latin(sys.argv[1])
    try:
        while True:
            print(result)
    except KeyboardInterrupt:
        sys.exit(0)
    #sys.exit(main())