from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy
from datetime import datetime, timedelta
from sqlalchemy import func

engine = create_engine('sqlite:///animalshelters.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def getPuppiesOrderByName():
    return session.query(Puppy).order_by(Puppy.name).all()


def getPuppiesYoungerThanSixMonths():
    date_min = datetime.today() - timedelta(days=180)
    return session.query(Puppy).filter(
        Puppy.date_of_birth >= date_min).order_by(Puppy.date_of_birth.desc()).\
        all()


def getPuppiesOrderByWeight():
    return session.query(Puppy).order_by(Puppy.weight.asc()).all()


def getPuppiesInShelters():
    return session.query(func.count(Puppy.name),
                         Shelter.name).filter(Puppy.shelter_id == Shelter.id)\
        .group_by(Puppy.shelter_id).all()
