// project euler (projecteuler.net) problem 12
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

int triangle(int n)
{
	int t = 0;
	for (int i = 1; i <= n; i++)
		t += i;
	return t;
}

int nFactors(int n)
{
	int r, i;
	r = 0;
	i = 1;
	while (i*i < n) {
		if (n%i == 0)
			r += 2;
		i++;
	}
	return r;
}

int firstOverNFactors(int n)
{
	int i, t, tf;
	i = 1;
	while (true) {
		t = triangle(i);
		tf = nFactors(t);
		if (tf > n) {
			break;
		}
		i++;
	}
	return t;
}

bool test()
{
	return (triangle(7) == 28 && firstOverNFactors(5) == 28);
}

void run()
{
	printf("%d\n",firstOverNFactors(500));
}

int main()
{
	return projectEuler(test,run);
}
