from flask import Flask, render_template, request, send_file, send_from_directory, safe_join, redirect, url_for, flash
import pytube
import instaloader
import os
import os.path
import sys
from instaloader import Post
from instaloader import Profile
import time
import re
import requests as r
import wget
from flask_mail import Mail, Message
import smtplib
import json
import urllib
import pafy
import asyncio
import youtube_dl

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['INSTA_USER_NAME'] = os.environ.get('INSTA_USER_NAME')
app.config['INSTA_PASS'] = os.environ.get('INSTA_PASS')
app.config['SITE_KEY'] = os.environ.get('SITE_KEY')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
mail = Mail(app)


@app.route('/')
def home():
    os.system(
        f"instaloader  --login={app.config['INSTA_USER_NAME']} --password={app.config['INSTA_PASS']}")
    return render_template("main.html")

@app.route('/youtube')
def youtube():
    return render_template("yt.html")


@app.route('/instagram')
def instagram():
    (f"instaloader  --login={app.config['INSTA_USER_NAME']} --password={app.config['INSTA_PASS']}")
    return render_template("insta.html")


@ app.route('/facebook')
def facebook():
    return render_template("fb.html")


@ app.route('/aboutus')
def aboutus():
    return render_template("about.html")


@ app.route('/contactus')
def contactus():
    return render_template("contact.html", site_key=str(app.config['SITE_KEY']))

if __name__ == '__main__':
    app.run()
