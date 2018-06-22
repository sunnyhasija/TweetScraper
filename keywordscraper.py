#!/usr/bin/env python
# encoding: utf-8
#Please use the following citation if using the Code

#*************************************************
#*    Title: KeywordScraper.py
#*    Author: Abhinav Hasija
#*    Date: 2018
#*    Code version: 1.0
#*    Availability: www.github.com/sunnyhasija/tweetscraper
#*************************************************/

import tweepy #Package that allows you to use the Twitter API
import csv  #Package to read and write CSV
import pandas as pd #Data frame package from Python

#You need to get your Twitter API credentials to interact with twitter from https://developer.twitter.com/

####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


#authorize With Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#lets get some tweets
# Open/Create a file to append data
csvFile = open('filename.csv','a',encoding='utf-8')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["screenname","id","created_at","text"])
outtweets=[]

#get the tweets for the particular keyword from the search API - we are setting the optional limit to 100 tweets at a time
for tweet in tweepy.Cursor(api.search,q="keyword/hashtag",count=100,lang="en",
                           since="2018-06-11").items():
    #display the tweets
    print (tweet.user.screen_name,tweet.id, tweet.created_at, tweet.text)
    #convert the tweets into a 2D array
    outtweets=[tweet.user.screen_name,tweet.id, tweet.created_at, tweet.text]
    #write them to the CSV
    csvWriter.writerow(outtweets)

#close the file
csvFile.close()
