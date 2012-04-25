#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 59
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #59
===========
Each character on a computer is assigned a unique code and the preferred 
standard is ASCII (American Standard Code for Information Interchange). For 
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage 
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text 
message, and the key is made up of random bytes. The user would keep the 
encrypted message and the encryption key in different locations, and without 
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified 
method is to use a password as a key. If the password is shorter than the 
message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for 
security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum 
of the ASCII values in the original text.
"""

def frequency(cipher,keylen=1):
    """
    Count number of occurances of each (keylen)th element in cipher.
    Returns list of len keylen where each element is a dictionary
    of the frequency of each unique element.
    """
    freqs = []
    for i in xrange(keylen):
        freq={}
        for j in xrange(i,len(cipher),keylen):
            if cipher[j] in freq:
                freq[cipher[j]] += 1
            else:
                freq[cipher[j]] = 1
        freqs.append(freq)
    return freqs

def printFreqs(freqs):
    vals=set()
    for f in freqs:
        vals = vals | set(f.keys())
    for v in vals:
        print "%2i:" % v,
        for i in range(len(freqs)):
            print " %4i" % freqs[i].get(v,0),
        print

def xor(cipher,keys):
    """
    Sequentially xor keys with cipher.
    """
    plaintext = []
    keylen = len(keys)
    for i in xrange(len(cipher)):
        plaintext.append(cipher[i] ^ keys[i%keylen])
    return plaintext

if __name__ == '__main__':
    f = open('cipher1.txt')
    cipher = map(int,f.readline().rstrip().split(','))
    f.close()
    keylen=3
    freqs = frequency(cipher,keylen)
    printFreqs(freqs)
    keys=[]
    for freq in freqs:
        # we assume the most common character in the plaintext is ' '
        # (it should be 'e' if spaces were removed from the plaintext
        # prior to encryption - in this case they weren't)
        keys.append(freq.keys()[freq.values().index(max(freq.values()))] 
            ^ ord(' '))
    print map(chr,keys)
    text = xor(cipher,keys)
    print "".join(map(chr,text))
    print sum(text)

