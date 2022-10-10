"""
"""
from flask import Blueprint

blueprint = Blueprint(
    'user_management_blueprint',
    __name__,
    url_prefix=''
)
