from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to Flask</h1>"

@app.route("/home")
def home():
    return "<h1>Home</h1>"

@app.route("/json")
def my_key():
    return {'my_key':'json','values':[1,2,3]}
