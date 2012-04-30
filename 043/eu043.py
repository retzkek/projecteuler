#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 43
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def permutations(seq):
    """
    Recursively determine lexicographic permutations of seq.
    Elegant, but probably quite slow
    """
    if len(seq) == 2:
        return [seq,[seq[1],seq[0]]]
    ps=[]
    for s in seq:
        seq1 = [n for n in seq if n != s]
        for s1 in permutations(seq1):
            ps.append([s]+s1)
    return ps

def hasProperty(n):
    if (n[1]*100 + n[2]*10 + n[3]) % 2 != 0:
        return False
    if (n[2]*100 + n[3]*10 + n[4]) % 3 != 0:
        return False
    if (n[3]*100 + n[4]*10 + n[5]) % 5 != 0:
        return False
    if (n[4]*100 + n[5]*10 + n[6]) % 7 != 0:
        return False
    if (n[5]*100 + n[6]*10 + n[7]) % 11 != 0:
        return False
    if (n[6]*100 + n[7]*10 + n[8]) % 13 != 0:
        return False
    if (n[7]*100 + n[8]*10 + n[9]) % 17 != 0:
        return False
    return True

if __name__ == "__main__":
    assert hasProperty([1,4,0,6,3,5,7,2,8,9])
    ps = permutations(range(10))
    rs = []
    for n in ps:
        if hasProperty(n):
            rs.append(n)
            print n
    result = 0
    for r in rs:
        result += int("".join(map(str,r)))
    print result
