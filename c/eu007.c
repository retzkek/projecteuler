// project euler (projecteuler.net) problem 7
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "primes.h"
#include "pe.h"

int main()
{
	primes_s *p = primes_new();
	while (p->numPrimes < 6) {
		primes_next(p);
	}
	pe_test_eq(p->primes[5], 13u, "%u");

	while (p->numPrimes < 10001) {
		primes_next(p);
	}
	printf("%u\n", p->primes[10000]);
	primes_free(p);
}
