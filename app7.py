from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100))
    date_joinded=db.Column(db.DateTime)

def insert_data():
    from datetime import datetime
    new_user=User(name="Arslan Shahzad Gondal",date_joined=datetime.now())
    db.session.add(new_user)
    db.session.commit()

