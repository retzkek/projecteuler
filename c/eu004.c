// project euler (projecteuler.net) problem 4
// solution by Kevin Retzke (retzkek@gmail.com) November 2012

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

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
			return false;
		}
	}
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

int main()
{
	int r;
	// test case
	r = palindrome(2); 
	if (r == 9009) {
		printf("test: pass\n");
	} else {
		printf("test: fail (r=%d)\n", r);
		return 1;
	}
	// challenge
	r = palindrome(3);
	printf("result: %d\n", r);
	return 0;
}
