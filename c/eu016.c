// project euler (projecteuler.net) problem 16
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>
#include <gmp.h>
#include <string.h>
#include <stdlib.h>

#include "pe.h"

int sumDigitsPow(unsigned long base, unsigned long exp)
{
	mpz_t n;
	char *digits;
	char digit[] = "x";
	int sum;

	mpz_init(n);
	mpz_ui_pow_ui(n,base,exp);
	digits = mpz_get_str(NULL,10,n);
	sum = 0;
	for (int i=0; i < strlen(digits); i++) {
		digit[0] = digits[i];
		sum += atoi(digit);
	}
	free(digits);
	mpz_clear(n);
	return sum;
}


bool test()
{
	return (sumDigitsPow(2,15) == 26);
}

void run()
{
	printf("%d\n",sumDigitsPow(2,1000));
}

int main()
{
	return projectEuler(test,run);
}
