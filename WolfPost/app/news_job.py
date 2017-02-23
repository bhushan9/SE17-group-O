from apscheduler.schedulers.blocking import BlockingScheduler
import pickle

import logging
logging.basicConfig()

import newspaper
import nltk


def parse_article(article):
	article.download()
	article.parse()
	article.nlp()
	return article.title, article.summary, article.top_image, article.url 


def pickle_news(data):
	#Save data as pickle (special python file that can be loaded into a variable)
	file = open('news.data', 'w')
	pickle.dump(data, file)
	file.close()


def unpickle_news():
	#Unpickle news file
	file = open('news.data', 'r')
	data = pickle.load(file)
	return dat


def download_news():
	news_sources = ['http://www.dailymail.co.uk/',
			'http://www.kotaku.com',
			'http://www.msn.com',
			'http://www.ign.com',
			'http://www.fox.com',
			'http://www.nytimes.com',
			'http://theguardian.com',
			'http://www.bbc.com']

	sites = []
	for source in news_sources:
		print source
		news = newspaper.build(source)
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
			sites.append(site_articles)

	#if sites list has data, save file
	if sites: pickle_news(sites)
	print sites


def news_job():
	scheduler = BlockingScheduler()
	scheduler.add_job(download_news, 'interval', minutes = 5)
	scheduler.start()


if __name__ == '__main__':
	news_job()
