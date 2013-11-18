#!/usr/bin/python
from db import *
import glob
import os

from lxml import etree

def parse_rvw( review ):
	doc = etree.parse( review )
	return {
		'location': doc.find('location').text,
		'service': doc.find('service').text,
		'url': doc.find('url').text,
		'rating': float( doc.find('rating').text ),
		'text': doc.find('text').text,
		}

os.chdir("data/reviews")
db = init('review')

i = 0
for review in glob.glob("*.rvw"):
	print "Adding ",review
	raw = parse_rvw( review )
	rev = Review()
	rev.placeid = 0
	rev.id = i
	i += 1
	rev.review = raw['text']
	db.add(rev)
db.commit()
