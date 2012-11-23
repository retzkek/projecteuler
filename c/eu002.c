// project euler (projecteuler.net) problem 2
// solution by Kevin Retzke (retzkek@gmail.com) November 2012

#include <stdio.h>

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
	int r;
	// test case
	r = fibsum(90);
	if (r == 44) {
		printf("test: pass\n");
	} else {
		printf("test: fail (r=%d)\n", r);
		return 1;
	}
	// challenge
	r = fibsum(4e6);
	printf("result: %d\n", r);
	return 0;
}
