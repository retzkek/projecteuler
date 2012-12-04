// project euler (projecteuler.net) problem 20
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>
#include <gmp.h>
#include <string.h>
#include <stdlib.h>

#include "pe.h"

int sumDigitsFac(unsigned long n)
{
	mpz_t fn;
	char *digits;
	char digit[] = "x";
	int sum;

	mpz_init(fn);
	mpz_fac_ui(fn,n);

	digits = mpz_get_str(NULL,10,fn);
	sum = 0;
	for (int i = 0; i < strlen(digits); i++) {
		digit[0] = digits[i];
		sum += atoi(digit);
	}
	free(digits);
	mpz_clear(fn);
	return sum;
}

int main()
{
	pe_test_eq(sumDigitsFac(10), 27, "%d");

	printf("%d\n",sumDigitsFac(100));
}
