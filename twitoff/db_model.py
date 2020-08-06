'''SQLAlchemy models for Twitoff'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    #user = db.relationship('User', backref=db.backref('tweet', lazy=True))
    
    def __repr__(self):
        return '<Tweet %r>' % self.text