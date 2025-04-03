# from flask import Flask
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api
# from app.config import CeleryConfig,DatabaseConfig
# from app.extensions import db, migrate, jwt, mail, make_celery
# from app.api import api_bp
# from celery import Celery

# celery = Celery(__name__)

# def create_app(env="development"):
#     """Factory function to create and configure the Flask app."""
#     app = Flask(__name__)

#     # Load configuration based on environment
#     app.config.from_object(DatabaseConfig[env])
#     app.config.from_object(CeleryConfig)

#     # Initialize Flask extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     mail.init_app(app)
#     CORS(app)

#     # Initialize Flask-RESTful API
#     api = Api(app)

#     # Initialize Celery with app context
#     celery.conf.update(app.config)

#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)

#     celery.Task = ContextTask

#     # Register API routes
#     from app.api import api_bp
#     app.register_blueprint(api_bp, url_prefix="/api")
#     # global celery
#     # celery = make_celery(app)


#     return appfrom flask import Flask
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.config import CeleryConfig, DatabaseConfig
from app.extensions import db, migrate, jwt, mail
from app.celery_config import make_celery

def create_app(env="development"):
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)

    # Load configuration based on environment
    app.config.from_object(DatabaseConfig[env])
    app.config.from_object(CeleryConfig)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    CORS(app)

    # Create and configure Celery with the app
    # from app.celery_config import make_celery
    # celery = make_celery(app)

    # Register API routes - do this after creating the app
    # from app.api import api_bp, init_routes
    # app.register_blueprint(api_bp, url_prefix="/api")
    from app.api import api
    
    
    # Initialize routes after blueprint registration
    with app.app_context():
        api.init_app(app)

    return app