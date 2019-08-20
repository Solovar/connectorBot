import tweepy

from classes.EnvRead import EnvRead

auth = tweepy.OAuthHandler(str(EnvRead('TWITTER_CON_KEY')), str(EnvRead('TWITTER_CON_SECRET')))
auth.set_access_token(str(EnvRead('TWITTER_ACC_TOKEN')), str(EnvRead('TWITTER_ACC_T_SECRET'))

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
