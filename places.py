import db

def get_id( place_name ):
	# TODO: Find the id, or make a new place...
	return 0

i = 0 # TODO: Find a better way to do unique ids...
	# No way this is complex.

def add( place_name ):
	global i
	place_db = db.init('place')
	p = Place()
	p.id = i
	p.name = place_name
	i += 1
	place_db.add(p)
	place_db.commit()

