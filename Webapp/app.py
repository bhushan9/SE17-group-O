from flask import Flask, render_template, request, json, session
from wtforms import Form
import sys
app = Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')
	#return "Welcome!"
@app.route("/showSignUp")
def showsignup():
	return render_template('signup.html')

@app.route("/signup", methods = ['POST'])
def signup():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	if _name and _email and _password:
		return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()	