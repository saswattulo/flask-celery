from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mailman import Mail
from celery import Celery

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config.get('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
        backend=app.config.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    )
    celery.conf.update(app.config)
    
    # This line ensures that celery recognizes Flask's app context
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask  # Attach the custom Task class
    return celery