import pandas as pd
from tweets import get_all_tweets
from data_cleaning import *


# Twiterr handles of selected left-leaning US/UK publishing houses
jacobin_handle = "jacobinmag"
verso_handle = "versobooks"
haymarket_handle = "haymarketbooks"
tribune_handle = "tribunemagazine"

get_all_tweets(jacobin_handle)
jacobin_tweets_df = pd.read_csv("new_jacobinmag_tweets.csv")

get_all_tweets(verso_handle)
verso_tweets_df = pd.read_csv("new_versobooks_tweets.csv")

get_all_tweets(tribune_handle)
tribune_tweets_df = pd.read_csv("new_tribunemagazine_tweets.csv")

get_all_tweets(haymarket_handle)
haymarket_tweets_df = pd.read_csv("new_haymarketbooks_tweets.csv")


df_list = [jacobin_tweets_df, verso_tweets_df, tribune_tweets_df, haymarket_tweets_df]

for df in df_list:
    df["text"] = df["text"].map(remove_rt)
    df["text"] = df["text"].map(remove_n_char)
    df["text"] = df["text"].map(remove_url)
    remove_blank_tweet(df)
