from collections import defaultdict
from wordutil import syllables, frequency

from text import getMyText #TODO Lots to be done here?

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

def print_poem( lines ):
	for line in lines:
		for word in line:
			print word,
		print ''

sentances = getMyText()

from itertools import islice
from random import choice

#TODO: Weight on avg_frequency?
#TODO: Limit to valid tagsets?

print "Making 5-syllable chunks..."
chunks5 = list( islice( chunks( sentances, 5 ), 100 ) )
print "Making 7-syllable chunks..."
chunks7 = list( islice( chunks( sentances, 7 ), 100 ) )

for i in range(50):
	print "---"
	print_poem([ choice(chunks5), choice(chunks7), choice(chunks5) ])





