// project euler (projecteuler.net) problem 104
// solution by Kevin Retzke (retzkek@gmail.com) April 2012
package main

import (
	"fmt"
    "math/big"
//    "index/suffixarray"
)

// fibonacci returns a closure that calculates the terms of the
// fibonacci sequence, starting with the third (2).
func fibonacci() (func() (int,*big.Int)) {
    nMinus2 := big.NewInt(1)
    nMinus1 := big.NewInt(1)
    k := 2
    return func() (int,*big.Int) {
        n := new(big.Int)
        n.Add(nMinus1,nMinus2)
        nMinus2=nMinus1
        nMinus1=n
        k++
        return k,n
    }
}

func main() {
	fib := fibonacci()
    last9 := new(big.Int)
    last9mod := big.NewInt(1000000000)
    //var last9str string
    for {
        k,n := fib()
        //last9str := suffixarray.New(last9.Mod(n,last9mod).Bytes())
        last9str := last9.Mod(n,last9mod).Bytes()
        fmt.Println(last9str)
        if k == 541 {
            break
        }
    }
}
