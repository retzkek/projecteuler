#!/usr/bin/env julia

## premises:
## (1) a + b + c = n
## (2) a^2 + b^2 = c^2
## (3) a < b < c

n = 1000
a = 0
b = 0
c = 0
found = false
while !found
    a+=1
    ## from (1) and (2), solve for b
    b = int((n*n - 2*n*a) / (2*n - 2*a))
    ## solve for c using (1)
    c = n - a - b
    ## check if (2) and (3) hold true
    found = b > a && c > b && a*a+b*b == c*c
end
println(a*b*c)
