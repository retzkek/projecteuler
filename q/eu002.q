/ list fibonacci numbers less than 4 million
fib:-1_{x,sum -2#x}/[{4e6>last x};1 2]
/ sum even-valued terms
sum {x*0=x mod 2} each fib
