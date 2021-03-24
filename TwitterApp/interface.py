import streamlit as st
from tweets import get_all_tweets
from data_cleaning import *
from data_download import csv_downloader
import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model = st.beta_container()


with header:
    st.title("Twitter Sentiment Retrieval")
    user_input = st.text_input("Enter a Twitter Handle (Do not include @)")
    if user_input:
        try:
            handle = user_input

            get_all_tweets(handle)
            handle_tweets_df = pd.read_csv(f"new_{handle}_tweets.csv")
            handle_tweets_df["text"] = handle_tweets_df["text"].map(remove_rt)
            handle_tweets_df["text"] = handle_tweets_df["text"].map(remove_n_char)
            handle_tweets_df["text"] = handle_tweets_df["text"].map(remove_url)
            remove_blank_tweet(handle_tweets_df)
            handle_tweets_df['score'] = handle_tweets_df['text'].apply(lambda tweet: sid.polarity_scores(tweet))
            handle_tweets_df['compound'] = handle_tweets_df['score'].apply(lambda d: d['compound'])
            handle_tweets_df['comp_score'] = handle_tweets_df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
            st.write(handle_tweets_df)
            csv_downloader(handle_tweets_df, handle)
        except:
            st.error("Sorry")


with dataset:
    pass


with features:
    pass

with model:
    pass


# st.markdown("""# This is a header
# ## This is a sub header
# This is text""")

# df = pd.DataFrame({
#           'first column': list(range(1, 11)),
#           'second column': np.arange(10, 101, 10)
#         })

# # this slider allows the user to select a number of lines
# # to display in the dataframe
# # the selected value is returned by st.slider
# line_count = st.slider('Select a line count', 1, 10, 3)

# # and used in order to select the displayed lines
# head_df = df.head(line_count)

# head_df
