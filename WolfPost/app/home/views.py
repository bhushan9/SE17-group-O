# app/home/views.py

from flask import abort, render_template, request, redirect
from flask_login import current_user, login_required
import pickle
import re
import requests

from . import home

@home.route('/')
def homepage():
    """
    Redirect to news
    """
    return redirect('/news', code=302)


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


@home.route('/like' ,methods = ['POST','GET'] )
def contact():
    count = 0
    if request.method == 'POST':
        if request.form['Like'] == 'Like':
            print("LIKEEEEEEEEEEEEEEEEEEEEEEE")
            count = count + 1
            return render_template ('home/news.html', like = count)


def unpickle_news():
	#Unpickle news file
	file = open('news/news.data', 'r')
	data = pickle.load(file)
	return data


def clean_content(text):
	do_not_remove = '.!?= -+%$'
	return re.sub(r'[^\w'+do_not_remove+']', '', text)


def get_news(value):
    	news_link_dict={'Dailymail' : 'https://newsapi.org/v1/articles?source=daily-mail&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'BBC':'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'The Economist':'https://newsapi.org/v1/articles?source=the-economist&sortBy=top&apiKey=a97466277811418284e9525947633cbd' ,\
    'CNN' : 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'The New York Times' : 'https://newsapi.org/v1/articles?source=the-new-york-times&sortBy=top&apiKey=a97466277811418284e9525947633cbd', \
    'Bloomberg' : 'https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey=a97466277811418284e9525947633cbd',\
    'The Guardian' : 'https://newsapi.org/v1/articles?source=the-guardian-uk&sortBy=top&apiKey=a97466277811418284e9525947633cbd' }

        r = requests.get(news_link_dict[value])
       	z = r.json()
        tts_summary=[]
        for i in range(len(z["articles"])):
         	tts_summary.append(z["articles"][i]["description"])
	return z, tts_summary


@home.route('/news', methods = ['POST','GET'])
def news():
    value = ''
    z = ''
    tts_summary = ''

    if request.method == 'POST':
        value = request.form['submit']
        z, tts_summary = get_news(value)
    elif request.method == 'GET':
        z, tts_summary = get_news('BBC')

    return render_template('home/news.html', data = z , tts_summary = tts_summary  )


def construct_email():
    import requests
    api_key = 'a97466277811418284e9525947633cbd'
    news_link_dict={'Dailymail' : 'https://newsapi.org/v1/articles?source=daily-mail&sortBy=top&apiKey=' + api_key,
            'BBC':'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=' + api_key,
            'The Economist':'https://newsapi.org/v1/articles?source=the-economist&sortBy=top&apiKey=' + api_key,
           'CNN' : 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=' + api_key,
            'The New York Times' : 'https://newsapi.org/v1/articles?source=the-new-york-times&sortBy=top&apiKey=' + api_key,
            'Bloomberg' : 'https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey=' + api_key,
            'The Guardian' : 'https://newsapi.org/v1/articles?source=the-guardian-uk&sortBy=top&apiKey=' + api_key }

    heading = """<html>
        <head>
           <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
           <title>Nettuts Email Newsletter</title>
           <style type="text/css">
           	a {color:#ff0000;}
        	body, #header h1, #header h2, p {margin: 0; padding: 0;}
        	#main {border: 1px solid #cfcece;}
        	img {display: block;}
        	#top-message p, #bottom-message p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
        	#header h1 {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
        	#header h2 {color: #ffffff !important; font-family: Arial, Helvetica, sans-serif; font-size: 24px; margin-bottom: 0 !important; padding-bottom: 0; }
        	#header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
        	h1, h2, h3, h4, h5, h6 {margin: 0 0 0.8em 0;}
        	h3 {font-size: 28px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
        	h4 {font-size: 22px; color: #4A72AF !important; font-family: Arial, Helvetica, sans-serif; }
        	h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
        	p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
           </style>
        </head>


        <body>


        <table width="100%" cellpadding="0" cellspacing="0"><tr><td>


        <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
        		<tr>
        			<td align="center">
        				<p>Trouble viewing this email? <a href="#">View in Browser</a></p>
        			</td>
        		</tr>
        	</table><!-- top message -->


        <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="#ffffff">
        		<tr>
        			<td>
        				<table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="#ff0000">
        					<tr>
        						<td width="570"><h1>The WolfPost</h1></td>
        					</tr>
        					<tr>
        						<td width="570"><h1>News and Events</h1></td>
        					</tr>
        					<tr>
        						<td width="570" align="right"><p>July 2010</p></td>
        					</tr>
        				</table><!-- header -->
        			</td>
        		</tr><!-- header -->

        		<tr>
        			<td></td>
        		</tr>"""
    bottom = """	<tr>
    			<td height="30"><img src="http://dummyimage.com/570x30/fff/fff" /></td>
    		</tr>
    		<tr>
    			<td>
    				<table id="content-6" cellpadding="0" cellspacing="0" align="center">
    					<p align="center">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
    					<p align="center"><a href="#">CALL TO ACTION</a></p>
    				</table>
    			</td>
    		</tr>

    	</table><!-- main -->
    	<table id="bottom-message" cellpadding="20" cellspacing="0" width="600" align="center">
    		<tr>
    			<td align="center">
    				<p>You are receiving this email because you signed up for updates</p>
    				<p><a href="#">Unsubscribe instantly</a> | <a href="#">Forward to a friend</a> | <a href="#">View in Browser</a></p>
    			</td>
    		</tr>
    	</table><!-- top message -->
    </td></tr></table><!-- wrapper -->
    </body>
    </html>
    """

    body = ''
    for key in news_link_dict:
        response = requests.get(news_link_dict[key])
        dict_response = response.json()

        #Get top article for new source
        title = dict_response['articles'][0]['title']
        text = dict_response['articles'][0]['description']
        url =  dict_response['articles'][0]['url']
        image = dict_response['articles'][0]['urlToImage']

        core = """
    		<tr>
    			<td>
    				<table id="content-1" cellpadding="0" cellspacing="0" align="center">
    					<tr>
    						<td width="170" valign="top">
    							<table cellpadding="5" cellspacing="0">
    								<tr><td bgcolor="d0d0d0"><img src=\""""+image+"""\" width="270" /></td></tr></table>
    						</td>
    						<td width="15"></td>
    						<td width="275" valign="top" colspan="3">
    							<h3>"""+title+"""</h3>
    							<h4>"""+text+"""</h4>
    							<h5><a href=\""""+url+"""\">Read more..</a>
    						</td>
    					</tr>
    				</table><!-- content 1 -->
    			</td>
    		</tr><!-- content 1 -->"""

        body += core
    return heading + body + bottom



@home.route('/email')
def email():
    return construct_email()
