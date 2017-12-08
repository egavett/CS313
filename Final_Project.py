#Authors: Elijah Gavett, Cyruz Campos
#APPLIED FROM: http://docs.tweepy.org/en/v3.5.0/index.html

import re
import tweepy
from matplotlib import colors as colors

#Create a class called myStreamListener and find a specific word or phrase from a tweet
class MyStreamListener(tweepy.StreamListener):
    color_array = []

    def on_status(self, status):
        regex = r'\w+'
        words = re.findall(regex, status.text)
        for word in words:
            if colors.is_color_like(word):
                print(status.text)
                print("Word: {}".format(word))
                color = colors.to_rgb(word)
                print("Color: {}".format(color))
                self.color_array.append(color)
                break
        
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

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener)

#Track the word 'python' in every tweet that has been shown in Twitter
myStream.filter(track=['thelastjedi'], async=True)
