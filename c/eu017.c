// project euler (projecteuler.net) problem 17
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "pe.h"

char *numToWords(unsigned int num)
{
	static char *digits[] = {"zero","one","two","three","four","five",
		"six","seven","eight","nine","ten","eleven","twelve","thirteen",
		"fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};
	static char *tens[] = {"zero","ten","twenty","thirty","forty",
		"fifty","sixty","seventy","eighty","ninety"};
	char *str0 = NULL, *str1 = NULL, *str2 = NULL;
	if (num < 20) {
		asprintf(&str0,"%s",digits[num]);
	} else if (num < 100) {
		asprintf(&str0,"%s",tens[num/10]);
		if (num%10 > 0) {
			str1 = numToWords(num%10);
			asprintf(&str2,"%s-%s",str0,str1);
			free(str0);
			free(str1);
			str0=str2;
		}
	} else if (num < 1000) {
		asprintf(&str0,"%s hundred",digits[num/100]);
		if (num%100 > 0) {
			str1 = numToWords(num%100);
			asprintf(&str2,"%s and %s",str0,str1);
			free(str0);
			free(str1);
			str0=str2;
		}
	} else if (num < 1000000) {
		str1 = numToWords(num/1000);
		asprintf(&str0,"%s thousand",str1);
		free(str1);
		if (num%1000 > 0) {
			str1 = numToWords(num%1000);
			asprintf(&str2,"%s and %s",str0,str1);
			free(str0);
			free(str1);
			str0=str2;
		}
	}
	return str0;
}

int countLetters(char *str)
{
	int c = 0;
	for (int i=0; i<strlen(str); i++) {
		if (str[i] != ' ' && str[i] != '-') 
			c++;
	}
	return c;
}

int main()
{
	char *str;

	str = numToWords(342);
	pe_test_eq(countLetters(str), 23, "%d")
	free(str);

	str = numToWords(115);
	pe_test_eq(countLetters(str), 20, "%d")
	free(str);

	int cnt = 0;
	for (int i = 1; i <= 1000; i++) {
		str = numToWords(i);
		cnt += countLetters(str);
		free(str);
	}
	printf("%d\n",cnt);
}
