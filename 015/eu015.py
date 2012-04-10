#!/usr/bin/python
# encoding: utf-8

def fac(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

def paths(n):
    f = fac(n)
    return fac(2*n) / (f * f)

if __name__ == "__main__":
    print paths(20)
