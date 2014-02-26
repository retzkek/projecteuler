#!/usr/bin/env julia

triangle(n::Int) = sum(1:n)

function count_factors(n::Int)
    r = 0
    i = 1
    while i*i < n
        if n%i == 0
            r += 2
        end
        i += 1
    end
    r
end

i = 1
while true
    t = triangle(i)
    if count_factors(t) > 500
        println(t)
        break
    end
    i += 1
end
