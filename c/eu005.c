// project euler (projecteuler.net) problem 5:
// solution by Kevin Retzke (retzkek@gmail.com), November 2009

#include <stdio.h>
#include <stdbool.h>

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
	int r;
	// test case
	r = smallestDivisibleBy(10);
	if (r == 2520) {
		printf("test: pass\n");
	} else {
		printf("ttst: fail (result = %d)\n", r);
		return 1;
	}
	// challenge
	r = smallestDivisibleBy(20);
	printf("result: %d\n", r);
	return 0;
}
