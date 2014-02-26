#!/usr/bin/env julia

f = open("../data/eu013.dat")

nums = map(BigInt, readlines(f))

println(string(sum(nums))[1:10])
