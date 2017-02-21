# app/home/views.py

from flask import abort, render_template, request, redirect, jsonify
from flask_login import current_user, login_required
from sys import argv
import newspaper
import nltk

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

@home.route('/news', methods = ['POST','GET'])
@login_required
def news():
    content = " "
    if request.method == 'POST':
    	value = request.form['submit']
    	return jsonify(test(value))
    elif request.method == 'GET':
    	pass
    	
    return render_template('home/news.html', title = "News", content = content)			
    	    
