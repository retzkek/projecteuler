Problem 381
===========
For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! 
= 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

Find ∑S(p) for 5 ≤ p < 10^8.

Python (PyPy 1.8.0)
-------------------
::

    > time pypy eu381.py
    139602943319822
    
    real    2m1.485s
    user    2m0.030s
    sys 0m0.940s

Python (CPython 2.7.1)
----------------------
::

    > time python eu381.py
    139602943319822
    
    real    14m39.233s
    user    14m20.480s
    sys 0m17.260s


