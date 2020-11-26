#!/usr/bin/env julia

include("primes.jl")

function main()
    n=0
    for i = length(Primes.primes)+1:10001
        n = Primes.next_prime()
    end
    n
end

println(main())
