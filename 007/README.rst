Problem 7
=========

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?

Go (go1.0.1)
------------
::

    > time go run eu007.go 
    104743
    
    real    0m0.280s
    user    0m0.240s
    sys     0m0.028s

Python (CPython 2.7.2)
----------------------
::

    > time python eu007.py 
    Test: pass
    Result: 104743
    
    real    0m10.582s
    user    0m10.549s
    sys     0m0.016s

Python (PyPy 1.8.0)
-------------------
::

    > time pypy eu007.py 
    Test: pass
    Result: 104743
    
    real    0m5.296s
    user    0m5.260s
    sys     0m0.020s

