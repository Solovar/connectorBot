import twitter
from classes.EnvRead import EnvRead
api = twitter.Api(consumer_key=[EnvRead('TWITTER_CON_KEY')],   # consumer key
                  consumer_secret=[EnvRead('TWITTER_CON_SECRET')],            # consumer secret
                  access_token_key=[EnvRead('TWITTER_ACC_TOKEN')],              # access token
                  access_token_secret=[EnvRead('TWITTER_ACC_T_SECRET')])    # access token secret

users = api.GetFriends()
