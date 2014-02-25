#!/usr/bin/env julia

# fib produces consecutive values in the Fibonacci sequence
function fib()
    n0 = BigInt(1)
    n1 = BigInt(1)
    while true
        produce(n0)
        next = n0+n1
        n0 = n1
        n1 = next
    end
end

num_digits(n::BigInt) = length(string(n))

f = Task(fib)

# test case
i = 1
n = consume(f)
while num_digits(n) < 3
    i+=1
    n = consume(f)
end

exp_r = 12
r = i
if r != exp_r
    error("test failed: expected $exp_r, got $r")
end

# problem
while num_digits(n) < 1000
    i+=1
    n = consume(f)
end
println(i)
