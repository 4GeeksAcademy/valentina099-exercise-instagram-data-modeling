import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table followers
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    user_from_id = Column(Integer, ForeignKey('user_from_id.id'))
    user_from_id = relationship(user_from_id)
    user_to_id = Column(Integer, ForeignKey('user_to_id.id'))
    user_to_id = relationship(user_to_id)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table post
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    urlimage = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Coments(Base):
    __tablename__ = 'coments'
    # Here we define columns for the table coments
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    coment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table media
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    media_type = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

   






    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
