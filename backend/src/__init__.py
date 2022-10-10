"""
Food for all application.
"""

import json
from importlib import import_module

from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# from .routes import food_api

db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)


def register_blueprints(app):
    for app_name in ('user_management', 'food_for_all'):
        application = import_module('src.{}.routes'.format(app_name))
        app.register_blueprint(application.blueprint)


def configure_db(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    """Construct the core app object."""
    app = Flask(__name__)
    # app.config.from_object('food_for_all.config.BaseConfig')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_db(app)

    @app.after_request
    def after_request(response):
        if int(response.status_code) >= 400:
            response_data = json.loads(response.get_data())
            if "errors" in response_data:
                response_data = {"success": False,
                                 "msg": list(response_data["errors"].items())[0][1]}
                response.set_data(json.dumps(response_data))
            response.headers.add('Content-Type', 'application/json')
        return response

    @app.shell_context_processor
    def make_shell_context():
        return {
            "app": app,
            "db": db
        }

    return app
