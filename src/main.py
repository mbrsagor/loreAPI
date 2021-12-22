import tweepy
import time, datetime

from src.credential import ACCESS_TOKEN, SECRET_ACCESS_TOKEN, API_key, API_SECRET_KEY

auth = tweepy.OAuthHandler(API_key, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)

api = tweepy.API(auth)


def twitter_bot(hashtag, delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, rpp=10).items(5):
            try:
                tweet_id = dict(tweet._json)['id']
                tweet_text = dict(tweet._text)['text']

                print("ID: " + str(tweet_id))
                print("text: " + tweet_text)

                api.retweet(tweet_id)

            except tweepy.TwitterServerError as error:
                print(error.response)

        time.sleep(delay)


twitter_bot("#python", 10)
