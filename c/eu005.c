// project euler (projecteuler.net) problem 5:
// solution by Kevin Retzke (retzkek@gmail.com), November 2009

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

// Calculates the smallest number that is evenly divisible by all 
// integers from 1 to max (inclusive).
int smallestDivisibleBy(int max)
{
	int i;
	bool candidate, found;
	i = 0;
	found = false;
	while (!found) {
		i += max;
		candidate = true;
		for (int j = max; j > max/2-1; j--) {
			if (i%j != 0) {
				candidate = false;
				break;
			}
		}
		found = candidate;
	}
	return i;
}

int main()
{
	pe_test_eq(smallestDivisibleBy(10), 2520, "%d");
	printf("%d\n", smallestDivisibleBy(20));
}
