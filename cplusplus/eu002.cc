// project euler (projecteuler.net) problem 2

#include <iostream>

#include "pe.h"

// Fibsum computes the sum of all even-valued members of the Fibonacci
// sequence below max.
int fibsum(int max) {
	int fib0 = 1;
	int fib1 = 2;
	int fibNext = 3;
	int result = 2;
	while (fib1 < max) {
		fibNext = fib0 + fib1;
		if (fibNext < max && fibNext%2 == 0) {
			result += fibNext;
		}
		fib0 = fib1;
		fib1 = fibNext;
	}
	return result;
}

int main() {
  pe::test<int>(fibsum(90), 44);
  std::cout << fibsum(4e6) << std::endl;
}
