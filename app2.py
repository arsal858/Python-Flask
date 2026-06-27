from flask import Flask
app=Flask(__name__)

@app.route("/Home_page")
def home_page():
    return "<h1><b>My Home Page Menu</b></h1>"