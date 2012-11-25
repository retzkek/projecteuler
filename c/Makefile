cc= gcc
#cc= clang
copts=-Wall -pedantic -std=gnu1x -g

eu004: eu004.c pe.h
	$(cc) $< $(copts) -lm -o $@.bin

eu010: eu010.c pe.h primes.h
	$(cc) $< $(copts) -o $@.bin

eu015: eu015.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

eu016: eu016.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

eu020: eu020.c pe.h
	$(cc) $< $(copts) -lgmp -o $@.bin

%: %.c pe.h
	$(cc) $< $(copts) -o $@.bin
