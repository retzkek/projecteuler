// project euler (projecteuler.net) problem 66
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
package main

import (
	"fmt"
	"math"
)

func isSquare(n int64) bool {
    root := math.Sqrt(float64(n))
    test := int64(root+0.5)
    return test*test == n
}

func diophantine(d int64) int64 {
    var x, num int64
    x = 2
    for {
        num = x*x-1
        if num%d == 0 && isSquare(num/d) {
            break
        }
        x++
    }
    return x
}

func main() {
    var maxx, maxd, d int64
    for d = 2; d < 1001; d++ {
        if isSquare(d) {
            continue
        }
        x := diophantine(d)
        fmt.Println(d, x)
        if x > maxx {
            maxx = x
            maxd = d
        }
    }
    fmt.Println(maxd)
}
