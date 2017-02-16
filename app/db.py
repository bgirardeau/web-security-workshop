# -*- coding: utf-8 -*-
"""
Database models for application.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from _app import app


db = SQLAlchemy(app)


def escape_string(string):
    """Escapes quotes in string."""
    return string.replace("\"", "\"\"")


class BaseModel(db.Model):
    """
    Base database model, adds id and created/modified timestamps.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(BaseModel):
    """
    Database model for a user.
    """
    __tablename__ = 'users'

    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)

    first_name = db.Column(db.String(128),  nullable=False)
    last_name = db.Column(db.String(128),  nullable=False)

    def __init__(self, username, password, role=0, first_name='', last_name=''):
        self.username = username
        self.password = password
        self.role = role
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %r>' % (self.username)

    # Methods required for login manager

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def check_password(self, password):
        return password == self.password


class Note(BaseModel):
    """
    Database model for a note.
    """
    __tablename__ = 'notes'

    author = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    public = db.Column(db.Integer, nullable=False, default=False)

    def __init__(self, public, author, title, text):
        self.public = public
        self.author = author
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Note %r>' % (self.title)
