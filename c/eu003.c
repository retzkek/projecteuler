// project euler (projecteuler.net) problem 3
// solution by Kevin Retzke (retzkek@gmail.com) November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

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
	pe_test_eq(largestPrimeFactor(13195), 29ul, "%lu");
	printf("%lu\n", largestPrimeFactor(600851475143));
}
