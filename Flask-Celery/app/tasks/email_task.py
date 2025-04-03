from app.celery_config import celery
from app.extensions import mail
from flask_mailman import EmailMessage
from app import create_app
from app.config.celery_config import CeleryConfig

@celery.task
def send_async_email(subject, body, recipient):
    app = create_app()
    with app.app_context():
        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email="tulosaswat@gmail.com",
                to=[recipient]
            )
            email.send()
            return f"Email sent to {recipient}"
        except Exception as e:
            print(f"Email sending failed: {str(e)}")
            return f"Failed to send email to {recipient}"