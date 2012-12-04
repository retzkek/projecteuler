// project euler (projecteuler.net) problem 22
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "pe.h"

#define INITIAL_SIZE 1000
#define INCREMENT_SIZE 500

typedef struct {
	char **names;
	int count;
	int capacity;
} names_t;

// read names from file, formatted one per line, e.g.:
//     BOB
//     TOM
//     HARRY
//     SALLY
names_t *readNamesFromFile(char *filename)
{
	FILE *f;
	names_t *n;
	char *line = NULL;
	size_t len = 0;
	unsigned int slen;

	n = malloc(sizeof(names_t));
	n->count = 0;
	n->capacity = INITIAL_SIZE;
	n->names = malloc(INITIAL_SIZE*sizeof(char*));

	f = fopen(filename, "r");
	if (f == NULL) {
		perror("error opening file");
		return NULL;
	}
	while (true) {
		slen = getline(&line, &len, f);
		if (slen == -1)  break;
		//printf("%s %u\n",line,slen);
		if (n->count+1 > n->capacity) {
			n->capacity += INCREMENT_SIZE;
			n->names = realloc(n->names, n->capacity*sizeof(char*));
		}
		line[slen-1]='\0'; // replace newline with null
		n->names[n->count] = line;
		n->count++;
		line=NULL;
	}
	free(line);
	fclose(f);
	return n;
}

// clean up names structure memory
void cleanNames(names_t *n)
{
	for (int i=0; i < n->count; i++) {
		free(n->names[i]);
	}
	free(n->names);
	free(n);
}

////////////////////////////////////////////////////////////////////////////////
// Quicksort
int qs_partition(char **array, int left, int right, int ipivot)
{
	char *pivot, *tmp;
	
	// move pivot to end
	pivot = array[ipivot];
	array[ipivot] = array[right];
	array[right] = pivot;

	int istore = left;
	for (int i = left; i < right; i++) {
		if (strcmp(array[i], pivot) < 0) {
			tmp = array[i];
			array[i] = array[istore];
			array[istore] = tmp;
			istore++;
		}
	}
	tmp = array[istore];
	array[istore] = array[right];
	array[right] = tmp;

	return istore;
}

void quicksort(char **array, int left, int right)
{
	int ipivot, inew, middle;

	if (right <= left) return;

	// choose pivot as median of (first,middle,last)
	middle = left+(right-left)/2;
	if (strcmp(array[left],array[middle]) < 0 &&
			strcmp(array[middle],array[right]) < 0) {
		ipivot = middle;
	} else if (strcmp(array[left],array[middle]) > 0 &&
			strcmp(array[left],array[right]) < 0) {
		ipivot = left;
	} else {
		ipivot = right;
	}

	inew = qs_partition(array, left, right, ipivot);
	quicksort(array, left, inew-1);
	quicksort(array, inew+1, right);
}
////////////////////////////////////////////////////////////////////////////////

// sort names in-place
void sortNames(names_t *n)
{
	quicksort(n->names, 0, n->count-1);
}

void printNames(names_t *n)
{
	for (int i = 0; i < n->count; i++) {
		printf("%s\n",n->names[i]);
	}
}

// compute sum of character values in str, where 'A'=1. 'B'=2, etc.
int sumCharacterValues(char *str)
{
	int sum = 0;
	for (int i = 0; i < strlen(str); i++) {
		sum += str[i]-'A'+1;
	}
	return sum;
}

int main()
{
	pe_test_eq(sumCharacterValues("COLIN"), 53, "%d");

	names_t *n;
	n = readNamesFromFile("../data/names_formatted.txt");
	if (n == NULL) {
		return 1;
	}
	sortNames(n);
	//printNames(n);
	unsigned long sum = 0;
	for (int i = 0; i < n->count; i++) {
		sum += sumCharacterValues(n->names[i])*(i+1);
	}
	printf("%lu\n",sum);
	cleanNames(n);
}
