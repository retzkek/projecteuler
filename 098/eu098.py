#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 98
solution by Kevin Retzke (retzkek@gmail.com), May 2012
"""

def anagram(word1, word2):
    return set(word1) == set(word2) and word1[::-1] != word1
        
if __name__ == "__main__":
    print anagram('CARE','RACE')
