from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
from nltk.tag.simplify import simplify_wsj_tag

from db import init_word
from db import Word

def __syllables__(word):
	print "Doing syllables lookup for", word
	d = cmudict.dict()
	if word == '':
		return 0
	return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word]][0]

def __frequency__(word):
	print "Doing frequency lookup for", word
	minfreq = 10**-6 # Right now, we have no really good method here...
	return minfreq

# Expensive contextless word PoS lookup...
def __part_of_speech__( word ):
	print "Doing POS lookup for", word
	tagged_sent = nltk.pos_tag([word])
	return simplify_wsj_tag(tagged_sent[0][1])

def syllables( word ):
	word = word.lower()
	db = init_word()
	w = db.query(Word).get(word)
	if w and w.syllables:
		return w.syllables
	# If we get here, we're going to have to make a call to __syllables__
	if not w:
		w = Word()
		w.word = word
		db.add(w)
	w.syllables = __syllables__(word)
	db.commit()
	return w.syllables

def frequency( word ):
	word = word.lower()
	db = init_word()
	w = db.query(Word).get(word)
	if w and w.frequency:
		return w.frequency
	# If we get here, we're going to have to make a call to __frequency__
	if not w:
		w = Word()
		w.word = word
		db.add(w)
	w.frequency = __frequency__(word)
	db.commit()
	return w.frequency	
