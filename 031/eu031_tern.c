// project euler (projecteuler.net) problem 31
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
#include <stdio.h>

int countCombinations(int *vals, int ival, int nvals, int total) 
{
	if (ival == nvals) {
        return total == 0;
	}
	return countCombinations(vals, ival+1, nvals, total) +
           ((vals[ival] <= total) ? countCombinations(vals, ival, nvals, total-vals[ival]) : 0);
}

int main()
{
	int coins[] = {200, 100, 50, 20, 10, 5, 2, 1};
	printf("%i\n",countCombinations(coins, 0, 8, 200));
}
