import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Twitter API credentials
consumer_key = "XJUn8p0PaayP1UsYrVVsS724n"
consumer_secret = "QghfJDxBsK19N1Ay3pKcb3zHXarwW8Xrx4DWFdQazk7N3mD6Yg"
access_key = "751960751070322689-YoEXRcl7ctXSrSY9x2iqQI3RpO2P28q"
access_secret = "RyYJh2YAQ59fyYXd4cIGfEWzbsDK3FHhKh0SXmD40kZpU"

class listener(StreamListener):
        def on_data(self, data):
                print data
                return True

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(follow=['751960751070322689'])