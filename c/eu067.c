// project euler (projecteuler.net) problem 67
// (same as problem 18 with different input)
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

typedef struct {
	int **t;
	int size;
} triangle;

// read a triangle from a text file.
// Example (size=4):
//
//	3
//	7 5
//	2 4 6
//	8 5 9 3
triangle *readTriangleFromFile(char *filename, int size) {
	FILE *f;
	triangle *t;

	t = malloc(sizeof(triangle));
	t->size = size;
	t->t = malloc(size*sizeof(int*));

	f = fopen(filename, "r");
	for (int j = 0; j < size; j++) {
		t->t[j] = malloc((j+1)*sizeof(int));
		for (int i = 0; i < j+1; i++) {
			fscanf(f, "%d", &t->t[j][i]);
		}
	}
	fclose(f);
	return t;
}

// clean up triangle memory.
void cleanTriangle(triangle *t) {
	for (int j=0; j < t->size; j++) {
		free(t->t[j]);
	}
	free(t->t);
	free(t);
}

// Print prints the triangle to stdout.
void printTriangle(triangle *t) {
	for (int j = 0; j < t->size; j++) {
		for (int i = 0; i < j+1; i++) {
			printf("%3d ",t->t[j][i]);
		}
		printf("\n");
	}
}

// compute the maximum sum of all paths from top to bottom.
int maxPathSum(triangle *t) {
	int *row0, *row1;
	row0 = malloc(t->size*sizeof(int));
	for (int i=0; i<t->size; i++) {
		row0[i] = t->t[t->size-1][i];
	}
	for (int j = t->size-2; j >= 0; j--) {
		row1 = malloc((j+1)*sizeof(int));
		for (int i = 0; i < j+1; i++) {
			if (row0[i] > row0[i+1]) {
				row1[i] = t->t[j][i] + row0[i];
			} else {
				row1[i] = t->t[j][i] + row0[i+1];
			}
		}
		free(row0);
		row0 = row1;
	}
	int r = row0[0];
	free(row0);
	return r;
}

bool test()
{
	triangle *t;
	t = readTriangleFromFile("../data/eu018test.dat",4);
	int r = maxPathSum(t);
	cleanTriangle(t);
	return (r == 23);
}

void run()
{
	triangle *t;
	t = readTriangleFromFile("../data/eu067.dat",100);
	//printTriangle(t);
	printf("%d\n",maxPathSum(t));
	cleanTriangle(t);
}

int main()
{
	return projectEuler(test,run);
}
