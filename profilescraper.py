#!/usr/bin/env python
# encoding: utf-8
#Please use the following citation if using the Code

#*************************************************
#*    Title: ProfileScraper.py
#*    Author: Abhinav Hasija
#*    Date: 2018
#*    Code version: 1.0
#*    Availability: www.github.com/sunnyhasija/tweetscraper
#*************************************************/
import tweepy #https://github.com/tweepy/tweepy
import csv #to write tweets to CSV file

#Twitter API credentials
#you can get this from developer.twitter.com and registering your application

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv
    #encode the text in utf-8 for ease of processing. You can also do latin-1

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.retweet_count] for tweet in alltweets]

    #write the csv
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text", "retweet_count"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    #pass in the username(s) of the account you want to download
    foo = ['username1','ohiostate'] #pass any number that you want separated by a comma
    for handle in foo:
        get_all_tweets( handle)
        print(" All tweets for %s downloaded" % handle)
