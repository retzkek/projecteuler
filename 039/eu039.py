#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 39
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #39
============
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""

def triangles(n):
    """
    Returns set of tuples (a,b,c) where the right angle triangle with integral
    length sides (a,b,c) has perimeter n.
    """
    results=set()
    for a in range(1,n):
        for b in range(1,n-a):
            c = n-a-b
            if a*a+b*b == c*c:
                abc=[a,b,c]
                abc.sort()
                if tuple(abc) not in set(results):
                    results.add(tuple(abc))
    return results

if __name__ == "__main__":
    import sys
    # test case
    r = triangles(120)
    if len(r) != 3:
        print "Test failed, r="
        print r
        sys.exit(1)
    # problem
    result=0
    resultn=0
    for i in xrange(12,1001):
        nt = len(triangles(i))
        if nt > 0:
            print "%i: %i" % (i, nt)
        if nt > resultn:
            result = i
            resultn = nt
    print "Max: %i (%i solutions)" % (result,resultn)
