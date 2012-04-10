#!/usr/bin/python
# encoding: utf-8

def numToWords(num, spaces=True):
    """
    returns the word representation of num.
    e.g. 225 would return "two hundred and twenty-five"
    if spaces=False spaces, 'and', and hyphens are ommitted
    e.g. "twohundredandtwentyfive"
    """
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    string = ''
    if num < 20:
        string += digits[num]
    elif num < 100:
        string += tens[int(num / 10)]
        if num % 10 > 0 :
            if spaces: string += '-'
            string += digits[num % 10]
    elif num < 1000:
        string += digits[int(num / 100)] 
        if spaces: string += ' '
        string += 'hundred'
        if num % 100 > 0:
            if spaces: string += ' '
            string += 'and'
            if spaces: string += ' '
            string += numToWords(num % 100, spaces)
    elif num < 1000000:
        string += numToWords(int(num / 1000)) 
        if spaces: string += ' '
        string += 'thousand'
        if num % 1000 > 0:
            if spaces: string += ' '
            string += 'and'
            if spaces: string += ' '
            string += numToWords(num % 1000)
    return string

def main():
    # test cases
    n = 342
    ns = numToWords(n, False)
    print n, ns
    print "%i letters" % len(ns)
    if len(ns) == 23:
        print "okay"
    n = 115
    ns = numToWords(n, False)
    print n, ns
    print "%i letters" % len(ns)
    if len(ns) == 20:
        print "okay"
    # problem
    cnt = 0
    for i in range(1,1001):
        str = numToWords(i, False)
        cnt += len(str)
    print cnt 
        

if __name__ == "__main__":
    main()
