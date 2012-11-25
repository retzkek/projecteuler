// project euler (projecteuler.net) problem 15
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>
#include <gmp.h>

#include "pe.h"

unsigned long paths(unsigned int n)
{
	mpz_t fn, f2n, fSquared,  r;

	mpz_init(fn);
	mpz_fac_ui(fn,n);

	mpz_init(f2n);
	mpz_fac_ui(f2n,2*n);

	mpz_init(fSquared);
	mpz_mul(fSquared,fn,fn);

	mpz_init(r);
	mpz_cdiv_q(r, f2n, fSquared);

	if (!mpz_fits_ulong_p(r)) {
		printf("warning: result exceeds unsigned long\n");
	}
	return mpz_get_ui(r);
}

bool test()
{
	return (paths(2) == 6);
}

void run()
{
	printf("%lu\n",paths(20));
}

int main()
{
	return projectEuler(test,run);
}
