#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 145
solution by Kevin Retzke (retzkek@gmail.com), May 2012
"""

def isReversible(n):
    revns = str(n)[::-1]
    # filter leading 0s
    if revns[0] == '0':
        return False
    revn = int(revns)
    for i in map(int,str(n+revn)):
        if i%2 == 0:
            return False
    return True

if __name__ == "__main__":
    assert isReversible(36)
    assert isReversible(409)
    count = 0
    for n in xrange(11,1000000000):
        if isReversible(n):
            count += 1
    print count
        
