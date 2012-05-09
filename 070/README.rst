Problem 70
==========

Euler's Totient function, φ(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to
n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n
and the ratio n/φ(n) produces a minimum

Go (go1.0.1)
------------
Running with 15 goroutines::

    {7026037 7.020736e+06 1.0007550490432913}
    {7357291 7.351792e+06 1.000747980900439}
    {7507321 7.501732e+06 1.0007450279482124}
    {8316907 8.310976e+06 1.0007136345959848}
    {8319823 8.313928e+06 1.0007090511248113}
    {10000019 1.0000019e+07 1}

    real    16m22.684s
    user    234m19.899s
    sys     0m18.344s

