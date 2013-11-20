import db

import places
import reviewers

i = 0 # TODO: Find a better way to do unique ids...
	# No way this is complex.
def add( review, place_name, rating, reviewer ):
	global i
	#print "Adding a", rating, "star review of", place_name, "by", reviewer, "!"
	review_db = db.init('review')
	r = db.Review()
	r.placeid = places.get_id( place_name )
	r.reviewerid = reviewers.get_id( reviewer )
	r.id = i
	i += 1
	r.review = review
	review_db.add(r)
	review_db.commit()

def get_by_place( place ):
	pass # TODO

def get_by_reviewer( reviewer ):
	pass # TODO
