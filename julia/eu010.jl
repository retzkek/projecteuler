#!/usr/bin/env julia

include("primes.jl")

using Test
Primes.eratos(10)
@test sum(Primes.primes)==17

# problem
Primes.eratos(2000000)
println(sum(Primes.primes))
