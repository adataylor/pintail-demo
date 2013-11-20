from collections import defaultdict
from wordutil import syllables, frequency

from text import * #TODO Lots to be done here? Use actual reviews?

def total_syllables( chunk ):
	try:
		return sum([ syllables( word ) for word in chunk ])
	except:
		return -1 #Some key did not work...

def avg_frequency( chunk ):
	frequencies = [ frequency( word ) for word in chunk ]
	return sum( frequencies ) / len( frequencies )

def chunks( sentances, num_syllables ):
	for sentance in sentances:
		for start_index in range( len( sentance ) ):
			for end_index in range( start_index, len( sentance ) ):
				chunk = sentance[start_index:end_index]
				chunk_syllables = total_syllables( chunk )
				if chunk_syllables > num_syllables or chunk_syllables < 0:
					break
				if chunk_syllables == num_syllables:
					yield chunk

valid = valid_tags()
def print_poem( lines ):
	for line in lines:
		for word in line:
			print word,
		print tag(line)
		print tag(line) in valid

sentances = getMyText()

from itertools import islice, ifilter
from random import choice

#TODO: Weight on avg_frequency?
haiku_lines = lambda n_syl: ifilter( lambda chunk: tag( chunk ) in valid, chunks( sentances, n_syl ) )

print "Making 3-syllable chunks..."
chunks3 = list( islice( haiku_lines( 3 ), 10 ) )
print chunks3
print "Making 4-syllable chunks..."
chunks4 = list( islice( haiku_lines( 4 ), 10 ) )
print chunks4
print "Making 5-syllable chunks..."
chunks5 = list( islice( haiku_lines( 5 ), 10 ) )
print chunks5
#print "Making 7-syllable chunks..."
#chunks7 = list( islice( haiku_lines( 7 ), 10 ) )
#print chunks7

for i in range(50):
	print "---"
	print_poem([ choice(chunks5), choice(chunks3) + [","] + choice(chunks4), choice(chunks5) ])

