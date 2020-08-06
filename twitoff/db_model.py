'''SQLAlchemy models for Twitoff'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.Integer, nullable=False)
    #tweet = db.relationship('Tweet', uselist=False, back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'))
    text = db.Column(db.Unicode(300))
    #user = db.relationship('User', back_populates='tweet')
    
    def __repr__(self):
        return '<Tweet %r>' % self.text

