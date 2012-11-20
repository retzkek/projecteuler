#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 220
solution by Kevin Retzke, April 2009

Let D_(0) be the two-letter string "Fa". For n≥1, derive D_(n) from D_(n-1) by the string-rewriting rules:

"a" → "aRbFR"
"b" → "LFaLb"

Thus, D_(0) = "Fa", D_(1) = "FaRbFR", D_(2) = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics program, with "F" meaning "draw forward one unit", "L" meaning "turn left 90 degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being ignored. The initial position of the computer cursor is (0,0), pointing up towards (0,1).

Then D_(n) is an exotic drawing known as the Heighway Dragon of order n. For example, D_(10) is shown below; counting each "F" as one step, the highlighted spot at (18,16) is the position reached after 500 steps.

(drawing omitted)

What is the position of the cursor after 10^(12) steps in D_(50) ?
Give your answer in the form x,y with no spaces.
"""

import re

class dragon:
    rule = 'Fa'

    def next(self):
        # replace a and b 
        # note that the replacement strings use A and B 
        self.rule = re.sub(r'a',r'ARBFR',self.rule)
        self.rule = re.sub(r'b',r'LFALB',self.rule)
        # replace the temporary A and B
        self.rule = re.sub(r'A',r'a',self.rule)
        self.rule = re.sub(r'B',r'b',self.rule)
        return self.rule
        

if __name__ == '__main__':
    d = dragon()
    for i in range(10):
        #print d.next()
        cmd = d.next()
        print i+1, cmd.count('F'), cmd.count('R'), cmd.count('L')
        


