import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict

from operator import itemgetter

from collections import defaultdict

def getSyllables(word):
	d = cmudict.dict()
	if word == "":
		return 0

	return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]

def updateInfoNewFile():
	freq = defaultdict(int)
	results = []
	output = ""
	with open('wordfreq.txt') as inputfile:
		for line in inputfile:
			items = line.strip().split(',')
			freq[items[1]] = float(items[4])
			
			#Output the line so far
			output = output.strip("\n") + line

			#If missing syllable info, generate it
			if(len(items) == 5):
				syllables = getSyllables(items[1])
				output += "," + str(syllables)

			output = output + "\n"
			
	return output

output = updateInfoNewFile()

f = open('workfile.txt', 'w')
f.write(output)