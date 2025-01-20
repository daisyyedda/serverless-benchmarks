import json
import logging
from compose_creator import compose_creator

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def compose_creator_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  
    
    req_id = body.get('req_id')
    user_id = body.get("user_id")
    username = body.get("username")
    
    try:
        result = compose_creator(req_id, user_id, username)
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
  "user_id": 8273918981211213824,
  "username": "daisyyedda"
}

example curl command:
curl -v 'https://ixerypob4boq4uem3fadszlvae0qokhj.lambda-url.us-east-2.on.aws/' \
-H 'content-type: application/json' \
-d '{
  "req_id": 0,
  "user_id": 8273918981211213824,
  "username": "daisyyedda"
}'
'''


