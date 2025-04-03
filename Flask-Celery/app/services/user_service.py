from app.models.user import User
from app.extensions import db
from app.tasks.email_task import send_async_email

class UserService:
    """Service class for User CRUD operations"""

    @staticmethod
    def get_all_users():
        """Fetch all users"""
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        """Fetch user by ID"""
        return User.query.get(user_id)

    @staticmethod
    def create_user(name, email):
        """Create a new user"""
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        send_async_email.delay(
            "Welcome", 
            f"Hello {email}, your account has been created", 
            email
        )
        return new_user

    @staticmethod
    def update_user(user_id, name=None, email=None):
        """Update user details"""
        user = User.query.get(user_id)
        if not user:
            return None
        
        if name:
            user.name = name
        if email:
            user.email = email

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        """Delete a user"""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
