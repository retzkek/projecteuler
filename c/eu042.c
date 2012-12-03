// project euler (projecteuler.net) problem 42
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "pe.h"

#define WORDS_INCREMENT_SIZE 500

typedef struct {
	char **words;
	int count;
	int capacity;
} words_s;

// read words from file, formatted one per line, e.g.:
//     BOB
//     TOM
//     HARRY
//     SALLY
words_s *words_read(char *filename)
{
	words_s *w = malloc(sizeof(words_s));
	w->count = 0;
	w->capacity = WORDS_INCREMENT_SIZE;
	w->words = malloc(WORDS_INCREMENT_SIZE*sizeof(char*));

	FILE *f = fopen(filename, "r");
	if (f == NULL) {
		perror("error opening file");
		return NULL;
	}

	char *line = NULL;
	while (true) {
		size_t len = 0;
		unsigned int slen = getline(&line, &len, f);
		if (slen == -1)  break;
		//printf("%s %u\n",line,slen);
		if (w->count+1 > w->capacity) {
			w->capacity += WORDS_INCREMENT_SIZE;
			w->words = realloc(w->words, w->capacity*sizeof(char*));
		}
		line[slen-1]='\0'; // replace newline with null
		w->words[w->count] = line;
		w->count++;
		line=NULL;
	}
	free(line);
	fclose(f);
	return w;
}

// free up words structure memory
void words_free(words_s *w)
{
	for (int i=0; i < w->count; i++) {
		free(w->words[i]);
	}
	free(w->words);
	free(w);
}

// compute sum of character values in str, where 'A'=1. 'B'=2, etc.
int sumCharacterValues(char *str)
{
	int sum = 0;
	for (int i = 0; i < strlen(str); i++) {
		sum += str[i]-'A'+1;
	}
	return sum;
}

#define SEQ_INCREMENT 100

// seq_s stores a sequence of unsigned ints, where ns[i] = seqf(i)
// and seqf(i) < seqf(i+1)
typedef struct {
	unsigned int *ns;
	unsigned int count, capacity;
	unsigned int (*seqf)(unsigned int n);
} seq_s;

// Initialize and return new sequence struct
seq_s *seq_new(unsigned int (*seqf)(unsigned int n))
{
	seq_s *s = malloc(sizeof(seq_s));
	s->ns = malloc(SEQ_INCREMENT*sizeof(unsigned int));
	s->count = 1;
	s->capacity = SEQ_INCREMENT;
	s->seqf = seqf;
	s->ns[0] = s->seqf(0);
	return s;
}

void seq_free(seq_s *s)
{
	free(s->ns);
	free(s);
}

void seq_next(seq_s *s)
{
	if (s->count+1 > s->capacity) {
		s->capacity += SEQ_INCREMENT;
		s->ns = realloc(s->ns, s->capacity*sizeof(unsigned int));
	}
	s->ns[s->count] = s->seqf(s->count);
	s->count++;
}

bool seq_contains(seq_s *s, unsigned int n)
{
	while (s->ns[s->count-1] < n) {
		seq_next(s);
	}
	bool found = false;
	for (int i = 0; i < s->count; i++) {
		if (s->ns[i] == n) {
			found = true;
			break;
		}
	}
	return found;
}

unsigned int triangle(unsigned int n)
{
	return n*(n+1)/2;
}

int main()
{
	seq_s *t = seq_new(triangle);
	pe_test_eq(sumCharacterValues("SKY"), 55, "%d");
	pe_test_eq(seq_contains(t,55), true, "%d");

	words_s *w = words_read("../data/words_formatted.txt");
	if (w == NULL) return 1;
	int count = 0;
	for (int i = 0; i < w->count; i++) {
		if (seq_contains(t,sumCharacterValues(w->words[i]))) count++;
	}
	printf("%d\n",count);

	words_free(w);
	seq_free(t);
}
