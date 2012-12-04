// project euler (projecteuler.net) problem 21
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

int sumProperDivisors(int n)
{
	int fac, sum;
	sum = 1;
	fac = 2;
	while (fac*fac <= n) {
		if (n%fac == 0) {
			sum += fac;
			if (fac*fac != n) {
				sum += n/fac;
			}
		}
		fac++;
	}
	return sum;
}

int main()
{
	pe_test_eq(sumProperDivisors(220), 284, "%d");
	pe_test_eq(sumProperDivisors(284), 220, "%d");

	static const int max_n = 10000;
	int sums[max_n];
	int sum;
	for (int i = 2; i < max_n; i++) {
		sums[i] = sumProperDivisors(i);
	}
	sum = 0;
	for (int i = 2; i < max_n; i++) {
		if (sums[i] < max_n) {
			if (sums[i] != i && sums[sums[i]] == i) {
				sum += i;
			}
		}
	}
	printf("%d\n",sum);
}
