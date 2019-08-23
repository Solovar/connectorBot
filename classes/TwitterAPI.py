import tweepy
from classes.EnvRead import EnvRead


class TwitterAPI(tweepy.StreamListener):

    def __init__(self):
        super().__init__()
        self._auth = tweepy.OAuthHandler(str(EnvRead('TWITTER_CON_KEY')), str(EnvRead('TWITTER_CON_SECRET')))
        self._auth.set_access_token(str(EnvRead('TWITTER_ACC_TOKEN')), str(EnvRead('TWITTER_ACC_T_SECRET')))
        self._api = tweepy.API(self._auth)  # build the API
        self._stream = tweepy.Stream(auth=self._auth, listener=self)
        self._watch_tweet_ids = ()  # tweets to watch
        self._watch_tags = ()   # hashtags to watch
        self._last_watch = ''   # time stamp of when watching happend
        self._error = False     # errors returns

    # normal Twitter API classes
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
        try:
            self._api.update_status(content)
            if watch:
                self.add_watch_tweet(self.return_statuses()[0].id)
        except tweepy.TweepError as e:
            self._error = e

    def get_tweet(self, tweet_id):  # get tweet by id
        try:
            return self._api.get_status(tweet_id)
        except tweepy.TweepError as e:
            self._error = e

    def retweet(self, tweet_id):  # retweet a tweet by id
        try:
            self._api.retweet(tweet_id)
        except tweepy.TweepError as e:
            self._error = e

    def like_tweet(self, tweet_id):  # like a tweet by id
        pass  # somehow I am having issues to get this to work
    '''
        INFORMATION STREAMING RELATED BELOW HERE #################################
    '''
    def add_watch_tag(self, tag_id):  # add watching tags
        self._watch_tags.append(tag_id)

    def add_watch_tweet(self, tweet_id):  # add watching on tweet
        self._watch_tweet_ids.append(tweet_id)

    def watching(self, target=''):  # check the tweets and tags
        return self._stream.filter(track=[target], is_async=True)

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

    # all errors are stored here
    def return_error(self):  # return the error, will return false if no errors
        return self._error


public_tweets = TwitterAPI()
# print(public_tweets.get_tweet('1164489774926827521'))
print(public_tweets.watching('#python'))
# print(type(public_tweets.return_statuses()[0].id))
exit()
for tweet in public_tweets.return_statuses():
    print(tweet)
    print('----------')
'''
for status in tweepy.Cursor(public_tweets.return_timeline()).items(50):
    print(status)
'''