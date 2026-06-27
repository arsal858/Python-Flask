from flask import Flask

app=Flask(__name__)

from flask import Flask
app = Flask(__name__)

@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f'The user entered some {user_input}'