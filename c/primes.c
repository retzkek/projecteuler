// Simple prime number methods
// Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdbool.h>
#include <string.h>

#include "primes.h"

// private methods
static void primes_add(primes_s *p, prime_t prime)
{
	if (p->numPrimes+1 > p->capacity) {
		p->capacity += PRIMES_SIZE_INCREMENT;
		p->primes = realloc(p->primes, p->capacity*sizeof(prime_t));
	}
	p->primes[p->numPrimes] = prime;
	p->numPrimes++;
}

static void primes_init(primes_s *p)
{
	p->primes = calloc(PRIMES_SIZE_INCREMENT, sizeof(prime_t));
	p->capacity = PRIMES_SIZE_INCREMENT;
	p->primes[0] = 2;
	p->numPrimes = 1;
}

// public methods
primes_s *primes_new()
{
	primes_s *p = malloc(sizeof(primes_s));
	primes_init(p);
	return p;
}

void primes_free(primes_s *p)
{
	free(p->primes);
	free(p);
}

size_t primes_populate(primes_s *p, prime_t max)
{
	if (p->primes) {
		free(p->primes);
		primes_init(p);
	}
	size_t slen = max/2+1;
	// sieve only stores odds, i.e.
	// index:  0 1 2 3 4  5  6  7  8  9 10 11 12
	//   num:  0 3 5 7 9 11 13 15 17 19 21 23 25
	bool *sieve = malloc(slen*sizeof(bool));
	memset(sieve, 0, slen*sizeof(bool));
	for (size_t i = 1; i < slen; i++) {
		if (!sieve[i]) {
			size_t inc = 2*i+1;
			for (size_t j = 3*i+1; j < slen; j += inc) {
				sieve[j] = true;
			}
		}
	}
	size_t numAdded = 0;
	for (size_t i = 1; i < slen; i++) {
		if (!sieve[i]) {
			primes_add(p, (prime_t)(2*i+1));
			numAdded++;
		}
	}
	free(sieve);
	return numAdded;
}

prime_t primes_next(primes_s *p)
{
	prime_t candidate, next;
	candidate = p->primes[p->numPrimes-1] + 2;
	next = 0;
	while (next == 0) {
		bool isPrime = true;
		for (size_t i = 0; i < p->numPrimes; i++) {
			if (candidate % p->primes[i] == 0) {
				isPrime = false;
				candidate += 2;
				break;
			}
			if (p->primes[i]*p->primes[i] > candidate) {
				break;
			}
		}
		if (isPrime) {
			next = candidate;
		}
	}
	primes_add(p,next);
	return next;
}

bool primes_isPrime(primes_s *p, prime_t num)
{
	while (p->primes[p->numPrimes-1] < num) {
		primes_next(p);
	}
	// naive search
	bool isPrime = false;
	for (size_t i = 0; i < p->numPrimes; i++) {
		if (p->primes[i] == num) {
			isPrime = true;
			break;
		}
	}
	return isPrime;
}

