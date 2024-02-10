from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "hello"

@app.route('/hello')

def index():
	flash("What's your name?")
	return render_template('index.html')

@app.route("/greet", methods=['POST', 'GET'])
def greet():
	request.form['name_input']
	flash("Hi " + str(request.form['name_input'] + ", great to see you!"))
	return render_template('index.html')

	