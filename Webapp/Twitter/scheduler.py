from apscheduler.schedulers.blocking import BlockingScheduler
from twitter import Twitter

import logging
logging.basicConfig()

import newspaper
import nltk

i = 0
twitter = Twitter()

def save_news():
	dailymail=newspaper.build('http://www.dailymail.co.uk/')
	try:
		article=dailymail.articles[0]
		article.download()
		article.parse()
		article.nlp()
	except:
		return 'No Articles', '', ''

        #result =  article.title
	#result += article.top_image
	#result += article.summary
	
	return article.summary, article.top_image, article.url
	#return article.summary[:137] + '...', article.top_image        

def some_job():
	summary, top_image, url = save_news()
	#twitter.post(summary, image = top_image)
	
	#remove line breaks
	summary = summary.replace('\n', ' ').replace('\r', '')	

	if summary != 'No Articles':
		twitter.post(summary + '\r' + url)
	print '\n' +  summary + ' ' + top_image + '\n'

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes = 1)
scheduler.start()
