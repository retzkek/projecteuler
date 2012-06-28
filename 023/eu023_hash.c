// project euler (projecteuler.net) problem 23
// Solution by Kevin Retzke, June 2012

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

////////////////////////////////////////////////////////////////////////////////
// Utility                                                                    //
////////////////////////////////////////////////////////////////////////////////
int
sumProperDivisors(int n)
{
	int sum = 1;
	int fac = 2;
	while (fac*fac <=n) {
		if (n%fac == 0) {
			sum += fac;
			if (fac*fac != n) {
				sum += n/fac;
			}
		}
		fac++;
	}
	return sum;
}
    
////////////////////////////////////////////////////////////////////////////////
// Main                                                                       //
////////////////////////////////////////////////////////////////////////////////
int
main()
{
	// test that 28 is perfect number
	int s = sumProperDivisors(28);
	if (s != 28) {
		printf("Error. sumProperDivisors(28) = %d, expecting 28.\n",s);
		return 1;
	}
	// problem
    // use a very simple hash-like table to keep track of abundant numbers
    // since the problem told us the maximum value we need to worry about,
    // can just create an array of that size
    const int nmin = 12;
    const int nmax = 28124;
    bool abunds[nmax];
    for (int i = nmin; i < nmax; i++) {
        abunds[i] = sumProperDivisors(i) > i;
    }
    unsigned int result = 0;
    bool include;
    for (int i = 1; i < nmax; i++) {
        include = true;
        for (int j = nmin; j < i; j++) {
            if (!abunds[j]) continue;
            if (abunds[i-j]) {
                include = false;
            }
        }
        if (include) result += i;
    }
    printf("%d\n",result);
}
