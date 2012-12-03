// Simple prime number methods
// Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdbool.h>

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

// public methods
primes_s *primes_new()
{
	primes_s *p = malloc(sizeof(primes_s));
	p->primes = calloc(PRIMES_SIZE_INCREMENT, sizeof(prime_t));
	p->capacity = PRIMES_SIZE_INCREMENT;
	p->primes[0] = 2;
	p->primes[1] = 3;
	p->numPrimes = 2;
	return p;
}

void primes_free(primes_s *p)
{
	free(p->primes);
	free(p);
}

size_t primes_populate(primes_s *p, prime_t max)
{
	bool sieve[max];
	for (prime_t i = 0; i < max; i++) {
		sieve[i] = false;
	}
	for (size_t i = 2; i*i < max; i++) {
		if (!sieve[i]) {
			for (size_t j = 2*i; j < max; j += i) {
				sieve[j] = true;
			}
		}
	}
	size_t numAdded = 0;
	for (size_t i = p->primes[p->numPrimes-1]+2; i < max; i++) {
		if (!sieve[i]) {
			primes_add(p, (prime_t)i);
			numAdded++;
		}
	}
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
	// naive add
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

