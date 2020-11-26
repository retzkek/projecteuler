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

using Test
@test divisible_by_all(collect(1:10)) == 2520

# problem
println(divisible_by_all(collect(1:20)))
