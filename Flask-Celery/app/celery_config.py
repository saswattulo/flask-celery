from celery import Celery

def make_celery(app=None):
    # Create Celery instance without requiring app initially
    celery = Celery(
        'flask_tasks',
        broker='redis://localhost:6379/0',
        backend='redis://localhost:6379/0'
    )

    if app:
        # Configure Celery with Flask app config if an app is provided
        celery.conf.update(app.config)

        class ContextTask(celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        celery.Task = ContextTask

    return celery

# Create a global Celery instance
celery = make_celery()