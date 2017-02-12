from twython import Twython
import json
import sys


#Get app and oauth keys from json file
def get_app_keys():
    with open('Twitter_Keys.keys') as data_file:
	keys = json.load(data_file)
    return keys['APP_KEY'], keys['APP_SECRET'], keys['OAUTH_TOKEN'], keys['OAUTH_TOKEN_SECRET']


#Post whatever text is passed
def post(text):
    APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = get_app_keys()

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    twitter.update_status(status = text)


if len(sys.argv) > 1:
    post( " ".join(sys.argv[1:]) )
