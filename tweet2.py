#import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import ast

#Variables that contains the user credentials to access Twitter API 
access_token = "3481204895-2fZykd8XR5zlQOCgDFb4bPC9ubmpGN3rO3uWMMI"
access_token_secret = "rZEKSWraeQBG6rgGuHWh6k6Z5k7pY0pyJF9lRwFVnNuF5"
consumer_key = "4XWcJjterrkBLjukW2ml4PoE0"
consumer_secret = "p2mTtL0NWy4f0bygIW28LCOAnAJe3fHyrZ9ZHwWvD8MYvxKlSb"

strsOfPurchase = ['trip', 'bought', 'Bought', 'BOUGHT', 'got', 'purchased']
itemPreludes   = ['new', ' an', ' a', 'bought', 'this', 'to']
itemEndings    = ['where', 'in', 'which', 'today', 'yesterday', 'last', '!', '.', ',', ' ']

def findItem(itemStr):
   #print "findItem"
   itemStr += ' ' #Not able to handle '' in the end properly, so need a space
   for prelude in itemPreludes:
        startPos = itemStr.find(prelude)
        if startPos != -1:
             #print "prelude: "+prelude
             #print "startPos "+str(startPos)
             startPos = itemStr.find(' ',startPos+1) #+1 is imp here
             startPos += 1 #just to go to the character ahead of space
             #print "startPos "+str(startPos)
             for ending in itemEndings:
                 endPos = itemStr.find(ending, startPos+1)
                 if endPos != -1:
                     #if it is space, find the last space
                     endPosX = endPos
                     while ending==' ' and endPosX!=-1:
                          endPosX = itemStr.find(ending, endPos+1)
                          if endPosX != -1:
                              endPos = endPosX
                     #print "ending: "+ending+"endPos: "+str(endPos)
                     item   = itemStr[startPos: endPos]
                     print "item: "+item
                     #items  = item.split(" ")
                     #itemsh = items[0] if len(items)==1 else " ".join(items[:-1])
                     #itemsh = " ".join(items[:-1])    
                     #return str(itemsh) 
                     return item
   return None

def parseItem(data):
   #print "parseItem"
   startPoint = data.find('text')
   startPoint = data.find('"',startPoint)
   textStart  = data.find('"',startPoint+1)
   textEnd    = data.find('"',textStart+1)
   itemStr = data[textStart+1: textEnd]
   #return data[textStart+1: textEnd]
   #Assumption: item name comes after 'new', 'this', 'to' (for trip)
   return findItem(itemStr)

def Find(itemStr):
    for st in strsOfPurchase:
        if st in itemStr:
              return itemStr.find(st)
    return -1

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        if Find(data) != -1:
           item = parseItem(data)
           #print data
           print item
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
    #stream.filter(track=['trip', 'new'])
    stream.filter(follow=['3481204895'])
    #stream.filter(track=['trip'])
    
