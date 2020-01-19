from flask import Flask, jsonify, request
import uuid
import boto3
import os

app = Flask(__name__)

#client = boto3.client('dynamodb', region_name="eu-west-2")
CONTACTS_TABLE = os.environ.get('CONTACTS_TABLE', 'contacts')

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/submissions', methods=['POST'])
def submit_contact():
    data = request.json

    for item in ['first_name', 'last_name', 'email', 'message']:
        if item not in data:
            return jsonify({
                    'status': 'error',
                    'message': f'Missing required {item} parameter'
                    }), 400

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    message = data.get('message')

    submission_id = uuid.uuid4().hex

#    client.put_item(
#            TableName=CONTACTS_TABLE,
#            Item= {
#                'id': {'S': submission_id},
#                'first_name': {'S': first_name},
#                'last_name': {'S': last_name},
#                'email': {'S': email},
##                'message': {'S': message}
#                }
#            )

    return jsonify({
        'status': 'success',
        'submission': {
            'id': submission_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message
            }
        }), 201

if __name__== '__main':
    app.run()
