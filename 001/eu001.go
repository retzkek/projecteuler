// project euler (projecteuler.net) problem 1
// solution by Kevin Retzke (retzkek@gmail.com) April 2012
package main

import (
    "fmt"
)

// Natmult computes the sum of all multiples of the given bases that are
// below max.
func natmult(bases []int, max int) int {
    result := 0
    for i:=0; i<max; i++ {
        for _, b := range bases {
            if i % b == 0 {
                result += i
                break
            }
        }
    }
    return result
}

func main() {
    // test case
    bases := []int{3,5}
    r := natmult(bases, 10)
    if r == 23 {
        fmt.Println("Test: pass")
    } else {
        fmt.Printf("Test: fail (r=%v)\n",r)
    }
    // challenge
    r = natmult(bases, 1000)
    fmt.Printf("Result: %v\n",r)
}
