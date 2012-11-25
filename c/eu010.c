// project euler (projecteuler.net) problem 10
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"
#include "primes.h"

bool test()
{
	primes p;
	initPrimes(&p);
	int sum = 5;
	while (p.last < 10) {
		sum += nextPrime(&p);
	}
	sum -= p.last;
	free(p.primes);
	return (sum == 17);
}

void run()
{
	primes p;
	initPrimes(&p);
	long sum = 5;
	while (p.last < 2e6) {
		sum += nextPrime(&p);
	}
	sum -= p.last;
	free(p.primes);
	printf("%ld\n",sum);
}

int main()
{
	return projectEuler(test,run);
}


