"""
Entry point of flask application.
"""
import os
from sys import exit
from flask_migrate import Migrate
from flask_minify import Minify

from src.config import config_dict
from src import create_app, db

DEBUG = True

try:
    app_config = config_dict['dev']
except KeyError:
    exit('Error: Invalid config.')

app = create_app(app_config)
Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG))
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE')
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT)

if __name__ == "__main__":
    # app = create_app()
    app.run(debug=True, host="0.0.0.0")
