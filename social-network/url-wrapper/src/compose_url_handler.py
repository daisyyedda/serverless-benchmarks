import json
import logging
from compose_url import compose_url

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def compose_url_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  
    
    req_id = body.get('req_id')
    urls = body.get('urls')

    try:
        result = compose_url(req_id=req_id, urls=urls)
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
  "urls": [
    "https://www.example.com/?breath=bone&base=boot",
    "http://blade.example.com/base/attack",
    "http://example.com/attraction/activity.aspx",
    "https://www.example.net/anger.php?argument=afternoon",
    "https://baseball.example.com/boat/baseball.html#apparel"
  ]
}

example curl command:
curl -v 'https://6gauus4ybeashyu7fuv5z4vwd40alwck.lambda-url.us-east-2.on.aws/' \
-H 'content-type: application/json' \
-d '{
  "req_id": 12345,
  "urls": [
    "https://www.example.com/?breath=bone&base=boot",
    "http://blade.example.com/base/attack",
    "http://example.com/attraction/activity.aspx",
    "https://www.example.net/anger.php?argument=afternoon",
    "https://baseball.example.com/boat/baseball.html#apparel"
  ]
}'
'''
