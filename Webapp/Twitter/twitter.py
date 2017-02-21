from twython import Twython
import json
import sys
import urllib, cStringIO

class Twitter:

	def __init__(self):
    		APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = self.get_app_keys()
    		self.twy = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


	def get_app_keys(self):
	#Get app and oauth keys from json file
    		with open('Twitter_Keys.keys') as data_file:
			keys = json.load(data_file)
    		return keys['APP_KEY'], keys['APP_SECRET'], keys['OAUTH_TOKEN'], keys['OAUTH_TOKEN_SECRET']


	def splitter(self, text):
		#chunk_size = 136
		#chunks = [ text[i:i+chunk_size] for i in range(0, len(text), chunk_size) ]

  		chunks = ['']
  		words = text.split()
  
  		for w in words:
			current_chunk = len(chunks) - 1
    			if len(chunks[current_chunk] + w) < 136:
      				chunks[current_chunk] += ' ' + w
    			else:
      				chunks.append('')

		chunks = [ str(chunks.index(x) + 1) + '/' + str(len(chunks)) + ' ' + x for x in chunks ]
		return chunks

	def post(self, text, image=''):
	#Post whatever text and image
		
		if len(text) > 140:
			tweets = self.splitter(text)
			for text in tweets:
				self.twy.update_status(status=text)
		else:
			self.twy.update_status(status=text)
			
		#if image != '':
		#	file = cStringIO.StringIO(urllib.urlopen(image).read())
		#	img = open(file, 'rb')
		#	response = self.twy.upload_media(media=img)
		#	self.twy.update_status(status=text, media_ids=[response['media_id']])
		#else:	
		#	self.twy.update_status(status=text)


#Post text from twitter using arguments from command line input
if len(sys.argv) > 1:
    t = twitter()
    t.post( " ".join(sys.argv[1:]) )
