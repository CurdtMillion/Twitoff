from os import getenv
import basilica
from twitter_scraper import get_tweets, Profile
from dotenv import load_dotenv
from .db_model import db, User, Tweet

load_dotenv()

#TWITTER_AUTH = tweepy.OAuthHandler(getenv('TWITTER_CONSUMER_API_KEY'),
#                                   getenv('TWITTER_CONSUMER_API_SECRET'))
#TWITTER_AUTH.set_access_token(getenv('TWITTER_ACCESS_TOKEN'),
#                              getenv('TWITTER_ACCESS_TOKEN_SECRET'))
#TWITTER = twitter_scraper.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))

def add_user_twitter_scraper(username):
    """Add a user and their tweets to database."""
    try:
        # Get user profile   
        user_profile = list(get_tweets(username, pages=25))
        db.session.add(user_profile)

        # Get most recent tweets
        tweets = list(get_tweets(username, pages=10))
        original_tweets = [d for d in tweets if d['username']==username]

        # Get an example Basilica embedding for first tweet
        embedding = BASILICA.embed_sentence(original_tweets[0]['text'], model='twitter')

        # Add tweet info to Tweet table
        db_tweet = Tweet(id=tweet.id,
                         text=tweet.full_text[:300],
                         embedding=embedding)
        user_profile.tweet.append(db_tweet)
        db.session.add(db_tweet)
            
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e

    else:
        db.session.commit()

    return original_tweets, embedding