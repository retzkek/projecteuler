#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 26
solution by Kevin Retzke, May 2012
"""

def longDivide(n,d):
    """Returns n/d as (i,f,r), where i is the integer portion, f
    is the non-recurring fraction, and r is the recurring fraction,
    i.e. i.f(r).  f and r are lists of digits."""
    integer = n//d
    rem = n%d
    rems = [rem]
    digits = []
    while True:
        rem *= 10
        digits.append(rem//d)
        rem = rem%d
        if rem in rems:
            start = rems.index(rem)
            return (integer, digits[:start], digits[start:])
        else:
            rems.append(rem)

if __name__ == '__main__':
    (i,f,r) = longDivide(1,6)
    assert len(r) == 1
    (i,f,r) = longDivide(1,7)
    assert len(r) == 6
    maxr = 0
    maxd = 0
    for d in xrange(1,1000):
        (i,f,r) = longDivide(1,d)
        if len(r) > maxr:
            maxr = len(r)
            maxd = d
    print maxd

