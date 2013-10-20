import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict

from collections import defaultdict

def makeFreqDict():
	freq = defaultdict(int)
	results = []
	with open('wordfreq.txt') as inputfile:
	    for line in inputfile:
	        items = line.strip().split(',')
	        freq[items[1]] = float(items[4])
	return freq

freq = makeFreqDict()

#str = raw_input("Enter your input: ");

#str = "These are neat words and goojgifhgofw4"
#print "Received input is : ", str

def getMyText():
	total = ""
	with open('raw.txt') as inputfile:
	    for line in inputfile:
	        total += line
	#return "this is a neat pretty test sequence"
	total = total.strip("\n")
	total = total.strip(",")

	return total

def getRarity(word):
	rarity = freq[word.lower()]
	if word == "":
		return 1
	
	#check if plural is in list
	if rarity == 0:
		if freq[word[:-1]] != 0:
			rarity = freq[word[:-1]]

	#Longer words are better, on approx same scale
	if rarity == 0:
		return 2.0/len(word)
	return rarity

def getSyllables(word):
	d = cmudict.dict()
	if word == "":
		return 0

	return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]

def getRarityAvg(rarityList):
	#print rarityList
	return reduce(lambda x, y: x + y, rarityList) / len(rarityList)

# for word in str.split(" "):
# 	print "Freq of " + word.lower() + " is :"
# 	print getRarity(word)

def makeHaiku():
	text = getMyText()
	syl_count = 0

	#options7 = []
	#options5 = []

	line5_1 = ("", 1)
	line7 = ("", 1)
	line5_2 = ("", 1)

	lump7 = []
	lump5 = []

	for word in text.split(" "):
		syl_count = getSyllables(word)
		#print word + " has " + str(syl_count) + " syllables"

		#Manage lumps
		#(word, syllables, rarity)
		wordinfo = (word, getSyllables(word), getRarity(word))

		#Add this word
		lump7.append(wordinfo)
		lump5.append(wordinfo)

		#Manicure the groupings
		while sum([pair[1] for pair in lump5]) > 5:
			if len(lump5) > 0:
				lump5.pop(0)
			else:
				break
		while sum([pair[1] for pair in lump7]) > 7:
			if len(lump7) > 0:
				lump7.pop(0)
			else:
				break

		if sum([pair[1] for pair in lump5]) == 5:
			phraseString = ' '.join([pair[0] for pair in lump5])
			print phraseString

			phraseValue = getRarityAvg([pair[2] for pair in lump5])
			if phraseValue < line5_1[1] or phraseValue < line5_2[1]:
				newline = (phraseString, phraseValue)

				if line5_1[1] < line5_2[1]:
					if newline[1] < line5_2[1]:
						line5_2 = newline
					elif newline[1] < line5_1[1]:
						line5_1 = newline
				if line5_2[1] < line5_1[1]:
					if newline[1] < line5_1[1]:
						line5_1 = newline
					elif newline[1] < line5_2[1]:
						line5_2 = newline



		if sum([pair[1] for pair in lump7]) == 7:
			phraseString = ' '.join([pair[0] for pair in lump7])
			print phraseString
			phraseValue = getRarityAvg([pair[2] for pair in lump7])
			if phraseValue > line7[1]:
				line7 = (phraseString, phraseValue)
	
		
		print "Haiku So Far:"
		print line5_1[0]
		print line7[0]
		print line5_2[0]


makeHaiku()





