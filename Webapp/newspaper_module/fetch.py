import newspaper
import nltk
import time
file1 = open("Dailymail.txt" , 'w')
file2 = open("bbc.txt", 'w')


def download_article(news_paper):
	list_article_summary=[]
	for single_article in news_paper.articles:
		single_article.download()
		single_article.parse()
		single_article.nlp()
		list_article_summary.append(single_article.summary)
	return list_article_summary


bbc = newspaper.build('http://www.bbc.com/news')
dailymail=newspaper.build('http://www.dailymail.co.uk/ushome/index.html')

news_built = {'dailymail' : dailymail , 'bbc' : bbc }

map = {'bbc' : file1 , 'dailymail' : file2}


for i in range(2):
	for single_news_built in news_built:
		summary=download_article(news_built[single_news_built])
		map[single_news_built].write(str(summary))
	time.sleep(60)



file1.close()
file2.close()


	
