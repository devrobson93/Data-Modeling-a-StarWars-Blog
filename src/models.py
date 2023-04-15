import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User (Base):
    __tablename__ = "user"
    id = Column (Integer, primary_key=True)
    name = Column(String)      

class Favorites (Base):
    __tablename__ = "favorites"
    id = id = Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey("user.id"))
    basic_data_id = Column(Integer, ForeignKey("basic_data.id"))

class Basic_data (Base):
    __tablename__ = "basic_data"
    id = Column (Integer, primary_key=True)
    name = Column(String)
    description = Column (String)

class Character (Base):
    __tablename__ = "character"
    gender = Column(String)
    hair_color = Column(String)
    eye_color = Column(String)
    basic_data_id = Column(Integer, ForeignKey("basic_data.id"),primary_key=True)

class Planet (Base):
    __tablename__ = "planet"
    population = Column(Integer)
    terrain = Column(String)
    climate = Column (String)
    orbital_period = Column(Integer)
    rotation_period = Column (Integer)
    diameter = Column(Integer)
    basic_data_id = Column(Integer, ForeignKey("basic_data.id"),primary_key=True)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
