import tweepy
from os import environ
from lista import haicais
from random import choice

c_key = environ["c_key"]
c_secret = environ["c_secret"]
a_token = environ["a_token"]
a_token_secret = environ["a_token_secret"]

client = tweepy.Client(
    consumer_key=c_key, consumer_secret=c_secret,
    access_token=a_token, access_token_secret=a_token_secret
)
response = client.create_tweet(text=choice(haicais))
