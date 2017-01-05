import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Date, Numeric  # NOQA


# Creates instance of declarative Base
Base = declarative_base()


class Shelter(Base):
    """docstring for Shelter."""
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)


class Puppy(Base):
    """docstring for Puppy."""
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String(6), nullable=False)
    weight = Column(Numeric(10))
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)


# Creates the database and adds tables and columns
engine = create_engine('sqlite:///animalshelters.db')
Base.metadata.create_all(engine)
