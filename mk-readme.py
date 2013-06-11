#!/usr/bin/env python2.7
"""
Assemble list of languages used to solve each problem; create README.md.
"""

import os
import re

header = """Collection of [Project Euler](http://www.projecteuler.net) 
solutions by [Kevin Retzke](retzkek@gmail.com).

![Official Progress](http://projecteuler.net/profile/retzkek.png)
"""

footer = """
"""

subdirs = ['c','go','misc','python','clojure']
#        ext  : language
langs = {'c'  : 'C', 
         'go' : 'Go',
		 'py' : 'Python',
		 'scm': 'Scheme',
		 'f90': 'Fortran',
		 'erl': 'Erlang',
		 'hs' : 'Haskell',
		 'clj': 'Clojure',
}

def parse_filename(f):
	"""
	Extract problem number and language from filename.
	"""
	problem = f[2:5]
	extension = f.split('.')[-1]
	if extension not in langs.keys():
		# if the extension isn't in our list we don't care about the file
		return (None, None)
	return (problem, langs[extension])

def write_readme(problems):
	lsort = sorted(langs.values())
	# header
	print header
	# count by language
	print 'Number of problems solved (or maybe just started) by language:'
	print
	lcount = {}
	for l in lsort:
		count = 0
		for p,ls in problems.iteritems():
			if l in ls:
				count += 1
		lcount[l]=count
	print 'Language |# Problems'
	print '-------- |----------'
	for l in sorted(lcount, key=lcount.get, reverse=True):
		print '%8s | %5d' % (l, lcount[l])
	print
	# table header
	print 'Full list of problem/language:'
	print
	print 'Problem',
	for l in lsort:
		print '| %7s ' % l,
	print
	print '-------',
	for i in range(len(lsort)):
		print '| --------',
	print
	# table body
	for p in sorted(problems.keys()):
		print '%7s' % p,
		for l in lsort:
			if l in problems[p]:
				print '| %7s ' % 'X',
			else:
				print '|         ',
		print
	# footer
	print footer


if __name__=='__main__':
	cwd=os.getcwd()
	problems={}
	prob_pattern = re.compile(r'eu')
	for s in subdirs:
		files=os.listdir(os.path.join(cwd,s))
		for f in files:
			if not prob_pattern.match(f):
				continue
			(problem, lang) = parse_filename(f)
			if problem is not None and lang is not None:
				if not problem in problems.keys():
					problems[problem]=set()
				problems[problem].add(lang)
	write_readme(problems)






