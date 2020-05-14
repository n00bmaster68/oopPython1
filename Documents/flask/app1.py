from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "CAC!!"
@app.route("/HUYTHANG")
def HUYTHANG():
	return "HUY THẮNG!!"
@app.route("/<string:name>")
def Heloo(name):
	name = name.capitalize()
	return f"<h1> hello, {name} </h1>"