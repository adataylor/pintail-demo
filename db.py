#!/usr/bin/python
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
import os

WordBase = declarative_base()
PlaceBase = declarative_base()
ReviewBase = declarative_base()
ReviewerBase = declarative_base()

class Word(WordBase):
	__tablename__ = "word"
	word = Column(String(128), primary_key=True)
	syllables = Column(Integer)
	frequency = Column(Float)

class Place(PlaceBase):
	__tablename__ = "place"
	id = Column(Integer, primary_key=True) #TODO: We need to delegate this to the table itself.
	name = Column(String(128), nullable=False, default="I need a name!")
	# TODO: Other place based info, such a location, city, etc?

class Review(ReviewBase):
	__tablename__ = "review"
	id = Column(Integer, primary_key=True) #TODO: We need to delegate this to the table itself.
	placeid = Column(Integer)
	reviewerid = Column(Integer)
	review = Column(String(5000), nullable=False, default="")

class Reviewer(ReviewerBase):
	__tablename__ = "reviewer"
	id = Column(Integer, primary_key=True) #TODO: We need to delegate this to the table itself.
	username = Column(String(128), default="<no username provided>")

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

def init( tablename ):
	return dbsetup( tablename, globals()[tablename.title() + "Base"] )

if __name__ == "__main__":

	commands = [ 'init' ]
	tablenames = [ 'word', 'place', 'review', 'reviewer' ]

	def CLIformat(l):
		s = '['
		for x in l:
			s += str(x)
			s += '|'
		return s[:-1]+']'
	
	import sys
	if len(sys.argv) != 3:
		print "Usage: %s %s %s" % (sys.argv[0], CLIformat(commands), CLIformat(tablenames))
		exit(1)
	
	command = sys.argv[1].strip()
	tablename = sys.argv[2].strip()
	
	if command in commands:
		if tablename in tablenames:
			globals()[command](tablename)
		else:
			raise Exception("Unknown table: %s" % tablename)
	else:
		raise Exception("Unknown command: %s" % command)
