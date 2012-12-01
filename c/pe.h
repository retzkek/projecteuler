// Simple macros for testing and running project euler problems
// Kevin Retzke (retzkek@gmail.com)
// November 2012

#define pe_test_eq(test, result, fmt) { \
	if ((test) != (result)) { \
		printf("Test failed: " #test " = " #fmt " != " #fmt "\n",(test),(result)); \
		return 1; \
	} \
}
