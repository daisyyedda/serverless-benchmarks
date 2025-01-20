import json
import logging
from media_service import compose_media

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def media_service_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  
    
    req_id = body.get('req_id')
    media_types = body.get('media_types')
    media_ids = body.get('media_ids')
    
    try:
        result = compose_media(req_id=req_id, media_types=media_types, media_ids=media_ids)
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
  "media_types": ["Text", "Image", "Combo"],
  "media_ids": ["111", "222", "333"]
}

example curl command:
curl -v 'https://ed7tqr4pixw7yjaned2evspsoa0dlbuf.lambda-url.us-east-2.on.aws/' \
-H 'content-type: application/json' \
-d '{
  "req_id": 0,
  "media_types": [
    "Text",
    "Image",
    "Combo"
  ],
  "media_ids": [
    "111",
    "222",
    "333"
  ]
}'
'''


