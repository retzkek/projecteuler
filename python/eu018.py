#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problems 18 and 67:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 5
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

(test case saved to eu018test.dat)

PROBLEM 18:

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

(data saved to eu018.dat)

PROBLEM 67:
"""

import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 2:
       print "usage: %s [data file]" % argv[0] 
       return 1
    f = open(argv[1],'r')
    triangle = []
    for line in f:
        triangle.append(map(int, line.split()))
    size = len(triangle)
    # collapse the triangle down by picking the best choice in the last row
    # for each element in the penultimate row and sum.  rinse and repeat.
    # example:
    #       03
    #     07  05
    #   02  04  06
    # 08  05  09  03
    #
    #     03
    #   07  05
    # 10  13  15
    #
    #   03
    # 20  20
    #
    # 23
    for row in range(size-2, -1, -1):
        for col in range(row+1):
            triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
    print triangle[0][0]
            


if __name__ == "__main__":
    sys.exit(main())

