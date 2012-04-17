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
    array2=copy.deepcopy(array)
    #for row in array:
    #    print row
    #print
    for i in xrange(dim-1,0,-1):
        # corner
        array2[i-1][i-1]+=array2[i][i]+min(array[i-1][i],array[i][i-1])
        # bottom row
        for j in xrange(i-1):
            array2[i-1][j]+=sum(array[i][j:i])+array2[i][i]
        # right column
        tot=array2[i][i]+array[i-1][i]
        for j in xrange(i-2,-1,-1):
            tot+=array[j][i]
            array2[j][i-1]+=tot
        del array2[i]
        for row in array2:
            del row[i]
        #for row in array2:
        #    print row
        #print
    return array2[0][0]
            

        
         
if __name__ == "__main__":
    import sys
    r=matrix('test.txt')
    if r != 2427:
        print "test failed, r=%r" % r
        sys.exit(1)
    print matrix('matrix.txt')
