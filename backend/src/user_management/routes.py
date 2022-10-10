"""
"""

import json
from functools import wraps
from datetime import datetime, timezone, timedelta

import jwt
import flask
from flask_restx import Api, Resource, fields
from flask import request, Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from src import db, login_manager
from src.user_management import blueprint
from src.user_management.forms import LoginForm, RegistrationForm
from src.user_management.models import Users
from src.user_management.utils import verify_pass


api = Api(blueprint)


@blueprint.route('/')
def route_default():
    return redirect(url_for('user_management_blueprint.login'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)

    if flask.request.method == 'POST':
        # read form data
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('user_management_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if current_user.is_authenticated:
        return redirect(url_for('food_for_all_blueprint.index'))
    else:
        return render_template('accounts/login.html',
                               form=login_form)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check password matches
        password = request.form['password']
        cnf_password = request.form['confirm_password']
        if password != cnf_password:
            return render_template('accounts/register.html',
                                   msg="Password doesn't match",
                                   success=False,
                                   form=registration_form)

        # Check usename exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=registration_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=registration_form)

        # else we can create the user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()

        return render_template('accounts/register.html',
                               msg='User created successfully.',
                               success=True,
                               form=registration_form)

    else:
        return render_template('accounts/register.html', form=registration_form)


@api.route('/login/jwt/', methods=['POST'])
class JWTLogin(Resource):
    def post(self):
        try:
            data = request.form

            if not data:
                data = request.json

            if not data:
                return {
                           'message': 'username or password is missing',
                           "data": None,
                           'success': False
                       }, 400
            # validate input
            user = Users.query.filter_by(username=data.get('username')).first()
            if user and verify_pass(data.get('password'), user.password):
                try:

                    # Empty or null Token
                    if not user.api_token or user.api_token == '':
                        user.api_token = generate_token(user.id)
                        user.api_token_ts = int(datetime.utcnow().timestamp())
                        db.session.commit()

                    # token should expire after 24 hrs
                    return {
                        "message": "Successfully fetched auth token",
                        "success": True,
                        "data": user.api_token
                    }
                except Exception as e:
                    return {
                               "error": "Something went wrong",
                               "success": False,
                               "message": str(e)
                           }, 500
            return {
                       'message': 'username or password is wrong',
                       'success': False
                   }, 403
        except Exception as e:
            return {
                       "error": "Something went wrong",
                       "success": False,
                       "message": str(e)
                   }, 500

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_management_blueprint.login'))


# Errors
@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500