# api/__init__.py
from flask_restful import Api
from flask import Blueprint

# api_bp = Blueprint("api", __name__)
api = Api()


# def init_routes():
#     # Register routes
from .user import UserListResource,UserResource
from .email import EmailResource
api.add_resource(UserListResource, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")
api.add_resource(EmailResource,"/send-email")
