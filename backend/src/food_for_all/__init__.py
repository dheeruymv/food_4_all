"""
"""
from flask import Blueprint

blueprint = Blueprint(
    'food_for_all_blueprint',
    __name__,
    url_prefix=''
)

# """
# Food for all application.
# """
#
# import json
#
# from flask import Flask
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
#
#
# from .routes import food_api
# db = SQLAlchemy()
#
#
# def create_app():
#     """Construct the core app object."""
#     app = Flask(__name__)
#     app.config.from_object('food_for_all.config.BaseConfig')
#
#     db.init_app(app)
#
#     from user_management.routes import um_api
#     um_api.init_app(app)
#     # food_api.init_app(app)
#     CORS(app)
#
#     #Setup Database
#     @app.before_first_request
#     def initialize_database():
#         db.create_all()
#
#     @app.after_request
#     def after_request(response):
#         if int(response.status_code) >= 400:
#             response_data = json.loads(response.get_data())
#             if "errors" in response_data:
#                 response_data = {"success": False,
#                                  "msg": list(response_data["errors"].items())[0][1]}
#                 response.set_data(json.dumps(response_data))
#             response.headers.add('Content-Type', 'application/json')
#         return response
#
#     @app.shell_context_processor
#     def make_shell_context():
#         return {
#             "app": app,
#             "db": db
#         }
#
#     return app
