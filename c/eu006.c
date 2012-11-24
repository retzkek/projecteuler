// project euler (projecteuler.net) problem 6:
// solution by Kevin Retzke (retzkek@gmail.com), November 2009

#include <stdio.h>

// SumOfSquares calculates the sum of the squares for all natural 
// numbers from 1 to max.
long SumOfSquares(int max)
{
	long sum = 0;
	for (int i = 1; i <= max; i++) {
		sum += i * i;
	}
	return sum;
}

// SquareOfSum calculates the square of the sum for all natural numbers
// from 1 to max.
long SquareOfSum(int max)
{
	long sum = 0;
	for (int i = 1; i <= max; i++) {
		sum += i;
	}
	return sum * sum;
}

int main()
{
	long r;
	// test case
	r = SquareOfSum(10) - SumOfSquares(10);
	if (r == 2640) {
		printf("test: pass\n");
	} else {
		printf("test: fail (result = %ld)\n", r);
		return 1;
	}
	// challenge
	r = SquareOfSum(100) - SumOfSquares(100);
	printf("result: %ld\n", r);
	return 0;
}
