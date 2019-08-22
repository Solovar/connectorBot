import tweepy
from classes.EnvRead import EnvRead


class TwitterAPI:

    def __init__(self):
        self._auth = tweepy.OAuthHandler(str(EnvRead('TWITTER_CON_KEY')), str(EnvRead('TWITTER_CON_SECRET')))
        self._auth.set_access_token(str(EnvRead('TWITTER_ACC_TOKEN')), str(EnvRead('TWITTER_ACC_T_SECRET')))
        self._api = tweepy.API(self._auth)
        self._error = False

    def return_timeline(self):
        try:
            return self._api.home_timeline(tweet_mode="extended")
        except tweepy.TweepError as e:
            self._error = e

    def return_statuses(self):
        try:
            return self._api.user_timeline()
        except tweepy.TweepError as e:
            self._error = e

    def tweet(self, content, watch=False):
        self._api.update_status(content)
        if watch:
            self._watch_tweet('111')

        #  return self._api.get_status()

    def get_tweet(self, tweet_id):
        return self._api.get_status(tweet_id)

    def _watch_tag(self, tag):
        pass

    def _watch_tweet(self, tweet_id):
        pass

    def retweet(self, tweet_id):
        pass

    def like_tweet(self, tweet_id):
        pass

    def return_error(self):
        return self._error


public_tweets = TwitterAPI()
print(public_tweets.get_tweet('1164489774926827521'))
print(public_tweets.return_statuses()[0])
exit()
for tweet in public_tweets.return_statuses():
    print(tweet)
    print('----------')
'''
for status in tweepy.Cursor(public_tweets.return_timeline()).items(50):
    print(status)
'''