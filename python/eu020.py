#!/usr/bin/python
# encoding: utf-8

def fac(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

if __name__ == "__main__":
    num = "%i" % fac(100)
    print sum(map(int,num))
