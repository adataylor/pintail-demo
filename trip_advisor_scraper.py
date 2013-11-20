import urllib2
from BeautifulSoup import BeautifulSoup
import re

import reviews

# TODO: Lots. Figure out the URL struture for Trip Advisor, or at least how to build it. Build in failsafes for when things fail. Figure out how to get a decent list of nearby buisnesses.

def scrape_page( url ):

	page = BeautifulSoup( urllib2.urlopen( url ).read() )

	place_name = page.findAll( lambda tag: tag.name == "h1" )[0].text

	for review in page.findAll(attrs={'class': re.compile(r"review .*")}):
		reviewer = review.findAll( lambda tag: tag.get("class") == "username mo" )[0].text
		rating = float( review.findAll( lambda tag: tag.get("class") == "sprite-ratings" )[0].get("content") )
		# TODO: Deal with the fact that we're not getting full reviews somehow. Avoid More...
		text = review.findAll( lambda tag: tag.get("class") == "entry" )[0].text
		reviews.add( text, place_name, rating, reviewer )

for pend in ['', 'or10-']:
	scrape_page( "http://www.tripadvisor.com/Hotel_Review-g60745-d222955-Reviews-" + pend + "The_Ritz_Carlton_Boston_Common-Boston_Massachusetts.html#REVIEWS" )
