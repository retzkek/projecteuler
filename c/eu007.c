// project euler (projecteuler.net) problem 7
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

#define INITIAL_LEN 100
#define INCREASE_LEN 100

typedef struct {
	int *primes;
	int nPrimes;
	int maxPrimes;
	int last;
} primes;

void initPrimes(primes *p)
{
	p->primes = calloc(INITIAL_LEN,sizeof(int));
	p->primes[0] = 2;
	p->primes[1] = 3;
	p->nPrimes = 2;
	p->maxPrimes = INITIAL_LEN;
	p->last = 3;
}

void addPrime(primes *p, int prime)
{
	if (p->nPrimes+1 > p->maxPrimes) {
		p->maxPrimes += INCREASE_LEN;
		p->primes = realloc(p->primes, p->maxPrimes*sizeof(int));
	}
	p->primes[p->nPrimes] = prime;
	p->nPrimes++;
	p->last = prime;
}

int nextPrime(primes *p)
{
	int candidate, next;
	bool isPrime;
	candidate = p->last + 2;
	next = 0;
	while (next == 0) {
		isPrime = true;
		for (int i = 0; i < p->nPrimes; i++) {
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
	addPrime(p,next);
	return next;
}

bool test()
{
	primes p;
	initPrimes(&p);
	for (int i = 3; i <= 6; i++) {
		nextPrime(&p);
	}
	free(p.primes);
	return (p.last == 13);
}

void run()
{
	primes p;
	initPrimes(&p);
	for (int i = 3; i <= 10001; i++) {
		//printf("%4d: %d\n",p.nPrimes,nextPrime(&p));
		nextPrime(&p);
	}
	free(p.primes);
	printf("%d\n",p.last);
}

int main()
{
	return projectEuler(test, run);
}
