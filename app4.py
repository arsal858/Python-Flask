from flask import Flask

app=Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the App"
app.route("/home")
def home():
    return "<h1>Welcome to Learning Journey of Flask</h1>"
app.post("/greet")
def greet():
    return "Hello sir"