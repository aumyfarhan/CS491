#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:02:57 2021

@author: farhan
"""
## Code snippets to load stored JSON format data, filter and store in CSV format.

# import packages
import json
import pandas as pd



filename = 'first_collection.txt'
cur_file = open(filename,'r')

tweet_count = 0 # counter to keep track no of tweets processed
user_count = 0 # counter to keep track no of unique_user processed

unique_user_id_set = set([])      
all_tweet_information = []
all_user_information = []
  
# iterate through the file
try:     
   for line in cur_file:
       # if line length is less than 100, that indicates error.
       if (len(line)>100): 
           tweet_object=json.loads(line) # convert "string-line" into json
           # check if json object has a key id. Otherwise continue to next.
           if 'id' in tweet_object.keys(): 
               tweet_count += 1
               # tweet object information
               tweet_id        = tweet_object['id']
               user_id         = tweet_object['user']['id']
               tweet_lang      = tweet_object['lang']
               tweet_time      = str(pd.to_datetime(tweet_object['created_at']))
               source          = tweet_object['source']
               tweet_text      = tweet_object['text']
               
               # tweet numeric information
               quote_count = tweet_object['quote_count']
               reply_count = tweet_object['reply_count']
               retweet_count = tweet_object['retweet_count']
               tweet_favorite_count = tweet_object['favorite_count']
               
               # meta-content information
               hashtags = [hashtag['text'] for hashtag in tweet_object['entities']['hashtags']]
               short_urls = [url['url'] for url in tweet_object['entities']['urls']]
               try:
                   expanded_urls = [url['expanded_url'] for url in tweet_object['entities']['urls']]
               except:
                   print('Error Message: No Expanded URL.')
                   expanded_urls = []
                   
               # user interaction based informations    
               user_mentions = [user_mentions['id']\
                                for user_mentions in tweet_object['entities']['user_mentions']]
               
               
               tweet_info = [tweet_id, user_id, tweet_lang,\
                            tweet_time, source, tweet_text,\
                            quote_count, reply_count, retweet_count,\
                            tweet_favorite_count, hashtags, short_urls,\
                            expanded_urls, user_mentions]
            
               all_tweet_information.append(tweet_info)
               # user profile information
               
               if user_id in unique_user_id_set:
                   pass
               else:
                   unique_user_id_set.add(user_id)
                   user_count += 1
                   user_screen_name      = tweet_object['user']['screen_name']
                   user_name             = tweet_object['user']['name']
                   user_language         = tweet_object['user']['lang']  
                   location              = tweet_object['user']['location']
                   profile_url           = tweet_object['user']['url']
                   description           = tweet_object['user']['description']
                   protected             = tweet_object['user']['protected']
                   verified              = tweet_object['user']['verified']
                   created_at            = str(pd.to_datetime(tweet_object['user']['created_at']))
                   friends_count         = tweet_object['user']['friends_count']
                   followers_count       = tweet_object['user']['followers_count']
                   favorites_count       = tweet_object['user']['favourites_count']
                   statuses_count        = tweet_object['user']['statuses_count']

                   user_information = [tweet_id, user_id, user_screen_name, user_name,\
                           user_language, location, profile_url,\
                           description, protected, verified, created_at,\
                           friends_count, followers_count,\
                           favorites_count, statuses_count]
                       
                   all_user_information.append(user_information)
                   
              
except Exception as e:
    print(f'Error in reading line. Message: {e}')

print(f"Total Tweet Processed: {tweet_count}")
print(f"Total unique users: {user_count}")

tweet_info_columns = ['tweet_id', 'user_id', 'tweet_lang',\
                      'tweet_time', 'source', 'tweet_text',\
                      'quote_count', 'reply_count', 'retweet_count',\
                      'tweet_favorite_count', 'hashtags', 'short_urls',\
                      'expanded_urls', 'user_mentions']
    
user_info_columns = ['tweet_id', 'user_id', 'user_screen_name', 'user_name',\
                     'user_language', 'location', 'profile_url',\
                     'description', 'protected', 'verified', 'created_at',\
                     'friends_count', 'followers_count',\
                     'favorites_count', 'statuses_count']
    
tweet_info_dataframe = pd.DataFrame(all_tweet_information, columns=tweet_info_columns)
user_info_dataframe = pd.DataFrame(all_user_information, columns=user_info_columns)

tweet_info_dataframe.to_csv('tweet_info_dataframe.csv')
user_info_dataframe.to_csv('user_info_dataframe.csv')