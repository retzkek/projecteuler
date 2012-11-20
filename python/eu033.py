#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 33
solution by Kevin Retzke, May 2012
"""

def isCuriousFraction(n,d):
    # ignore trivial examples
    if n%10 == 0 or d%10 == 0:
        return False
    if n//d == 1:
        return False
    ndigits = map(int,str(n))
    ddigits = map(int,str(d))
    for nd in ndigits:
        if nd in ddigits:
            ndigits.remove(nd)
            ddigits.remove(nd)
    nn = reduce(lambda x,y: 10*x+y, ndigits)
    dd = reduce(lambda x,y: 10*x+y, ddigits)
    #print n, d, nn, dd
    return n != nn and float(n)/d == float(nn)/dd

if __name__ == '__main__':
    assert isCuriousFraction(49,98)
    assert not isCuriousFraction(30,50)
    nn = 1
    dd = 1
    for n in xrange(11,100):
        for d in xrange(n,100):
            if isCuriousFraction(n,d):
                print n,d
                nn *= n
                dd *= d
    print "%i/%i" % (nn,dd)
