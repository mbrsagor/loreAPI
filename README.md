# Twitter Bot
The project is mainly I'm making a Twitter bot that gets all info from the Twitter Developer API.

#### Run the applicaiton in your local development environment.

###### Instruction:
- At lest install python3 in your development environment.
- Install python virtual environment.

```bash
git clone https://github.com/mbrsagor/twitterBot.git
cd twitterBot
virtualenv venv --python=python3.8
source venv/bin-activate
pip install -r requirements.txt 
```

### Bot demo example:
```python
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")
```
