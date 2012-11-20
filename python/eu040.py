#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 40
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #40
============
An irrational decimal fraction is created by concatenating the positive 
integers:

0.
123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

if __name__ == "__main__":
    import sys
    ds=set([12,1,10,100,1000,10000,100000,1000000])
    istart=1
    values={}
    for i in xrange(1,1000000):
        stri=str(i)
        iend=istart+len(stri)
        for d in ds:
            if d >= istart and d < iend:
                values[d] = int(stri[d-istart])
        istart=iend
        if istart > max(ds):
            break
    # test case
    if values[12] != 1:
        print "Test failed"
        sys.exit(1)
    # problem
    r = values[1]*values[10]*values[100]*values[1000]*values[10000] \
        * values[100000]*values[1000000]
    print r
