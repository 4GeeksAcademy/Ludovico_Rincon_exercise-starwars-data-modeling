import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(50))
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship(Planets)

class Favorite_planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

class Favorite_characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
