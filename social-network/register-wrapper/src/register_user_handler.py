import json
import logging
from register_user import register_user

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def register_user_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  
    
    req_id = body.get('req_id')
    user_id = body.get('user_id')
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    username = body.get('username')
    password = body.get('password')
    
    try:
        result = register_user(req_id, user_id, first_name, last_name, username, password)
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": 'true'
            },
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": 'true'
        },
        'body': json.dumps(result)
    }
  

'''
example JSON input:
{
  "req_id": 0,
  "user_id": "",
  "first_name": "Daisy",
  "last_name": "Ye",
  "username": "daisyyedda",
  "password": "abcdefg123!"
}

example curl command:
curl -v 'https://di72na4lnmwb6wvxcpi5h7evbm0xfzcq.lambda-url.us-east-2.on.aws/' \
-H 'content-type: application/json' \
-d '{
  "req_id": 0,
  "user_id": "",
  "first_name": "Daisy",
  "last_name": "Ye",
  "username": "daisyyedda",
  "password": "abcdefg123!"
}'
'''


