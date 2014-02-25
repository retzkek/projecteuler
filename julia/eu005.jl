#!/usr/bin/env julia

# divisible_by_all returns the smallest integer that is evenly divisible
# by all integers in ns.
function divisible_by_all(ns::Array{Int})
    i = 0
    step = maximum(ns)
    found = false
    while !found
        i += step
        candidate = true
        for n in ns
            if i%n != 0
                candidate = false
                break
            end
        end
        found = candidate
    end
    return i
end

# test case
exp_r = 2520
r = divisible_by_all([1:10])
if r != exp_r
    error("test failed: expected $exp_r, got $r")
end

# problem
println(divisible_by_all([1:20]))

