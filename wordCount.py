# ! /usr/bin/env python3

"""
Jazmin Idhali Paz
Lab 01 Python Intro
28 August 2019
"""

import sys  # sys lib used to take 2+ parameters
import re  # regular expression lib used to set boundaries for characters

freq = {}  # empty dictionary
pattern = re.compile(r'[a-z]+')  # the re pattern I used to find only alphabetic words

inputf = open(sys.argv[1], 'r')
outputf = open(sys.argv[2], 'w')

readinput = inputf.read().lower()  # read input file and convert all words to lowercase (case-insensitive)
allwords = re.findall(pattern, readinput)  # creates list of all words within character boundaries w/ specified pattern

for word in allwords:
    count = freq.get(word, 0)  # default value of 0 in order to display count (avoid mismatch error)
    freq[word] = count + 1

freqlist = freq.keys()

for words in sorted(freqlist):  # sort in alphabetical order with sorted()
    outputf.write(words + " " + str(freq[words]) + "\n")
