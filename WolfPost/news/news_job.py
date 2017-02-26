from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import pickle

import logging
logging.basicConfig()

import newspaper
import nltk


def parse_article(article):
	#Run manditory article code, return title, summary, image and url
	article.download()
	article.parse()
	article.nlp()
	return article.title, article.summary, article.top_image, article.url 


def pickle_news(data):
	#Save data as pickle (special python file that can be loaded into a variable)
	file = open('news/news.data', 'w')
	pickle.dump(data, file)
	file.close()


def unpickle_news():
	#Unpickle news file
	file = open('news/news.data', 'r')
	data = pickle.load(file)
	return data


def download_news():
	news_sources = {'Dailymail' 	: 'http://www.dailymail.co.uk/ushome/index.html',
			'BBC'		: 'http://www.bbc.com/news',
			'The Economist'	: 'http://www.economist.com',
			'CNN' 		: 'http://www.cnn.com',
			'New York Times': 'https://www.nytimes.com',
			'The Atlantic'	: 'https://www.theatlantic.com',
			'The Guardian'	: 'https://www.theguardian.com/us'}
	sites = dict()
	for source_key in news_sources:
		print source_key + '\t\t' + news_sources[source_key]
		news = newspaper.build(news_sources[source_key])
		site_articles = []

		num = 1
		for article in news.articles:
			if num > 3: break
			else: num += 1
			try:
				title, summary, image, url = parse_article(article)
				article_list = dict()
				article_list['title'] = title
				article_list['summary'] = summary
				article_list['url'] = url
				article_list['image'] = image
				site_articles.append(article_list)
			except:
				pass

		#if list is empty, dont add
		if not site_articles:
			pass
		else:
			sites[source_key] = site_articles

	#if sites list has data, save file
	if sites:
		pickle_news(sites);
		print 'News Updated Successfully'


def news_job():
	scheduler = BackgroundScheduler()
	scheduler.add_job(download_news, 'interval', minutes = 10)
	scheduler.start()


if __name__ == '__main__':
	news_job()
