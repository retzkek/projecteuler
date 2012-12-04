// project euler (projecteuler.net) problem 10
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"
#include "primes.h"

unsigned long sumPrimes(primes_s *p, prime_t max)
{
	unsigned long sum = 0;
	for (size_t i = 0; p->primes[i] < max; i++) {
		sum += p->primes[i];
	}
	return sum;
}

int main()
{
	primes_s *p = primes_new();
	primes_populate(p, 10);
	pe_test_eq(sumPrimes(p,10), 17lu, "%lu");

	primes_populate(p, 2e6);
	printf("%lu\n",sumPrimes(p, 2e6));

	primes_free(p);
}


