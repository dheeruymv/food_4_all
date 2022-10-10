"""
Class holding flask application configurations.
"""
import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../foodforall.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'f00dF0r@ll$ecret')

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

    DEBUG = True


config_dict = {
    'dev': Config
}
