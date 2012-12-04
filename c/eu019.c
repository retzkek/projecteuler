// project euler (projecteuler.net) problem 19
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>

#include "pe.h"

static int daysInMonth[] = {31,28,31,30,31,30,31,31,30,31,30,31};

int main()
{
	int d, n;
	d = 1;
	n = 0;
	for (int year=1900; year < 2001; year++) {
		for (int month = 0; month < 12; month++) {
			if (year > 1900 && d%7 == 0) {
				n++;
				//printf("%d/%d %d\n",month+1,year,d);
			}
			d += daysInMonth[month];
			// leap year
			if (month == 1 && year%4 == 0) {
				if (year%100 == 0 && year%400 != 0)
					continue;
				d++;
			}
		}
	}
	printf("%d\n",n);
}
