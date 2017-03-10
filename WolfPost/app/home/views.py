# app/home/views.py

from flask import abort, render_template, request, redirect, jsonify
from flask_login import current_user, login_required
from sys import argv
import newspaper
import nltk
import pickle
import re

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
    	abort(403)
    return render_template('home/admin_dashboard.html', title = "Dashboard")


def test(value):
    news_link_dict={'Dailymail' : 'http://www.dailymail.co.uk/ushome/index.html', \
	'BBC':'http://www.bbc.com/news', \
	'The Economist':'http://www.economist.com/' ,\
	'CNN' : 'http://www.cnn.com/', \
	'New York Times' : 'https://www.nytimes.com/', \
	'The Atlantic' : 'https://www.theatlantic.com/',\
	'The Guardian' : 'https://www.theguardian.com/us' }
    news_paper=newspaper.build(news_link_dict[value])
    if news_paper.articles[0]:
    	article=news_paper.articles[0]
    else:
    	article = "No article found"	
    article.download()
    article.parse()
    article.nlp()
    return article.summary


def unpickle_news():
	#Unpickle news file
	file = open('news/news.data', 'r')
	data = pickle.load(file)
	return data


def clean_content(text):
	do_not_remove = '.!?= -+%$'
	return re.sub(r'[^\w'+do_not_remove+']', '', text) 


@home.route('/news', methods = ['POST','GET'])
@login_required
def news():
    content = ''
    content0=content1=content2 = ''
    title0=title1=title2= ''
    url0=url1=url2 = ''
    image0=image1=image2 = ''
    if request.method == 'POST':
    	value = request.form['submit']
	news = unpickle_news()
	try:
    	    content0 = news[value][0]['summary']
            title0 = news[value][0]['title']
            url0 = news[value][0]['url']
            image0 = news[value][0]['image']

            content1 = news[value][1]['summary']
            title1 = news[value][1]['title']
            url1 = news[value][1]['url']
            image1 = news[value][1]['image']

            content2 = news[value][2]['summary']
            title2 = news[value][2]['title']
            url2 = news[value][2]['url']
            image2 = news[value][2]['image']
        except KeyError:
            content = 'Key Error. No value for ' + value 
    elif request.method == 'GET':
	content = 'No News Found For Source'
    	pass
    
    tts_summary0 = clean_content(content0)
    tts_summary1 = clean_content(content1)
    tts_summary2 = clean_content(content2)
    return render_template('home/news.html', title0 = title0 , content0 = content0, tts_summary0 = tts_summary0 ,image0 = image0, url0 = url0,
        title1 = title1 , content1 = content1, tts_summary1 = tts_summary1 ,image1 = image1, url1 = url1,
        title2 = title2 , content2 = content2, tts_summary2 = tts_summary2 ,image2 = image2, url2 = url2

        )    	    
