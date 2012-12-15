// project euler (projecteuler.net) problem 9
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
)

/* premises:
 * (1) a + b + c = n
 * (2) a^2 + b^2 = c^2
 * (3) a < b < c
 */

func main() {
	n := 1000
	a := 0
	var b, c int
	found := false
	for !found {
		a++
		// from (1) and (2), solve for b
		b = (n*n - 2*n*a) / (2*n - 2*a)
		// solve for c using (1)
		c = n - a - b
		// check if (2) and (3) hold true
		if (a*a+b*b == c*c) && (b > a) && (c > b) {
			found = true
		}
	}
	fmt.Printf("%d\n", a*b*c)
}
