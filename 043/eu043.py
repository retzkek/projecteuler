#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 43
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

pandigital = set("0123456789")

def hasProperty(n):
    ns = str(n)
    if len(ns) == 9:
        ns = '0'+ns
    if set(ns) != pandigital:
        return False
    if int(ns[1:4]) % 2 != 0:
        return False
    if int(ns[2:5]) % 3 != 0:
        return False
    if int(ns[3:6]) % 5 != 0:
        return False
    if int(ns[4:7]) % 7 != 0:
        return False
    if int(ns[5:8]) % 11 != 0:
        return False
    if int(ns[6:9]) % 13 != 0:
        return False
    if int(ns[7:10]) % 17 != 0:
        return False
    return True

if __name__ == "__main__":
    assert hasProperty("1406357289")
    for n in xrange(123456789,9876543210):
        if hasProperty(n):
            print n
