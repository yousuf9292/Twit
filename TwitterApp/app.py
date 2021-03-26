import streamlit as st
from tweets import get_all_tweets
from data_cleaning import *
from data_download import csv_downloader
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()

progress = st.progress(0)


with header:
    st.title("🔵 Twitter Sentiment Retrieval 📲")
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
            st.error("Invalid handle or tweets unavailable. Please try another handle.")


with dataset:
    st.subheader("About this application")
    st.markdown("This is a simple web application that grabs approximately 3,000\
     recent tweets of any Twitter user and runs them through a sentiment intensity analyser.")

    st.subheader("How it's done")
    st.markdown("Using the Twitter API, the application is able to retrieve any\
      publicly available twitter account and it's respective tweets. Once the\
      tweets are loaded into a dataframe they are passed through a sublibary\
       within Natural Language Toolkit (NLTK), a suite of libraries within \
       natural language processing. The current model only works for Tweets \
       in English and does not process attachements to tweets such as\
       images or hyperlinks. More information about the Twitter API \
       can be found here: https://developer.twitter.com/en/docs. For further\
       reading about NLTK's sentiment intensity analyzer library, read here:\
       https://www.nltk.org/howto/sentiment.html.")

    st.subheader("Who is this for?📈 📉 ")
    st.markdown("Anyone! But those who work with or are interested in data analysis \
      may find this most useful, as well as companies, influencers, or any user \
      curious to see their sentiment score. Is there a correlation \
       between engagement and positivity? Negativity? Maybe time of day plays a \
       role in how a negative tweet is received by followers? There are many \
       questions one could seek to answer with this data.")

    st.subheader("What is sentiment analysis?😡😐😁")
    st.markdown("Put simply, sentiment analysis is the process of a computer \
      identifying or categorizing opinions from a piece of text and \
      determining whether the writer's attitude towards a particular \
      subject is positive, negative or neutral. Here's a definitive guide\
      on the subject: https://monkeylearn.com/sentiment-analysis/")

with features:
    st.subheader("Try it out")
    user_input = st.text_input("Write a sentence and I'll try to guess how you \
      feel (note: computer's are not so good with sarcasm 🙃)")
    if user_input:
        polarity = sid.polarity_scores(user_input)
        if polarity["compound"] >= 0:
            st.balloons()
            st.success("🤖: I'm detecting positivity!!!")
        else:
            st.error("🤖: I'm detecting negativity")

