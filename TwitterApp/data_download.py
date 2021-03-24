import tweepy
import csv
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweets import get_all_tweets

# Twiterr handles of selected left-leaning US/UK publishing houses
jacobin_handle = "jacobinmag"
verso_handle = "versobooks"
haymarket_handle = "haymarketbooks"
tribune_handle = "tribunemagazine"

get_all_tweets(jacobin_handle)
jacobin_tweets_df = pd.read_csv("new_jacobinmag_tweets.csv")
