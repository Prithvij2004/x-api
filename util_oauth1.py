import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def create_client(consumer_key, consumer_secret, access_token, access_token_secret):
    client = tweepy.Client(
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret, 
        access_token=access_token, 
        access_token_secret=access_token_secret
        )
    return client

# consumer_key = os.getenv('CONSUMER_KEY')
# consumer_secret = os.getenv('CONSUMER_SECRET')
# access_token = os.getenv('ACCESS_TOKEN')
# access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# print(consumer_key)
# print(consumer_secret)
# print(access_token)
# print(access_token_secret)

# client = create_client(consumer_key, consumer_secret, access_token, access_token_secret)

