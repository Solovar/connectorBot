import twitter
api = twitter.Api(consumer_key=[''],   # consumer key
                  consumer_secret=[''],            # consumer secret
                  access_token_key=[''],              # access token
                  access_token_secret=[''])    # access token secret

users = api.GetFriends()
print([u.name for u in users])


'''
https://python-twitter.readthedocs.io/en/latest/index.html
'''
