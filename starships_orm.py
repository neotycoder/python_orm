# Descriptions: This is an example of how to create a ORM. 
# This database will house 2 tables that will contain entries for
# both Federation and Klingon starships. 
# I though this would be a cool way to show an example of how to 
# create an ORM. 

# This is just the ORM. Another script will be written to write
# content to this database to inialize the databsase.
# Another script will be written to query the database.

# Import the requirements to build the ORM
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Declare the Star Trek Database
STBase = declarative_base()

# This creates the federation starships database.
class fed_starships(STBase):
    __tablename__ = 'fed_starships'

    id = Column(Integer, primary_key=True)
    # Example: USS Enterprise
    hullname = Column(String(250), nullable=False)
    # Example: NCC-1701
    # Example: NX-01
    registry = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)

# This creates the klingon starships database.
class klingon_starships(STBase):
    __tablename__ = 'klingons_starships'

    id = Column(Integer, primary_key=True)
    # Example: USS Enterprise
    hullname = Column(String(250), nullable=False)
    # Example: NCC-1701
    # Example: NX-01
    registry = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)

# Define the database engine that STBase will be using.
engine = create_engine('sqlite:///starships.db')

# Create all the tables for the Star Trek Database
# Write all the content for the new tables to this database.
STBase.metadata.create_all(engine)