#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 42
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def triangle(n):
    return n*(n+1)/2

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def wordValue(word):
    value = 0
    for c in word:
        value += letters.index(c)+1
    return value

if __name__ == "__main__":
    # read and parse wordlist
    f = open('words.txt')
    words = f.readline().split(',')
    for i in range(len(words)):
        words[i] = words[i].replace('"','')
    # calculate word values
    wl = []
    for w in words:
        wl.append(wordValue(w))
    # calculate triangle numbers
    t = set()
    for i in range(1,max(wl)+1):
        t.add(triangle(i))
    # find how many words are triangle words
    n = 0
    for w in wl:
        if w in t:
            n += 1
    print n
