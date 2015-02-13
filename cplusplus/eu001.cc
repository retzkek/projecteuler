// project euler (projecteuler.net) problem 1

#include <iostream>

#include "pe.h"

int natMult3or5(int max) {
	int result = 0;
	for (int i = 0; i < max; i++)
		if (i%3 == 0 || i%5 == 0)
			result += i;
	return result;
}

int main() {
  pe::test<int>(natMult3or5(10), 23);
  std::cout << natMult3or5(1000) << std::endl;
}

