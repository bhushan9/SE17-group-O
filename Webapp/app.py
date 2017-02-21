from flask import Flask, render_template, request, json, session, flash
from wtforms import Form
from flaskext.mysql import MySQL
import sys
from werkzeug import generate_password_hash as gph, check_password_hash as cph
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'WolfPost'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def index():
	return render_template('index.html')
	flash("in the first page")
	#return "Welcome!"
@app.route("/showSignUp")
def showsignup():
	return render_template('signup.html')
	Flask.flash("Inside signup")
@app.route("/signUp", methods = ['POST','GET'])
def signup():
	try:
		name = request.form['inputName']
		email = request.form['inputEmail']
		password = request.form['inputPassword']
		print name
		if name and email and password:
			
			con = MySQL.connect()
			cursor = con.cursor()
			encrypted_password = gph(password)
			cursor.callproc('sp_createUser', (name,email,encrypted_password))
			data = cursor.fetchall()
			if(len(data) == 0):
				return json.dumps({'message':'User created successfully!'})
			else:
				return json.dumps({'error':str(data[0])})	
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:	
		cursor.close()
		con.close()		
if __name__ == "__main__":
    app.run()	