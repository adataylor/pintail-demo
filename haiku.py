import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict

from operator import itemgetter

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
	total = total.replace("\n", " ")
	total = total.replace(",", " ")
	total = total.replace(".", " ")
	total = total.replace(";", " ")

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
		#return 1
		return 2.0/len(word)
	return rarity

def getSyllables(word):
	d = cmudict.dict()
	if word == "":
		return 0
	try:
		return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]
	except Exception, e:
		return 7

def getRarityAvg(rarityList):
	#print rarityList
	return reduce(lambda x, y: x + y, rarityList) / len(rarityList)

# for word in str.split(" "):
# 	print "Freq of " + word.lower() + " is :"
# 	print getRarity(word)

def makeHaiku():
	text = getMyText()
	syl_count = 0

	options7 = []
	options5 = []

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
			newline = (phraseString, phraseValue)
			options5.append(newline)



		if sum([pair[1] for pair in lump7]) == 7:
			phraseString = ' '.join([pair[0] for pair in lump7])
			print phraseString
			phraseValue = getRarityAvg([pair[2] for pair in lump7])
			newline = (phraseString, phraseValue)
			options7.append(newline)
	
	print "found all options"
	options7 = sorted(options7,key=itemgetter(1))
	options5 = sorted(options5,key=itemgetter(1))

	print "Final Haiku"
	print options5[0]
	print options7[0]
	print options5[1]

makeHaiku()





