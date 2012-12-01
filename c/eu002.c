// project euler (projecteuler.net) problem 2
// solution by Kevin Retzke (retzkek@gmail.com) November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

// Fibsum computes the sum of all even-valued members of the Fibonacci
// sequence below max.
int fibsum(int max) 
{
	int fib0, fib1, fibNext, result;
	fib0 = 1;
	fib1 = 2;
	fibNext = 3;
	result = 2;
	while (fib1 < max) {
		fibNext = fib0 + fib1;
		if (fibNext < max && fibNext%2 == 0) {
			result += fibNext;
		}
		fib0 = fib1;
		fib1 = fibNext;
	}
	return result;
}

int main() 
{
	pe_test_eq(fibsum(90), 44, "%d")
	printf("%d\n", fibsum(4e6));
}
