Problem 87
==========

The smallest number expressible as the sum of a prime square, prime cube,
and prime fourth power is 28. In fact, there are exactly four numbers 
below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a 
prime square, prime cube, and prime fourth power?

Go (go1.0.1)
------------
::

    > time go run eu087.go
    1097343

    real    0m0.796s
    user    0m0.712s
    sys     0m0.072s

Python (PyPy 1.8.0)
-------------------
::

    > time pypy eu087.py 
    1097343
    
    real    0m1.569s
    user    0m1.508s
    sys     0m0.052s

Python (CPython 2.7.2)
----------------------
::
    
    > time python eu087.py 
    1097343
    
    real    0m11.212s
    user    0m11.157s
    sys 0m0.036s
