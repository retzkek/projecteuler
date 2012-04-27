#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 24
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""
def permutations(seq, main=False):
    """
    Recursively determine lexicographic permutations of seq.
    Elegant, but probably quite slow
    Some extra logic required to address the problem at hand.
    """
    if len(seq) == 2:
        return [seq,[seq[1],seq[0]]]
    ps=[]
    i=0
    for s in seq:
        seq1 = [n for n in seq if n != s]
        for s1 in permutations(seq1):
            ps.append([s]+s1)
            # since we need the millionth permutation, keep track and bug
            # out once we hit that
            if main:
                i += 1
                if i == 1e6:
                    print "".join([str(a) for a in [s]+s1])
                    return ps
    return ps


if __name__ == "__main__":
    seq=range(10)
    permutations(seq, True)
