# app/home/views.py

from flask import abort, render_template, request, redirect, jsonify
from flask_login import current_user, login_required
from sys import argv
import newspaper
import nltk
import pickle
import re
import requests
import json

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
	'The New York Times' : 'https://www.nytimes.com/', \
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
    value = ''
    z = ''
    tts_summary = ''

    news_link_dict={'Dailymail' : 'https://newsapi.org/v1/articles?source=daily-mail&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'BBC':'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'The Economist':'https://newsapi.org/v1/articles?source=the-economist&sortBy=top&apiKey=a97466277811418284e9525947633cbd' ,\
    'CNN' : 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'The New York Times' : 'https://newsapi.org/v1/articles?source=the-new-york-times&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'Bloomberg' : 'https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey=a97466277811418284e9525947633cbd',\
    'The Guardian' : 'https://newsapi.org/v1/articles?source=the-guardian-uk&sortBy=top&apiKey=a97466277811418284e9525947633cbd' }
   
    if request.method == 'POST':
        value = request.form['submit']
        print("KRLGDSGDSJKBGKJDSBGKJDSBGJKDSBGJDS")
        r=requests.get(news_link_dict[value])
        z= r.json()
        tts_summary=[]
        for i in range(len(z["articles"])):
            tts_summary.append(clean_content(z["articles"][i]["description"]))  
    elif request.method == 'GET':
        pass

    return render_template('home/news.html', data = z , tts_summary = tts_summary  )    	    
