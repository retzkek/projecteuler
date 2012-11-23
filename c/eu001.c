// project euler (projecteuler.net) problem 1
// solution by Kevin Retzke (retzkek@gmail.com) Novemeber 2012

#include <stdio.h>

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
	int r;
	// test
	r = natMult3or5(10);
	if (r == 23) {
		printf("Test: pass\n");
	} else {
		printf("test: fail (r=%d)\n",r);
		return 1;
	}
	// challenge
	r = natMult3or5(1000);
	printf("result: %d\n",r);
	return 0;
}

