# ! /usr/bin/env python3

"""
Jazmin I. Paz
Lab 01 Python Intro
28 August 2019
"""

import sys  # sys lib used to take 2+ parameters
import re  # regular expression lib used to set character boundaries

freq = {}  # empty dictionary

inputf = open(sys.argv[1], 'r')
outputf = open(sys.argv[2], 'w')

readinput = inputf.read().lower()  # read input file and convert all words to lowercase

allwords = re.findall("[a-z]+", readinput)  # creates list of all words omitting non-alphabetic characters

for word in allwords:
    count = freq.get(word, 0)  # default value of 0 in order to display count (avoid mismatch error)
    freq[word] = count + 1

freqlist = freq.keys()

for words in sorted(freqlist):
    outputf.write(words + " " + str(freq[words]) + "\n")

    
