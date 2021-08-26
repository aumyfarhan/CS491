import pandas as pd
import numpy as np
import csv

file_name = ""
separator = ","
columns_name = ['']
dataframe = pd.read_csv(file_name, sep=separator, usecols=columns_name)


chunk_size = 10000 
temporary_data_list = []

for chunk in pd.read_csv(file_name, chunksize=chunk_size,\
                        sep=separator, usecols=columns_name):
    temporary_data_list.append(chunk)

data_frame = pd.concat(temporary_data_list, axis=0)
del temporary_data_list, chunk




# dataframe meta information
users_columns = ['user_id', 'user_display_name', 'user_screen_name',\
         'user_reported_location', 'user_pro_des', 'user_pro_url',\
         'followers_count', 'following_count', 'statuses_count',\
         'favorited_count', 'account_lang', 'account_creation_date'] 

tweets_columns = ['tweet_id', 'user_id', 'tweet_lang', 'tweet_text',\
         'tweet_time', 'tweet_client_name', 'sentiment',\
         'is_retweet', 'retweet_user_id', 'retweet_screen_name', 'hashtags']


combined_pat = r'|'.join((r'@[A-Za-z0-9_]+', r'RT\s@\S+', \
                          r'https?://[^ ]+',r'www.[^ ]+'))


analyser=SentimentIntensityAnalyzer()

def get_tweet_sentiment(tweet_text):
    
    filtered_text = re.sub(combined_pat, '', tweet_text)
    vader_score=analyser.polarity_scores(filtered_text)
    
    if (vader_score['compound'] <= -0.05):
        sentiment=-1
    elif (vader_score['compound'] >=0.05):
        sentiment=1
    else:
        sentiment=0
        
    return sentiment
