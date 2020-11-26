#!/usr/bin/env julia

triangle(n::Int) = sum(1:n)

function count_factors(n::Int)
    r = 0
    for i = 1:Int(ceil(sqrt(n)))
        if n%i == 0
            r += 2
        end
    end
    r
end

function main()
    i = 1
    while true
        t = triangle(i)
        if count_factors(t) > 500
            println(t)
            break
        end
        i += 1
    end
end

main()
