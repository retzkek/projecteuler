// project euler (projecteuler.net) problem 4
// solution by Kevin Retzke (retzkek@gmail.com) November 2012

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#include "pe.h"

// IsPalindrome returns true if num is palindromic.
bool isPalindrome(int num)
{
	size_t strLen, strMaxLen;
	char *str;
	strMaxLen=50;
	str = malloc(sizeof(char)*strMaxLen);
	strLen = snprintf(str, strMaxLen, "%d", num);
	for (int i = 0; i < (int)strLen/2; i++) {
		if (str[i] != str[strLen-i-1]) {
			free(str);
			return false;
		}
	}
	free(str);
	return true;
}

// Palindrome calculates the largest palindrom made from the product of two
// digits-digit numbers.
int palindrome(int digits)
{
	int start, stop, largest, n;
	start = (int)powf(10.0f,(float)digits) - 1;
	stop = (start+1)/10;
	largest = 0;
	for (int i = start; i >= stop; i--) {
		for (int j = i; j >= stop; j--) {
			n = i*j;
			if (isPalindrome(n) && n > largest)
				largest = n;
		}
	}
	return largest;
}

bool test()
{
	return (palindrome(2) == 9009);
}

void run()
{
	printf("%d\n", palindrome(3));
}

int main()
{
	return projectEuler(test,run);
}
