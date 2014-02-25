#!/usr/bin/env julia

# is_palindrome tests if n is palindromic (e.g. 12321)
function is_palindrome(n::Int)
    ss = string(n)
    ss == reverse(ss)
end

# palindrome calculates the largest palindrome made from the product
# of two d-digit numbers.
function palindrome(d::Int)
    start = 10^d-1
    stop = 10^(d-1)
    largest = 0
    for i = start:-1:stop
        for j = i:-1:stop
            n = i*j
            if n > largest && is_palindrome(n)
                largest = n
            end
        end
    end
    largest
end

# test case
exp_r = 9009
r = palindrome(2)
if r != exp_r
    error("test failed: expected $exp_r, got $r")
end

# problem
println(palindrome(3))

