// project euler (projecteuler.net) problem 41
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"
#include "primes.h"

bool isPandigital(unsigned int num)
{
	// determine order of magnitude
	unsigned int mag = 0;
	for (unsigned int n = num; n > 0; n = n/10) {
		mag++;
	}
	// find digits in num
	bool digits[mag];
	for (unsigned int i = 0; i < mag; i++) {
		digits[i] = false;
	}
	for (unsigned int n = num; n > 0; n = n/10) {
		int i = n%10 - 1;
		if (i == -1) {
			return false;
		}
		if (i < mag && !digits[i]) {
			digits[i] = true;
		}
	}
	// check if num contains all digits 1:mag
	for (unsigned int i = 0; i < mag; i++) {
		if (!digits[i]) return false;
	}
	return true;
}

int main()
{
	primes_s *p = primes_new();
	printf("%lu\n",primes_populate(p, 987654321));

	pe_test_eq(primes_isPrime(p,2143), true, "%d");
	pe_test_eq(isPandigital(2143), true, "%d");

	for (size_t n = p->numPrimes-1; n > 0; n--) {
		if (isPandigital(p->primes[n])) {
			printf("%u\n",p->primes[n]);
			break;
		}
	}
	primes_free(p);
}


