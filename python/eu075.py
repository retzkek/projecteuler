#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 75
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def triangles(n):
    """Returns set of tuples (a,b,c) where the right angle triangle with
    integral length sides (a,b,c) has perimeter n."""
    results=set()
    for a in xrange(1,n):
        for b in xrange(1,n-a):
            c = n-a-b
            if a*a+b*b == c*c:
                abc=[a,b,c]
                abc.sort()
                if tuple(abc) not in set(results):
                    results.add(tuple(abc))
    if len(results) > 0:
        print n, results
    return results

if __name__ == "__main__":
    #for n in [12, 24, 30, 36, 40, 48]:
    #    print n,triangles(n)
    #print triangles(120)
    result = 0
    for i in xrange(12,1500001):
        if len(triangles(i)) == 1:
            result += 1
    print result
