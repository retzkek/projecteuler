#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 382
solution by Kevin Retzke (retzkek@gmail.com), May 2012
"""

def u(n):
    seq = [1,2,3]
    for i in xrange(3,n):
        seq.append(seq[i-1]+seq[i-3])
    return seq

if __name__ == "__main__":
    print u(10)
