// project euler (projecteuler.net) problem 3
// solution by Kevin Retzke (retzkek@gmail.com) November 2012

#include <stdio.h>

// LargestPrimeFactor returns the largest prime factor of num.
unsigned long largestPrimeFactor(unsigned long num)
{
	unsigned long result, fac;
	result = 1;
	fac = 2;
	while (fac*fac <= num) {
		if (num%fac == 0 && fac > result) {
			result = fac;
			num = num / fac;
		} else {
			fac++;
		}
	}
	if (num != 1) {
		result = num;
	}
	return result;
}

int main()
{
	unsigned long r;
	// test case
	r = largestPrimeFactor(13195);
	if (r == 29) {
		printf("test: pass\n");
	} else {
		printf("test: fail (r=%lu)\n", r);
		return 1;
	}
	// challenge
	r = largestPrimeFactor(600851475143);
	printf("result: %lu\n", r);
	return 0;
}
