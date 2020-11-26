#!/usr/bin/env julia

f = open("../data/eu013.dat")

nums = map(x -> parse(BigInt,x), readlines(f))

println(string(sum(nums))[1:10])
