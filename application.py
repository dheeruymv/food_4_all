from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommands')
def recommands():
    return render_template('recommands.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/fav_receipies')
def fav_receipies():
    return render_template('fav_receipies.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
