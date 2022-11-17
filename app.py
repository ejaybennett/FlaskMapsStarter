#The goal of this project is to make a "Where you're from" section for our website. 
#Users will be able to drop a pin on thier current location, and the map of all users' 
#Locations will be displayed along with a bar graph with the users' home states 
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
import requests
import json 
from secrets_app import geoip_secret, googlemaps_secret, URI
import socket
import urllib
from flask_googlemaps import GoogleMaps, Map
import matplotlib.pyplot as plt, mpld3

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['GOOGLEMAPS_KEY'] = googlemaps_secret
GoogleMaps(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


def get_user_location(request):
    pass

#Add a User class inheriting from UserMixin here. Make sure the primary key is called id.
#Also add state and country as Strings, latutitude and longitude as floats

class User(db.Model, UserMixin):
    pass

db.create_all()
    
#Add a user_loader function here, which should return None if the given id is not in our database
#and the User object with the given id if it is
@login_manager.user_loader
def load_user(id):
    pass

#Add the login/signup form here

#Add route for home here, just rendering a home.html
@app.route("/", methods = ["GET"])
@login_required
def home():
    return "Placeholder"


app.run()