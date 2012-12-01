// project euler (projecteuler.net) problem 25
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <gmp.h>

#include "pe.h"

typedef struct {
	mpz_t last, curr;
	unsigned int term;
} fib_s;

fib_s *fib_new()
{
	fib_s *fib = malloc(sizeof(fib_s));
	mpz_init_set_ui(fib->last, 1);
	mpz_init_set_ui(fib->curr, 1);
	fib->term = 2;
	return fib;
}

void fib_free(fib_s *fib)
{
	mpz_clear(fib->last);
	mpz_clear(fib->curr);
	free(fib);
}

void fib_next(fib_s *fib)
{
	mpz_t next;
	mpz_init(next);
	mpz_add(next, fib->last, fib->curr);
	mpz_set(fib->last, fib->curr);
	mpz_set(fib->curr, next);
	mpz_clear(next);
	fib->term++;
}

size_t fib_num_digits(fib_s *fib)
{
	char *digits;
	digits = mpz_get_str(NULL,10,fib->curr);
	size_t len = strlen(digits);
	free(digits);
	return len;
}

int main()
{
	fib_s *fib = fib_new();
	while (fib_num_digits(fib) < 1000) {
		fib_next(fib);
	}
	printf("%u\n", fib->term);
	fib_free(fib);
}
