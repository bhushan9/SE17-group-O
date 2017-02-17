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
	#dailymail=newspaper.build('http://www.kotaku.com/')
	article=dailymail.articles[0]
	article.download()
	article.parse()
	article.nlp()

        #result =  article.title
	#result += article.top_image
	#result += article.summary
	
	return article.summary[:137] + '...', article.top_image
        

def some_job():
	summary, top_image = save_news()
	#twitter.post(summary, image = top_image)
	twitter.post(summary)
	print '\n' +  summary + ' ' + top_image + '\n'

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes = 10)
scheduler.start()
