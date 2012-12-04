#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdbool.h>

#include "primes.h"

#define TEST_NUMS 1000
#define MAX_NUM RAND_MAX/100

int main()
{
	primes_s *p = primes_new();
	primes_populate(p, MAX_NUM);

	srandom(time(NULL));

	unsigned int nPrime = 0;
	for (unsigned int i = 0; i < TEST_NUMS; i++) {
		long int n = random()/100;
		if (primes_isPrime(p,n)) nPrime++;
	}
	printf("%u / %u primes\n",nPrime,TEST_NUMS);
	primes_free(p);
}

