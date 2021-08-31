#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:16:53 2021

@author: farhan
"""
import tweepy
import yaml
from datetime import datetime

# yaml file reader funtion
def read_yaml(file_path):
	with open(file_path, "r") as f:
		return yaml.safe_load(f)

# yaml config file path
file_path = "twitter_api_key_config.yaml"
# read from config file
api_credential = read_yaml(file_path)



# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, listen_time=60, output_file=None):
        super(MyStreamListener, self).__init__()
        self.counter = 0
        print("Initialized Tweepy StreamListener.")
        self.start_time = datetime.now()
        self.current_time = datetime.now()
        self.listen_time = listen_time
        self.output_file = output_file
        
    def on_data(self, data):
        self.current_time = datetime.now()
        time_elapsed = (self.current_time - self.start_time).total_seconds()
        if time_elapsed < self.listen_time:
            try:
                self.counter += 1
                print(f'Data no: {self.counter}. Data: {data}\n\n\n\n')
                self.output_file.write(str(data))
            except Exception as e:
                print(f"On data Exception:{e}.")
        else:
            print(f"Stream listen time period ended. Total listen time: {self.listen_time} seconds.")
            return False
    s
    """
    def on_status(self, status):
        self.counter += 1
        print(f'Tweet No: {self.counter}. status.text: {status.text}\n'\
              f'status: {status}\n\n\n')
    """
    """
    def on_data(self, data):
        self.counter += 1
        print(f'Data no: {self.counter}. Data: {data}\n\n\n\n')
    """
    # handling Errors
    def on_error(self, status_code):
        print(f"status_code: {status_code}")
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
    
    
# API authentication
auth = tweepy.OAuthHandler(api_credential["api_key"], \
                           api_credential["api_secret_token"])
auth.set_access_token(api_credential["access_token"], \
                      api_credential["access_token_secret"])
api = tweepy.API(auth, wait_on_rate_limit=True)
"""
auth = tweepy.AppAuthHandler(api_credential["api_key"], api_credential["api_secret_token"])
api = tweepy.API(auth, wait_on_rate_limit=True)
"""

# name and open a text file to store raw tweets.
output_file_name = "first_colelction.txt"
output_file = open(output_file_name,'w')


# create a stream
myStreamListener = MyStreamListener(listen_time=10, output_file=output_file)
myStream = tweepy.Stream(api.auth, myStreamListener)

# start a stream
keywords = ['COVID-19']
try:
    print("Stream Filter")
    myStream.filter(track=keywords)
    print("DONE")
except Exception as e:
    print(f"error in stream filter {e}")

output_file.close()