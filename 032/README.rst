Problem 32
==========
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.

Python (CPython 2.7.2)
----------------------
::

    > time python eu032.py
    4 1738 6952
    4 1963 7852
    12 483 5796
    18 297 5346
    27 198 5346
    28 157 4396
    39 186 7254
    42 138 5796
    48 159 7632
    Sum: 45228
    
    real    0m43.005s
    user    0m42.939s
    sys 0m0.008s
