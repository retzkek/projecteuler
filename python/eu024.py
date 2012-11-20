#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 24
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


if __name__ == "__main__":
    seq=range(10)
    ps = permutations(seq)
    print len(ps)
    print ps[999999]
