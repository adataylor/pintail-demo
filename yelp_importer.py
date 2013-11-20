import json

import reviews

def import_json_file( filename ):
	f = open(filename,'r')
	for line in f:
		obj = json.loads(line)
		# TODO: switch to make use of all data.
		if obj['type'] == 'review':
			# TODO: Handle id's correctly.
			reviews.add( obj['text'], obj['business_id'], float( obj['stars'] ), obj['user_id'] )
	f.close()
	
import_json_file('data/yelp/users.json')
import_json_file('data/yelp/businesses.json')
# import_json_file('data/yelp/reviews.1.json')
# import_json_file('data/yelp/reviews.2.json')
# import_json_file('data/yelp/reviews.3.json')
import_json_file('data/yelp/reviews.4.json')
