#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:00:17 2020

@author: luofan
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from urllib3.exceptions import ProtocolError
from requests.exceptions import ChunkedEncodingError
from http.client import IncompleteRead

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            print (data)
            savefile = open("elections.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException.e:
            print ("Failed on Data", str(e))
            time.sleep(5)
    

    def on_error(self, status):
        print (status)


    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(languages = ['en'], track=["US Presidential Election 2020","Biden","Trump","Democrats","Republicans" ])
