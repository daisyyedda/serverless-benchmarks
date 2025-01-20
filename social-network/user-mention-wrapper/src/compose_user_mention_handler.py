import json
import logging
from compose_user_mention import compose_user_mention

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def compose_user_mention_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  
    
    req_id = body.get('req_id')
    usernames = body.get('usernames')

    try:
        result = compose_user_mention(req_id=req_id, usernames=usernames)
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
  "req_id": 12345,
  "usernames": [
    "daisyyedda",
    "janesunnn",
    "llollolmao"
  ]
}

example curl command:
curl -v 'https://imc4qcxp2tn47h3u2t4yokrc4u0gcuen.lambda-url.us-east-2.on.aws/' \
-H 'content-type: application/json' \
-d '{
  "req_id": 12345,
  "usernames": [
    "daisyyedda",
    "janesunnn",
    "wizmyphone"
  ]
}'
'''