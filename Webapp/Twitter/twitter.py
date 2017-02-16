from twython import Twython
import json
import sys


class twitter:

	def __init__(self):
    		APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = self.get_app_keys()
    		self.twy = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


	#Get app and oauth keys from json file
	def get_app_keys(self):
    		with open('Twitter_Keys.keys') as data_file:
			keys = json.load(data_file)
    		return keys['APP_KEY'], keys['APP_SECRET'], keys['OAUTH_TOKEN'], keys['OAUTH_TOKEN_SECRET']


	#Post whatever text is passed
	def post(self, text):
		self.twy.update_status(status = text)


#Post text from twitter using arguments from command line input
if len(sys.argv) > 1:
    t = twitter()
    t.post( " ".join(sys.argv[1:]) )
