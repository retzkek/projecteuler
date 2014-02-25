#!/usr/bin/env julia

include("primes.jl")

n=0
for i = length(Primes.primes)+1:10001
    n = Primes.next_prime()
end
println(n)
