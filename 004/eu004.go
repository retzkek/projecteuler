// project euler (projecteuler.net) problem 4
// solution by Kevin Retzke (retzkek@gmail.com) April 2012
package main

import (
	"fmt"
    "math"
)

// Reverse reverses and integer, e.g. 123 returns 321.
func reverse(num int) int {
    var digits, result int
    for digits=1;int(math.Pow10(digits))<num;digits++ {}
    for i:=1;i<=digits;i++ {
        result += (num%int(math.Pow10(i)))*int(math.Pow10(digits-i))
    }
    return result
}

// IsPalindrome returns true if num is palindromic.
func isPalindrome(num int) bool {
    return true
}

// Palindrome calculates the largest palindrom made from the product of two
// digits-digit numbers.  The return values are the two numbers and the
// product.
func palindrome(digits int) (int, int, int) {
    var start, stop, num0, num1, largest int
    start = int(math.Pow10(digits))-1
    stop = int(math.Pow10(digits-1))
    for i:=start;i>=stop;i-- {
        for j:=i;j>=stop;j-- {
            if n:=i*j; isPalindrome(n) && n > largest {
                largest = n
                num0 = i
                num1 = j
                fmt.Println(i,j,n)
            }
        }
    }
    return num0, num1, largest
}

func main() {
	var a, b, r int
    fmt.Println(1234,reverse(1234))
	// test case
	if a,b,r = palindrome(2); r == 9009 {
		fmt.Println("Test: pass")
	} else {
		fmt.Printf("Test: fail (r=%v (%v * %v))\n", r, a, b)
	}
	// challenge
	//a,b,r = palindrome(3)
	//fmt.Printf("Result: %v (%i * %i)\n", r, a, b)
}
