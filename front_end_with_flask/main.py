from flask import Blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from .app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/recommands')
def recommands():
    return render_template('recommands.html')

@main.route('/post')
def post():
    return render_template('post.html')

@main.route('/fav_receipies')
def fav_receipies():
    return render_template('fav_receipies.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# @main.route('/login')
# def login():
#     return render_template('login.html')