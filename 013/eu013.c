// Project Euler problem 13
// Solution by Kevin Retzke, June 2012
#include <stdio.h>
#include <stdlib.h>

typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned char byte;

// simple multi-precision integer
typedef struct {
	byte *digits;
	size_t len;
} integer;

// initialize integer with value 0
integer*
initInteger(size_t len)
{
	// allocate
	byte *d = calloc(len, sizeof(byte));
	integer *newint = malloc(sizeof(integer));
	if (d == NULL || newint == NULL) {
		printf("Error. Unable to allocate new integer of length %zu\n",len);
		free(d);
		free(newint);
		return NULL;
	}
	// initialize
	for (size_t i = 0; i < len; i++) {
		d[i] = 0;
	}
	newint->digits = d;
	newint->len = len;
	return newint;
}

// Create integer and set to value from null-terminated string.
integer*
initIntegerFromString(const char *str, size_t len)
{
	integer *newint = initInteger(len-1);
	if (newint == NULL) return NULL;
	for (size_t i = 0; i < len-1; i++) {
		newint->digits[i] = (int)str[len-2-i]-48;
	}
	return newint;
}

// clean up integer
void 
delInteger(integer *n)
{
	free(n->digits);
	free(n);
}

// print integer
void 
printInteger(integer *n)
{
	for (size_t i = n->len; i > 0; i--) {
		printf("%d",n->digits[i-1]);
	}
	printf("\n");
}

// Set integer value.  If length of num is longer than 
// n->len, value is truncated.
void 
setIntegerFromInt(integer *n, ulong num)
{
	ulong rem = num;
	for (size_t i=0; i<n->len; i++) {
		if (rem == 0) break;
		n->digits[i] = rem%10;
		rem = rem/10;
	}
	if (rem > 0) {
		printf("Warning. Integer set to value [%lu] beyond length [%zu].\n",
				num,n->len);
	}
}

// Add two integers.  They can be different lens, len of return value
// is greater of two argument lens, increased if necessary.
integer*
sumIntegers(integer *n, integer *m)
{
	integer *min, *max;
	if (n->len > m->len) {
		min = m;
		max = n;
	} else {
		min = n;
		max = m;
	}
	integer *newint = initInteger(max->len);
	if (newint == NULL) return NULL;
	for (size_t i=0; i<max->len-1; i++) {
		newint->digits[i] += max->digits[i];
		if (i < min->len) newint->digits[i] += min->digits[i];
		newint->digits[i+1] = newint->digits[i]/10;
		newint->digits[i] = newint->digits[i]%10;
	}
	newint->digits[max->len-1] += max->digits[max->len-1];
	if (min->len == max->len) 
		newint->digits[max->len-1] += min->digits[max->len-1];
	// increase len of result if necessary
	if (newint->digits[max->len-1] >= 10) {
		newint->digits = realloc(newint->digits, (max->len+1)*sizeof(byte));
		newint->len++;
		newint->digits[max->len] = newint->digits[max->len-1]/10;
		newint->digits[max->len-1] = newint->digits[max->len-1]%10;
	}
	return newint;
}

int 
main()
{
	FILE *f;
	const size_t len = 52; // length of numbers+2 for trailing \n\0
	char line[len];
	f = fopen("eu013.dat","r");
	if (f == NULL) {
		return 1;
	}
	integer *n, *oldsum, *newsum;
	oldsum = initInteger(len-2);
	while (fgets(line,len,f) != NULL) {
		n = initIntegerFromString(line,len-1); // omit trailing \0
		newsum = sumIntegers(oldsum, n);
		delInteger(oldsum);
		delInteger(n);
		oldsum = newsum;
	}
	printInteger(oldsum);
	delInteger(oldsum);
	return 0;
}
