from flask import Flask, render_template, request, redirect
import newspaper
import nltk
app = Flask(__name__)


def test():
	#d={'dailymail' : 'http://www.dailymail.co.uk/ushome/index.html','bbc':'http://www.bbc.com/news','economist':'http://www.economist.com/'}
	
	dailymail=newspaper.build('http://www.dailymail.co.uk/ushome/index.html')
	if dailymail.articles:
		article=dailymail.articles[0]
	else:
		article = ""
	article.download()
	article.parse()
	return article.text

@app.route('/signup', methods = ['POST','GET'])
def signup():
	if request.method == 'POST':
		value = ''
        	if request.form['submit'] == 'dailymail':
			value = 'dailymail'
        	elif request.form['submit'] == 'cnn':
			value = 'cnn'

		return value + ' \r ' + test()

	elif request.method == 'GET':
		pass

@app.route("/")
def main():
	return render_template("index.html")
    #return "Welcome!"

if __name__ == "__main__":
    app.run()    








