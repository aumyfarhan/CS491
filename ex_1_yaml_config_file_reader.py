# read config file in yaml format

import yaml

def read_yaml(file_path):
	with open(file_path, "r") as f:
		return yaml.safe_load(f)

file_path = "twitter_api_key_config.yaml"
api_credential = read_yaml(file_path)

print(f'api_key: {api_credential["access_token_secret"]}\n'
      f'api_secret_token: {api_credential["api_secret_token"]}\n'
      f'access_token: {api_credential["access_token"]}\n'
      f'access_token_secret: {api_credential["access_token_secret"]}')