"""
"""
from flask_restx import Api, Resource, fields


food_api = Api(version="1.0", title="Food for All API",
               default="Food for All",
               default_label="APIs for recipe recommendation.")


@food_api.route('/api/food/test')
class LogoutUser(Resource):
    """
       Logs out User using 'logout_model' input
    """
    def get(self):
        return {"success": True}, 200
