// project euler (projecteuler.net) problem 31
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
#include <stdio.h>

int countCombinations(int *vals, int ival, int nvals, int total) 
{
	if (ival+1 == nvals) {
        return ((total%vals[ival]) == 0);
	}
	int count = 0;
	if (vals[ival] <= total) {
		count += countCombinations(vals, ival, nvals, total-vals[ival]);
	}
	count += countCombinations(vals, ival+1, nvals, total);
	return count;
}

int main()
{
	int coins[] = {200, 100, 50, 20, 10, 5, 2};
	printf("%i\n",countCombinations(coins, 0, 7, 200));
}
