import json
import logging
from post_service import post_service

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post_service_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  

    post_id = body.get('post_id')
    creator = body.get('creator')
    req_id =  body.get('req_id')
    text_return = body.get('text_return')
    media = body.get('media')
    post_type = body.get('post_type')
    
    try:
        result = post_service(post_id, creator, text_return, media, req_id, post_type)
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
curl -v 'https://phaqx465nv3b2mwjrnrwzuaqmy0kzlfu.lambda-url.us-east-2.on.aws/' \
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
