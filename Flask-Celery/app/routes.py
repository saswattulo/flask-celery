from app.api.user import UserResource, UserList
# from app.api.auth import AuthLogin, AuthRegister

def register_routes(api):
    """Register all API routes."""
    api.add_resource(UserList, "/api/users")
    api.add_resource(UserResource, "/api/users/<int:user_id>")
    # api.add_resource(AuthLogin, "/api/auth/login")
    # api.add_resource(AuthRegister, "/api/auth/register")
