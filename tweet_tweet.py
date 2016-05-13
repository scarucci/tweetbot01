# import twython library

from twython import Twython

APP_KEY = 'XXXX'
APP_SECRET = 'XXXX'
OAUTH_TOKEN = 'XXXX'
OAUTH_TOKEN_SECRET = 'XXXX'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) # authenticate twitter credentials

# search for tweets based on 'tag' + amount of tweets to display

search = twitter.search(q='simoncarucci', count=5)

tweets_searched = search['statuses']

for tweet in tweets_searched:
    print tweet['id_str'], '\n', tweet['text'], '\n\n\n'

# input -> new post

new_tweet = raw_input()

twitter.update_status(status=new_tweet)



