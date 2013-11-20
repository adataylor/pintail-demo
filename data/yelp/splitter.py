# This is a file designed to make it possible to cut down the filesize of the dataset.
import json

f = open('academic_dataset.json','r')

# Delete these files first
businesses_file = open('businesses.json', 'w+')
reviews_file = open('reviews.json', 'w+')
users_file = open('users.json', 'w+')

for line in f:
	obj = json.loads( line )
	# TODO: switch to make use of all data.
	if obj['type'] == 'review':
		reviews_file.write( line )
	if obj['type'] == 'business':
		businesses_file.write( line )
	if obj['type'] == 'user':
		users_file.write( line )

# After this all, you'll want to split up the reviews file further using
# split -l 100000 reviews.json new
	
	
