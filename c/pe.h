// Simple framework for running project euler problems
// Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

int projectEuler(bool (*test)(), void (*run)())
{
	if (test == NULL) {
		printf("no test\n");
	} else {
		if (!test()) {
			printf("test failed\n");
			return 1;
		}
	}
	run();
	return 0;
}
