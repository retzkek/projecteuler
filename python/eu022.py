#!/usr/bin/python
# encoding: utf-8

from string import ascii_uppercase

def read(filename):
    f = open(filename, 'r')
    names = []
    for line in f:
        names.extend(line.split(','))
    # remove quotes
    return map(lambda s: s.strip('"'), names)

# this was used to build the character value dictionary in characterValue()
#def buildScores():
#    scores = {}
#    val = 1
#    for ch in ascii_uppercase:
#        scores[ch] = val
#        val += 1
#    print scores

def characterValue(ch):
    vals = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 
        'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 
        'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 
        'V': 22, 'Y': 25, 'X': 24, 'Z': 26}
    if ch in vals.keys():
        return vals[ch]
    else:
        return None

def score(name):
    return sum(map(characterValue,name))


if __name__  == '__main__':
    names = read('eu022.dat')
    names.sort()
    assert score('COLIN') == 53, "name score incorrect"
    i = 1
    total = 0
    for name in names:
        total += i * score(name)
        i += 1
    print total
        
    

