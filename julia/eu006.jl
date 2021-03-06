#!/usr/bin/env julia

# calculates the sum of the squares for all integers from 1 to n
function sum_of_squares(n::Int)
    sum(map(x->x*x, 1:n))
end

# calculates the square of the sum for all integers from 1 to n
function square_of_sum(n::Int)
    s = sum(1:n)
    s*s
end

using Test
@test square_of_sum(10) - sum_of_squares(10) == 2640

println(square_of_sum(100) - sum_of_squares(100))
