#Authors: Elijah Gavett, Cyruz Campos
#APPLIED FROM: http://docs.tweepy.org/en/v3.5.0/index.html

import tweepy
import matplotlib

colors = ["red", "green", "blue", "yellow"]

#Create a class called myStreamListener and find a specific word or phrase from a tweet
class StreamListener(tweepy.StreamListener):

    def __init__(self):
        self.statuses = []

    def on_status(self, status):
        print(status.text)
        statuses.append(status.text)
        
    def on_error(self, status_code):
        return False

#Every Key needed for making a connection to the Twitter API
consumer_key = "37NJ7Vvly1HYSXEPp74NMzQRh"
consumer_secret ="swcGN0Ntl63zMIlhmBi0OdRrzK40AOu33ord3vaJA0sfpr0Jlx"
access_key = "510548566-KR9iEx0IE9KGkgptLmj679wgAlb2uXCFywlVEoj7"
access_secret = "e0fps4X0LiPEsBvfSxq1fGQJl7KxqQ7Ke7I3Ka7nvIECC"

#Calling each key and setting them to their designated slot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

#Authenticate the login information
api = tweepy.API(auth)

listener = StreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=listener)

#Track the word 'python' in every tweet that has been shown in Twitter
myStream.filter(track=['CS313'], async=True)

