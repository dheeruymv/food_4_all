from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from .app import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('signin-email')
    password = request.form.get('signin-password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    # if the above check passes, then we know the user has the right credentials
    # login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('login.html')
    else: # if the request is POST, then we check if the email
          # doesn't already exist and then we save data
        # code to validate and add user to database goes here
        email = request.form.get('signup-email')
        name = request.form.get('signup-username')
        password = request.form.get('signup-password')

        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to login page so user can try again
            flash('Email address already exists')
            # return redirect(url_for('auth.login'))
            return redirect(url_for('main.recommands'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        # return redirect(url_for('auth.login_post'))
        return redirect(url_for('auth.users'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/users')
def list():
    users = db.session.execute(db.select(User).order_by(User.name)).scalars()
    return render_template("db_records.html", users=users)
