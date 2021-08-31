# example code to get started with Twitter RESTful API

# import packages
import tweepy
import yaml

# yaml file reader funtion
def read_yaml(file_path):
	with open(file_path, "r") as f:
		return yaml.safe_load(f)

# yaml config file path
file_path = "twitter_api_key_config.yaml"
# read from config file
api_credential = read_yaml(file_path)

print(f'api_key: {api_credential["api_key"]}\n'
      f'api_secret_token: {api_credential["api_secret_token"]}\n'
      f'access_token: {api_credential["access_token"]}\n'
      f'access_token_secret: {api_credential["access_token_secret"]}')


## Twitter Authentication Type-1 (OAuth) 
auth = tweepy.OAuthHandler(api_credential["api_key"], api_credential["api_secret_token"])
auth.set_access_token(api_credential["access_token"], api_credential["access_token_secret"])
API = tweepy.API(auth, wait_on_rate_limit=True)


## Authentication Type-2 (AppAuth) 
"""
auth = tweepy.AppAuthHandler(api_credential["api_key"], api_credential["api_secret_token"])
api = tweepy.API(auth, wait_on_rate_limit=True)
"""


## collect user information using a single screen_id
# API.get_user(id/user_id/screen_name)
# parameters, either, "user_id" or "screen_name"
cristiano_screen_name = "cristiano"
cristiano_user_id = 155659213
single_user_object_via_user_id = API.get_user(user_id=cristiano_user_id)
single_user_object_via_screen_name = API.get_user(screen_name=cristiano_screen_name)



## collect user information using a list of user_ids/screen_name (max=100 in single request)
user_ids = [1104149473721311232, 155659213]
# screen_names = ['', '']
user_objects_via_user_id = API.lookup_users(user_ids=user_ids)
# user_objects_via_screen_name = api.lookup_users(screen_name=screen_names)
print(f"user_objects_via_user_id.screen_name: {user_objects_via_user_id[0].screen_name}")
print(f"user_objects_via_user_id.followers_count: {user_objects_via_user_id[0].followers_count}")

## collect followers_ids
# API.friends_ids(id/screen_name/user_id[, cursor])


## collect friends_ids
# API.followers_ids(id/screen_name/user_id)
user_id = 155659213
followers = API.followers_ids(user_id=user_id)

## collect follower information of a single user
# API.followers([id/screen_name/user_id][, cursor])
# returns list of user objects
user_id = 155659213
followers = API.followers(user_id=user_id)
print(followers)
## collect friend information of a single user
# API.friends([id/user_id/screen_name]
# returns list of user objects
user_id = 155659213
friends = API.friends(user_id=user_id)

## Collect the 3200 recent tweets of a single user 
tweet_list = []
for status in tweepy.Cursor(API.user_timeline(id=user_id)).items():
    # process status here
    tweet_list.append(status)

## Search Tweets
# API.search(q[, geocode][,\
#    lang][, locale][, result_type][, count][, until][, since_id][, max_id][, include_entities])

# q – the search query string of 500 characters maximum, including operators. 
# Queries may additionally be limited by complexity.

