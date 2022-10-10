"""This module contains flask forms for user registration,
login and password reset.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length, Optional)


# login and registration
class LoginForm(FlaskForm):
    username = StringField('Username',
                           id='username_login',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                       id="name",
                       validators=[DataRequired()])
    username = StringField('Username',
                           id='username_create',
                           validators=[DataRequired()])
    email = StringField('Email',
                        id='email_create',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Password',
                                     id='cnf_pwd',
                                     validators=[DataRequired()])
