import newspaper
from newspaper import news_pool

news_sources = {'Dailymail' 	: 'http://www.dailymail.co.uk/ushome/index.html',
			'BBC'		: 'http://www.bbc.com/news',
			'The Economist'	: 'http://www.economist.com',
			'CNN' 		: 'http://www.cnn.com',
			'New York Times': 'https://www.nytimes.com',
			'The Atlantic'	: 'https://www.theatlantic.com',
			'The Guardian'	: 'https://www.theguardian.com/us'}



print("yoyo")

news_build=[]

for source_key in news_sources:
	news=newspaper.build(news_sources[source_key])
	news_build.append(news)

news_pool.set(news_build, threads_per_source = 2)
news_pool.join()


print(news_build[0].articles[0].html)

