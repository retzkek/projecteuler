#!/usr/bin/env julia

# fibsum computes the sum of all even-values members of the
# Fibonacci sequence below n.
function fibsum(n::Int)
    f0 = 1
    f1 = 2
    fnext = 3
    r = 2
    while f1 < n
        fnext = f0+f1
        if fnext < n && fnext%2 == 0
            r += fnext
        end
        f0 = f1
        f1 = fnext
    end
    r
end

# test case
exp_r = 44
r = fibsum(90)
if r != exp_r
    println("test failed: expected $exp_r, got $r")
end

# problem
println(fibsum(4000000))

