// Simple prime number methods
// Kevin Retzke (retzkek@gmail.com)
// November 2012

#ifndef _PRIMES_H
#define _PRIMES_H

#include <stdlib.h>

#define PRIMES_SIZE_INCREMENT 100

typedef unsigned int prime_t;

typedef struct {
	prime_t *primes;
	size_t numPrimes;
	// housekeeping
	size_t capacity;
} primes_s;

// Initialize new primes instance.
primes_s *primes_new();

// Free primes instance.
void primes_free(primes_s *p);

// Populate primes instance with all primes up to max (using sieve of 
// eratosthenes). Returns number of primes found.
size_t primes_populate(primes_s *p, prime_t max);

// Finds and returns next prime.
prime_t primes_next(primes_s *p);

// Test if num is prime.
bool primes_isPrime(primes_s *p, prime_t num);

#endif
