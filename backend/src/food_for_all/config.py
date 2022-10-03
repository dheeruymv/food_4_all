"""
Class holding flask application configurations.
"""
import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../foodforall.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "qwerty"
    JWT_SECRET_KEY = "ytrewq"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
