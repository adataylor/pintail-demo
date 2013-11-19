#!/usr/bin/python
import glob
import os
from lxml import etree

import reviews

def parse_review( review ):
	doc = etree.parse( review )
	return {
		'location': doc.find('location').text,
		'service': doc.find('service').text,
		'url': doc.find('url').text,
		'rating': float( doc.find('rating').text ),
		'text': doc.find('text').text,
		}

os.chdir("data/reviews")
for review in glob.glob("*.rvw"):
	raw = parse_review( review )
	reviews.add( raw['text'], raw['location'], raw['rating'], "UNKNOWN" )
os.chdir("../..")

import trip_advisor_scraper
import yelp_importer
