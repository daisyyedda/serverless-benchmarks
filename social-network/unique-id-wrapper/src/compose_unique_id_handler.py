import json
import logging
from compose_unique_id import compose_unique_id

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def compose_unique_id_handler(event, context):
    try:
        result = compose_unique_id()
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
NONE

example curl command:
curl https://ydbrv3yp2aeod5lfxwuf6fqdga0fwblu.lambda-url.us-east-2.on.aws/
'''