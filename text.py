from nltk.tokenize import word_tokenize, sent_tokenize
from db import *

# TODO: This file is a mess. There is a ton of stuff to be done here...
# Really, we shouldn't be relying on any function here, with the possible
# Exception of tag.

# Damn this is a hack...
def sentify( text ):
	sents = []
	for line in text.split('\n'):
		tokens = [word for sent in sent_tokenize(line.strip()) for word in word_tokenize(sent)]
		sent = []
		for tok in tokens:
			if tok in ',-.;:':
				if len( sent ) > 0:
					sents.append( sent )
					sent = []
				continue
			sent.append( tok.lower() )
		if len( sent ) > 0:
			sents.append( sent )
			sent = []
	return sents

def getMyText():
	sents = []
	db = init('review')
	for row in db.query(Review).filter(Review.placeid==0):
		print row.review
		sents.extend( sentify( row.review ) )
	return sents
	
# TO USE THE DoI...
#	with open('data/raw.txt') as f:
#		sents = []
#		for line in f:
#			sents.extend( sentify( line ) )
#		return sents

import nltk
from nltk.tag.simplify import simplify_wsj_tag
def tag( tokens ):
	tagged_sent = nltk.pos_tag(tokens)
	simplified = [simplify_wsj_tag(tag) for word, tag in tagged_sent]
	return simplified

def valid_tags():
	lines = []
	with open('data/haiku_lines.txt') as f:
		for line in f:
			tokens = [word for sent in sent_tokenize(line.strip()) for word in word_tokenize(sent)]
			lines.append( tag(tokens) )
		return lines
