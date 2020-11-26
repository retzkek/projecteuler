#!/usr/bin/env julia
using Test

# fib produces consecutive values in the Fibonacci sequence
function fib(ch)
    n0 = BigInt(1)
    n1 = BigInt(1)
    while true
        put!(ch,n0)
        next = n0+n1
        n0 = n1
        n1 = next
    end
end

num_digits(n::BigInt) = length(string(n))


function main()
    ch = Channel{BigInt}(fib)

    # test case
    i = 1
    n = take!(ch)
    while num_digits(n) < 3
        i+=1
        n = take!(ch)
    end
    @test i == 12

    while num_digits(n) < 1000
        i+=1
        n = take!(ch)
    end
    i
end
println(main())
