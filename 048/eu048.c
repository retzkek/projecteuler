// Project Euler problem 48
// Solution by Kevin Retzke, June 2012
#include <stdio.h>
#include <stdlib.h>

typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned int byte;

// print number array
void printArray(byte *array, size_t len)
{
	for (int i = len-1; i >= 0; i--) {
		printf("%d",array[i]);
	}
}


// expand number to array, e.g. 123 -> {3,2,1}
void makeArray(uint num, byte *array, size_t len)
{
	uint rem = num;
	for (uint i=0; i<len; i++) {
		array[i] = rem%10;
		rem = rem/10;
	}
}

// add array2 to array1, results in array1
void addArray(byte *array1, const byte *array2, size_t len)
{
	for (uint i=0; i<len-1; i++) {
		array1[i] = array1[i]+array2[i];
		array1[i+1] += array1[i]/10;
		array1[i] = array1[i]%10;
	}
	array1[len-1] = (array1[len-1]+array2[len-1])%10;
}

// powmod computes the last n digits of base**expo
void powmod(uint base, uint expo, byte *res_array, size_t digits)
{
	byte base_array[digits];
	makeArray(base, base_array, digits);
	makeArray(base, res_array, digits);
	// expand base**expo into base*base*base*...
	for (uint e = 1; e < expo; e++) {
		byte tmp_array[digits];
		makeArray(0, tmp_array, digits);
		// perform long multiplication
		for (uint i = 0; i < digits; i++) {
			for (uint j = 0; j < digits-i; j++) {
				tmp_array[i+j] += res_array[j]*base_array[i];
			}
		}
		// carry and copy to result array
		for (uint i = 0; i < digits-1; i++) {
			tmp_array[i+1] += tmp_array[i]/10;
			res_array[i] = tmp_array[i]%10;
		}
		res_array[digits-1] = tmp_array[digits-1]%10;
	}
}

int main()
{
	static const size_t res_digits = 10;
	byte res_array[res_digits], tmp_array[res_digits];
	makeArray(0,res_array,res_digits);
	for (uint i=1; i<=1000; i++) {
		powmod(i,i,tmp_array,res_digits);
		addArray(res_array,tmp_array,res_digits);
		/*printf("%4d\t",i);
		printArray(tmp_array, res_digits);
		printf("\t");
		printArray(res_array, res_digits);
		printf("\n");*/
	}
	//powmod(999,999,res_array,res_digits);
	printArray(res_array, res_digits);
	printf("\n");
	return 0;
}
