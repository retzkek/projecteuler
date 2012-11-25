cc= gcc
#cc= clang
copts=-Wall -pedantic -std=c99 -g

eu004: eu004.c pe.h
	$(cc) $< $(copts) -lm -o $@.bin

eu010: eu010.c pe.h primes.h
	$(cc) $< $(copts) -o $@.bin

eu015: eu015.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

%: %.c pe.h
	$(cc) $< $(copts) -o $@.bin
