cc= gcc
#cc= clang
copts=-Wall -pedantic -std=gnu11 -g -O3

primes: primes.c primes.h
	$(cc) $< $(copts) -c

primes_test: primes_test.c primes
	$(cc) $< primes.o $(copts) -o $@.bin

eu004: eu004.c pe.h
	$(cc) $< $(copts) -lm -o $@.bin

eu010: eu010.c pe.h primes
	$(cc) $< primes.o $(copts) -o $@.bin

eu015: eu015.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

eu016: eu016.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

eu020: eu020.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

eu025: eu025.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

eu041: eu041.c pe.h primes
	$(cc) $< primes.o $(copts) -o $@.bin

%: %.c pe.h
	$(cc) $< $(copts) -o $@.bin
