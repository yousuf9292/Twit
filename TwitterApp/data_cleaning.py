import re


def remove_rt(tweet):
    # Remove the "RT" and following "@handle" if it's a retweet
    if tweet.startswith("RT")== True:
        tweet_split = tweet.split(" ")[2:]
        clean_tweet = ' '.join(word for word in tweet_split)
        return clean_tweet
    else:
        return tweet


def remove_n_char(tweet):
    # Replace new line escapes with white space
    full_tweet = tweet.replace('\n', " ")
    full_tweet = ' '.join(full_tweet.split())
    return full_tweet


def remove_url(tweet):
    # Remove  any url inside the tweet text
    new_tweet = re.sub(r'\(?http\S+', '', tweet)
    return new_tweet


def remove_blank_tweet(df):
    # Remove tweets that are empty
    blank_tweets = []
    for index, tweet in df['text'].iteritems():
        if not tweet:
            blank_tweets.append(index)
    df.drop(blank_tweets, inplace=True)
