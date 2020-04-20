import os

from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from registerdb import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False




@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        gender = request.form.get("gender")
        new_user=USERS(username=username,password=password,email=email,gender=gender)
        db.session.add(new_user)
        db.session.commit
        print(username,password,email,gender)
        return render_template("success.html")
    return render_template("registration.html")

@app.route("/login.html",methods=["POST","GET"])
def login():
    if request.method == "POST":
        return render_template("success.html")
    return render_template("login.html")
