from flask_sqlalchemy import SQLAlchemy
from . import db

class Sport(db.Model):
    __tablename__ = 'sport'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    games = db.relationship('Game', backref='sport')

    def __repr__(self):
        return '<Sport %r>' % self.name


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    date = db.Column(db.Date, nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'))

    def __repr__(self):
        return '<Game %r>' % self.name


class Guest(db.Model):
    __tablename__ = 'guest'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'))

    def __repr__(self):
        return '<Guest %r>' % self.name
