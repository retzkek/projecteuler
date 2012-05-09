#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 75
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def triangles(n):
    print "xxxxxxxx"
    results=set()
    ntri = 0
    for a in xrange(1,n):
        for b in xrange(1,n-a):
            c = n-a-b
            if a*a+b*b == c*c:
                abc=[a,b,c]
                abc.sort()
                if tuple(abc) not in results:
                    results.add(tuple(abc))
                    ntri += 1
                    if ntri > 1:
                        return ntri
    return ntri

if __name__ == "__main__":
    for n in [12, 24, 30, 36, 40, 48]:
        assert triangles(n) == 1
    assert triangles(20) == 0
    assert triangles(120) > 1
    result = 0
    alltri = set()
    for i in xrange(12,1500001):
        ntri = 0
        for t in alltri:
            if 2*t > i:
                break
            if i%t == 0:
                ntri += 1
                if ntri > 1:
                    break
        if ntri == 0:
            ntri = triangles(i)
        if ntri > 0:
            alltri.add(i)
            if ntri == 1:
                print i
                result += 1
    print result
