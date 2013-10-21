from nltk.tokenize import word_tokenize, sent_tokenize

def getMyText():
	with open('raw.txt') as f:
		sents = []
		for line in f:
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
