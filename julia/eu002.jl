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

using Test
@test fibsum(90) == 44

# problem
println(fibsum(4000000))

