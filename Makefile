# I made this for Ubuntu 13.04 Linux. I've tried to keep it cross platform, but I may not have succeeded.
# Let me know. ~woursler
all: clean init-db populate-db

setup:
	chmod +x db.py

init-db:
	# Run db.py init for each table.
	# Using python db.py rather than
	# ./db.py for compatibility.
	python db.py init word
	python db.py init place
	python db.py init review
	python db.py init reviewer

populate-db:
	python frequency_populate.py
	python review_populate.py

# Remove all runtime based information.
# Should return the repo to a "source-only" state.
clean:
	# Remove all database files.
	rm -rf db
