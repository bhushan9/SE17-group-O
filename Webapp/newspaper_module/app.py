from flask import Flask, render_template, request, redirect, jsonify
from sys import argv
import newspaper
import nltk
app = Flask(__name__)


file = open("Dailymail.txt" , 'w')
file.write("hello world")
file.close()

def test(value):
	news_link_dict={'Dailymail' : 'http://www.dailymail.co.uk/ushome/index.html', \
	'BBC':'http://www.bbc.com/news', \
	'The Economist':'http://www.economist.com/' ,\
	'CNN' : 'http://www.cnn.com/', \
	'New York Times' : 'https://www.nytimes.com/', \
	'The Atlantic' : 'https://www.theatlantic.com/',\
	'The Guardian' : 'https://www.theguardian.com/us' }

	news_paper=newspaper.build(news_link_dict[value])
	try:
		article=news_paper.articles[0]

		article.download()
		article.parse()
		article.nlp()
		return article.summary
	except:
		return 'lol sorry'

@app.route('/signup', methods = ['POST','GET'])
def signup():
	if request.method == 'POST':
		value = request.form['submit']
        	

		return jsonify(test(value))
		#return value + ' \r ' +test(value)

	elif request.method == 'GET':
		pass

@app.route("/")
def main():
	
	return render_template("index.html")
    #return "Welcome!"

if __name__ == "__main__":
    app.run()    
