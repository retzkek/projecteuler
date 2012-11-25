// project euler (projecteuler.net) problem 6:
// solution by Kevin Retzke (retzkek@gmail.com), November 2009

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

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

bool test()
{
	return (SquareOfSum(10) - SumOfSquares(10) == 2640);
}

void run()
{
	printf("%ld\n", SquareOfSum(100) - SumOfSquares(100));
}

int main()
{
	return projectEuler(test, run);
}
