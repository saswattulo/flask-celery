from app import create_app
from app.celery_config import make_celery
# from app.extensions import make_celery

flask_app = create_app()

Celery = make_celery(flask_app)