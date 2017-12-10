#Authors: Elijah Gavett, Cyruz Campos, Christopher Blair-Garcia
#APPLIED FROM: http://docs.tweepy.org/en/v3.5.0/index.html
#APPLIED FROM: https://pypi.python.org/pypi/colored

import re
import tweepy
import time
import colored
import os
from colored import fg, bg, attr
from matplotlib import colors as colors


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Create a class called myStreamListener and find a specific word or phrase from a tweet
class MyStreamListener(tweepy.StreamListener):
    color_array = []

    def on_status(self, status):
        #words = status.text.split()
        regex = r'\w+'
        words = re.findall(regex, status.text)
        for word in words:
            if colors.is_color_like(word):
                if not RepresentsInt(word) and len(word) > 1:
                    #print(status.text)
                    #print("Word: {}".format(word))
                    color = colors.to_hex(word)
                    #print("Color: {}".format(color))
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
myStream.filter(track=['trump'], async=True)
print("Listening...")

#print ('%s%s Hello World !!! %s' % (fg('white'), bg('yellow'), attr('reset')))

while True:
    time.sleep(5)
    if MyStreamListener.color_array:
        rgb_hex = MyStreamListener.color_array.pop(0)
        color = fg ('#000000') + bg(rgb_hex)
        reset = attr('reset')
        os.system("cls")
        for _ in range(0, 6):
            print (color + '                          ' + reset)

    else:
        os.system("cls")
        print('no color found')