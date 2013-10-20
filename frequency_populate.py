#!/usr/bin/python
from db import init_word, Word

# Used to generate freqs.csv (clumsy, but functional).
# cat original_wordfreq.txt | awk -F',' '{print $2","$4}' | grep ".*,..*" | awk -F',' '{print $1","$2/3.29795e+08}' > ../populate/freqs.csv

with open('data/freqs.csv') as inputfile:
	db = init_word()
	for line in inputfile:
		word, frequency = line.strip().split(',')
		word = word.lower()
		frequency = float( frequency )
		w = db.query(Word).get(word)
		if not w:
			w = Word()
			w.word = word
			db.add(w)
		if not w.frequency:
			print "Adding frequency for", word
			w.frequency = frequency
	db.commit()

