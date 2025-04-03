from flask_restful import Resource, reqparse
from app.services.user_service import UserService

class UserListResource(Resource):
    """Handles GET and POST for the User list"""

    def get(self):
        """Fetch all users"""
        users = UserService.get_all_users()
        return [{"id": u.id, "name": u.name, "email": u.email} for u in users], 200

    def post(self):
        """Create a new user"""
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name is required")
        parser.add_argument("email", type=str, required=True, help="Email is required")
        args = parser.parse_args()

        user = UserService.create_user(args["name"], args["email"])
        return {"message": "User created", "user": {"id": user.id, "name": user.name, "email": user.email}}, 201


class UserResource(Resource):
    """Handles GET, PUT, DELETE for a single User"""

    def get(self, user_id):
        """Fetch a user by ID"""
        user = UserService.get_user_by_id(user_id)
        if user:
            return {"id": user.id, "name": user.name, "email": user.email}, 200
        return {"message": "User not found"}, 404

    def put(self, user_id):
        """Update user information"""
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("email", type=str)
        args = parser.parse_args()

        updated_user = UserService.update_user(user_id, args["name"], args["email"])
        if updated_user:
            return {"message": "User updated", "user": {"id": updated_user.id, "name": updated_user.name, "email": updated_user.email}}, 200
        return {"message": "User not found"}, 404

    def delete(self, user_id):
        """Delete a user"""
        if UserService.delete_user(user_id):
            return {"message": "User deleted"}, 200
        return {"message": "User not found"}, 404
