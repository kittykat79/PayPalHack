#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2879939870-Lc0SCPzsQY3zntlN1agPIl0Wn46Qa2wSkRyTQmq"
access_token_secret = "I1bIk5JRIuIUvU7ohTM7D4rwsXa7eqVXImH27jadg3bLV"
consumer_key = "98h9AhNaU5yazVBXX3fUysemh"
consumer_secret = "pZTmcmXcTRzJXvfPy1Q5A3Ak3rGEPwEnxtuxnb52wxjavQ6Phq"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])