#!/usr/bin/python3
import tweepy
import csv
from os.path import join, dirname
import os
from dotenv import load_dotenv, find_dotenv

env_path = join(dirname(__file__), ".env")
load_dotenv(find_dotenv())
api_key = os.environ.get('API_KEY')
api_key_secret = os.environ.get('API_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')


def get_all_tweets(screen_name):
    # Because of the limit, this function only allows for 3240 tweets to be collected

    # Authorize twitter and initialize tweepy
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Create empty list to hold all tweets
    alltweets = []

    # maake  request for  recent tweets (200 is the maximum allowed for count, extended allows for full 280 chars)
    new_tweets = api.user_timeline(screen_name = screen_name, count=200, tweet_mode="extended")

    # save tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, tweet_mode="extended")

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text, tweet.favorite_count, tweet.retweet_count] for tweet in alltweets]

    #write the csv
    with open(f'new_{screen_name}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text", "favorites", "retweets"])
        writer.writerows(outtweets)

    pass
