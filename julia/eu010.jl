#!/usr/bin/env julia

include("primes.jl")


# test case
exp_r = 17
Primes.eratos(10)
r = sum(Primes.primes)
if r != exp_r
    error("test failed: expected $exp_r, got $r")
end

# problem
Primes.eratos(2000000)
println(sum(Primes.primes))
