#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 81
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #81
============
In the 5 by 5 matrix below, the minimal path sum from the top left to the 
bottom right, by only moving to the right and down, is indicated in bold 
red and is equal to 2427.

    
    131 673 234 103 18
    201 96  342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524 37  331
        

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target 
As...'), a 31K text file containing a 80 by 80 matrix, from the top left to
the bottom right by only moving right and down.
"""
import copy

def matrix(filename):
    array=[]
    f = open(filename)
    for line in f:
        array.append([int(x) for x in line.rstrip().split(',')])
    dim = len(array)
    for row in array:
        if len(row) != dim:
            print "error: matrix not square"
            return None
    #for row in array:
    #    print row
    #print
    # bottom row
    for i in xrange(dim-2,-1,-1):
        array[dim-1][i]+=array[dim-1][i+1]
    # right column
    for j in xrange(dim-2,-1,-1):
        array[j][dim-1]+=array[j+1][dim-1]
    # work bottom to top, right to left, adding the min of the
    # cell to the right and the cell below
    for j in xrange(dim-2,-1,-1):
        for i in xrange(dim-2,-1,-1):
            array[j][i]+=min(array[j+1][i],array[j][i+1])
    return array[0][0]
         
if __name__ == "__main__":
    import sys
    r=matrix('test.txt')
    if r != 2427:
        print "test failed, r=%r" % r
        sys.exit(1)
    print matrix('matrix.txt')
