#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 14:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

"""

def next(n):
    """
    returns the next value in the sequence
    """
    if n % 2 == 0:
        return n/2
    else:
        return 3 * n + 1

def count(n, echo=False):
    """
    count number of terms in sequence to reach 1
    """
    i = 1
    if echo:
        print n,
    while n > 1:
        i += 1
        n = next(n)
        if echo:
            print "-> %i" % n,
    if echo:
        print
    return i

def main():
    # test case
    # print count(13, echo=True)
    max = 0
    for i in range(999999,0,-1):
        m = count(i)
        if m > max:
            max = m
            print "%i: %i" % (i, max)

    



if __name__ == '__main__':
    main()
    
