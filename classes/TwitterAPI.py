import tweepy
from classes.EnvRead import EnvRead


class TwitterAPI:

    def __init__(self):
        self._auth = tweepy.OAuthHandler(str(EnvRead('TWITTER_CON_KEY')), str(EnvRead('TWITTER_CON_SECRET')))
        self._auth.set_access_token(str(EnvRead('TWITTER_ACC_TOKEN')), str(EnvRead('TWITTER_ACC_T_SECRET')))
        self._api = tweepy.API(self._auth)  # build the
        self._watch_tweet_ids = ()  # tweets to watch
        self._watch_tags = ()   # hashtags to watch
        self._error = False     # errors returns

    def return_timeline(self):  # return the timeline
        try:
            return self._api.home_timeline(tweet_mode="extended")
        except tweepy.TweepError as e:
            self._error = e

    def return_statuses(self):  # return the user tweets
        try:
            return self._api.user_timeline()
        except tweepy.TweepError as e:
            self._error = e

    def tweet(self, content, watch=False):  # tweet from user profile
        self._api.update_status(content)
        if watch:
            self._watch_tweet_ids = self.return_statuses()[0].id

        #  return self._api.get_status()

    def get_tweet(self, tweet_id):  # get tweet by id
        return self._api.get_status(tweet_id)

    def add_watch_tag(self, tag_id):  # add watching tags
        pass

    def add_watch_tweet(self, tweet_id):  # add watching on tweet
        pass

    def _do_watching(self):  # check the tweets and tags
        pass

    def retweet(self, tweet_id):  # retweet a tweet by id
        pass

    def like_tweet(self, tweet_id):  # like a tweet by id
        pass

    def return_error(self):  # return the error, will return false if no errors
        return self._error


public_tweets = TwitterAPI()
print(public_tweets.get_tweet('1164489774926827521'))
print(type(public_tweets.return_statuses()[0].id))
exit()
for tweet in public_tweets.return_statuses():
    print(tweet)
    print('----------')
'''
for status in tweepy.Cursor(public_tweets.return_timeline()).items(50):
    print(status)
'''