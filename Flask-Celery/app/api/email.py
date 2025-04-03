from flask_restful import Resource,reqparse
from app.tasks.email_task import send_async_email

class EmailResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('subject', type=str, required=True)
        self.parser.add_argument('message', type=str, required=True)
        self.parser.add_argument('to_email', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        
        # Trigger async email task
        task = send_async_email.delay(
            args['subject'], 
            args['message'], 
            args['to_email']
        )
        
        return {
            'message': 'Email task queued',
            'task_id': task.id
        }