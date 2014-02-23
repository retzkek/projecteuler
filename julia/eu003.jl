#!/usr/bin/env julia

function largest_prime_factor(n::Int)
    r = 1
    fac = 2
    while fac*fac <= n
        if n%fac == 0 && n > r
            r = fac
            n = n/fac
        else
            fac+=1
        end
    end
    if n != 1
        return n
    end
    r
end

# test case
exp_r = 29
r = largest_prime_factor(13195)
if r != exp_r
    println("test failed: expected $exp_r, got $r")
end

# problem
println(largest_prime_factor(600851475143))

