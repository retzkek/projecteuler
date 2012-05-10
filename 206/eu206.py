#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 206
solution by Kevin Retzke (retzkek@gmail.com), May 2012
"""
import math

if __name__ == "__main__":
    n = int(math.sqrt(1020304050607080900))
    while str(n**2)[::2] != '1234567890':
        n += 1
        #print n, str(n**2)
    print n
