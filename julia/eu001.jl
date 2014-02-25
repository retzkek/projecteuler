#!/usr/bin/env julia

# multiple determines if n is a multiple of any of the bases.
function multiple(n::Int, bases::Vector{Int})
    for b in bases
        if n%b == 0
            return true
        end
    end
    return false
end

# natmult computes the sum of all multiples of the given bases that are
# below n.
function natmult(n::Int, bases::Vector{Int})
    result = 0
    for i=1:(n-1)
        if multiple(i,bases)
            result += i
        end
    end
    result
end

bases = [3,5]

# test case
exp_r = 23
r = natmult(10,bases)
if r != exp_r
    error("test failed: expected $exp_r, got $r")
end

# problem
println(natmult(1000,bases))

