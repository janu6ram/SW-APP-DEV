import os

from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Set up database

db = SQLAlchemy(app)

class USERS(db.Model) :
    __tablename__ = "USERS"
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = True)
    gender = db.Column(db.String, nullable = False)

def main():
    db.create_all()

if __name__=="__main__":
    with app.app_context():
        main()
