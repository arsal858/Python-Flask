from flask import flask

app=flask(__name__)

@app.route('basic html page')
def basic_html_page():
    return '<h1>My first Page Creation in Flask</h1>'