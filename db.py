#!/usr/bin/python
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
import os

WordBase = declarative_base()
PlaceBase = declarative_base()
ReviewBase = declarative_base()

class Word(WordBase):
	__tablename__ = "word"
	word = Column(String(128), primary_key=True)
	syllables = Column(Integer)
	frequency = Column(Float)

class Place(PlaceBase):
	__tablename__ = "place"
	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False, default="I need a name!")
	# TODO: Other place based info, such a location, city, etc?

class Review(ReviewBase):
	__tablename__ = "review"
	id = Column(Integer, primary_key=True)
	placeid = Column(Integer)
	review = Column(String(5000), nullable=False, default="")

def dbsetup(name, base):
	thisdir = os.path.dirname(os.path.abspath(__file__))
	dbdir   = os.path.join(thisdir, "db", name)
	if not os.path.exists(dbdir):
		os.makedirs(dbdir)

	dbfile  = os.path.join(dbdir, "%s.db" % name)
	engine  = create_engine('sqlite:///%s' % dbfile)
	base.metadata.create_all(engine)
	session = sessionmaker(bind=engine)
	return session()

#TODO This seems redundant. Use locals[] with a rewrite for the class name?
def init_word():
	return dbsetup("word", WordBase)

def init_place():
	return dbsetup("place", PlaceBase)

def init_review():
	return dbsetup("review", ReviewBase)

if __name__ == "__main__":

	commands = [ 'init' ]
	tablenames = [ 'word', 'place', 'review' ]

	def CLIformat(l):
		s = '['
		for x in l:
			s += str(x)
			s += '|'
		return s[:-1]+']'
	
	import sys
	if len(sys.argv) < 2:
		print "Usage: %s %s %s" % (sys.argv[0], CLIformat(commands), CLIformat(tablenames))
		exit(1)
	
	command = sys.argv[1].strip()
	tablename = sys.argv[2].strip()
	
	if command in commands:
		if tablename in tablenames:
			globals()["%s_%s" % (command, tablename)]()
		else:
			raise Exception("Unknown table: %s" % tablename)
	else:
		raise Exception("Unknown command: %s" % command)
