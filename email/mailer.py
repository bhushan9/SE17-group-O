import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import codecs 
import pynliner
import datetime
from bs4 import BeautifulSoup as bs
import requests
fromaddr = "rohitnambisan99@gmail.com"
toaddr = "zithomas@ncsu.edu"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Daily News"
msg.preamble = """
Your mail reader does not support the report format.
Please visit us <a href="http://www.mysite.com">online</a>!"""
texts = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
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
heading_soup = bs(heading,'html.parser')
p_vlaues = heading_soup.findAll('p')
p_vlaues[1].string = datetime.datetime.now().strftime('%B %d, %Y')
heading = str(heading_soup)		

body = heading	
for key in news_link_dict:
    html = """
		<tr>
			<td>
				<table id="content-1" cellpadding="0" cellspacing="0" align="center">
					<tr>
						<td width="170" valign="top">
							<table cellpadding="5" cellspacing="0">
								<tr><td bgcolor="d0d0d0"><img src="http://tessat.s3.amazonaws.com/coins_small.jpg" width="270" /></td></tr></table>
						</td>
						<td width="15"></td>
						<td width="275" valign="top" colspan="3">
							<h3>All New Site Design</h3>
							<h4>It's 150% Better and 40% More Efficient!</h4>
							<h5><a href="">Read more..</a> 
						</td>
					</tr>
				</table><!-- content 1 -->
			</td>
		</tr><!-- content 1 -->"""
    response = requests.get(news_link_dict[key])
    dict_response = response.json()

        #Get top article for new source
    title = dict_response['articles'][0]['title']     
    text = dict_response['articles'][0]['description']
    url =  dict_response['articles'][0]['url']
    image = dict_response['articles'][0]['urlToImage']
    #print title
    soup = bs(html, 'html.parser')
    img = soup.find('img')
    img['src'] = image
    title_html = soup.find('h3')
    title_html.string = title
    desc = soup.find('h4')
    desc.string = text
    a = soup.find('a')
    a['href'] = url
    body+=str(soup)
		
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
#smsg.attach(MIMEText(texts, 'plain'))
#body+=bottom
msg.attach(MIMEText(body, 'html'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "manchesterutd")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
