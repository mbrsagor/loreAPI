import tweepy
from src.credential import ACCESS_TOKEN, SECRET_ACCESS_TOKEN, API_key, API_SECRET_KEY

auth = tweepy.OAuthHandler(API_key, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")
