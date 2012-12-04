// project euler (projecteuler.net) problem 14
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#include "pe.h"

#define MAX_N 1000000

int countn[MAX_N];

long next(long n)
{
	if (n%2 == 0) {
		return n/2;
	} else {
		return 3*n+1;
	}
}

int count(int n)
{
	int i = 1;
	long m = n;
	while (m > 1) {
		i++;
		m = next(m);
		if (m < MAX_N) {
			if (countn[m] > 0) {
				i += countn[m];
				break;
			}
		}
	}
	countn[n] = i;
	return i;
}

int main()
{
	memset(&countn[0], 0, MAX_N);
	pe_test_eq(count(13), 10, "%d");

	long m, max;
	int imax = 0;
	max = 0;
	for (int i = 1; i < MAX_N; i++) {
		m = count(i);
		if (m > max) {
			max = m;
			imax = i;
		}
	}
	printf("%d\n",imax);
}
