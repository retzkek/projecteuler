#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 76
solution by Kevin Retzke, April 2012
"""

def combination(vals, total):
    if len(vals) == 0:
        return [{}]
    v = max(vals)
    nv = total/v
    newvals = [n for n in vals if n != v]
    cs = []
    for i in range(nv+1):
        remainder = total - i*v
        for c in combination(newvals, remainder):
            c[v]=i
            cs.append(c)
    return cs

if __name__ == '__main__':
    cs = combination(range(99,0,-1),100)
    cs1 = []
    for c in cs:
        tot = 0
        for v,n in c.iteritems():
            tot += n*v
        if tot == 5:
            cs1.append(c)
    #for c in cs1:
    #    print c
    print len(cs1)

