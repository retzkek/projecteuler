// project euler (projecteuler.net) problem 10
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"
#include "primes.h"

unsigned long sumPrimes(primes_s *p)
{
	unsigned long sum = 0;
	for (size_t i = 0; i < p->numPrimes; i++) {
		sum += p->primes[i];
	}
	return sum;
}

int main()
{
	primes_s *p = primes_new();
	primes_populate(p, 10);
	pe_test_eq(sumPrimes(p), 17lu, "%lu");

	primes_populate(p, 2e6);
	printf("%lu\n",sumPrimes(p));

	primes_free(p);
}


