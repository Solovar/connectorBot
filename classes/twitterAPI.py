import tweepy

from classes.EnvRead import EnvRead

con_key = str(EnvRead('TWITTER_CON_KEY'))
sec_key = str(EnvRead('TWITTER_CON_SECRET'))

acc_t = str(EnvRead('TWITTER_ACC_TOKEN'))
acc_ts = str(EnvRead('TWITTER_ACC_T_SECRET'))


auth = tweepy.OAuthHandler(con_key, sec_key)
auth.set_access_token(acc_t, acc_ts)


api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    print('----------')
