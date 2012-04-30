#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 31
solution by Kevin Retzke (retzkek@gmail.com), April 2012
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

if __name__ == "__main__":
    coins = [200,100,50,20,10,5,2,1]
    cs = combination(coins,200)
    cs1 = []
    for c in cs:
        total = 0
        for v,n in c.iteritems():
            total += n*v
        if total == 200:
            cs1.append(c)
    print len(cs1)

