Problem 92
==========

A number chain is created by continuously adding the square of the 
digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an 
endless loop. What is most amazing is that EVERY starting number will 
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

Go (go1.0.1)
------------
::

    > time go run eu092.go
    8581146

    real    0m1.563s
    user    0m1.528s
    sys     0m0.020s

Python (PyPy 1.8.0)
-------------------
::

    > time pypy eu092.py 
    8581146

    real    0m40.605s
    user    0m40.351s
    sys     0m0.060s


Python (CPython 2.7.2)
----------------------
::
    
    > time python eu092.py 
    8581146

    real    2m32.275s
    user    2m31.973s
    sys     0m0.080s
