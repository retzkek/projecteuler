// project euler (projecteuler.net) problem 1
// solution by Kevin Retzke (retzkek@gmail.com) Novemeber 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

int natMult3or5(int max) 
{
	int result = 0;
	for (int i = 0; i < max; i++)
		if (i%3 == 0 || i%5 == 0)
			result += i;
	return result;
}

int main()
{
	pe_test_eq(natMult3or5(10), 23, "%d")
	printf("%d\n",natMult3or5(1000));
}

