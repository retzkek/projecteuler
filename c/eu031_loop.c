// project euler (projecteuler.net) problem 31
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
#include <stdio.h>

int countCombinations(const int *val, const int *end, int total) 
{
    if (val > end) {
        return total == 0;
    }
    int count = 0;
    for (int i = 0; i <= total/(*val); ++i) {
        count += countCombinations(val+1, end, total-(*val)*i);
    }
    return count;
}

int main()
{
    static const int coins[] = {200, 100, 50, 20, 10, 5, 2, 1};
    printf("%i\n",countCombinations(&coins[0], &coins[7], 200));
}
