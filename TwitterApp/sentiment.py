import tweepy
import csv
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweets import get_all_tweets
from data_download import haymarket_tweets_df,verso_tweets_df,tribune_tweets_df, jacobin_tweets_df

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
df_list = [jacobin_tweets_df, verso_tweets_df, tribune_tweets_df, haymarket_tweets_df]


for df in df_list:
    # Create new column with full polarity score
    df['score'] = df['text'].apply(lambda tweet: sid.polarity_scores(tweet))
    df['score'] = df['text'].apply(lambda tweet: sid.polarity_scores(tweet))
    df['score'] = df['text'].apply(lambda tweet: sid.polarity_scores(tweet))
    df['score'] = df['text'].apply(lambda tweet: sid.polarity_scores(tweet))

    # Grab the compound score
    df['compound'] = df['score'].apply(lambda d: d['compound'])
    df['compound'] = df['score'].apply(lambda d: d['compound'])
    df['compound'] = df['score'].apply(lambda d: d['compound'])
    df['compound'] = df['score'].apply(lambda d: d['compound'])

    # Create a column classifying if a tweet is considered positive or negative based on compound score number
    df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
    df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
    df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
    df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
