import json
import logging
from text_service_one import compose_text_one

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def text_service_handler_one(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event.get('body', '{}'))
    except json.JSONDecodeError:
        body = {}  
        
    logger.info(body)

    # extract needed values from payload
    req_id = body.get('req_id')
    text = body['text']

    logger.info(text)

    try:
        result = compose_text_one(req_id=req_id, text=text)
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
  "text": "Today is such a beautiful day, grabbed brunch with @daisyyedda, 
  @janesunnn, and @wizmyphone. Click into the following links for a promo code: 
  https://www.example.com/?breath=bone&base=boot, 
  http://blade.example.com/base/attack,
  http://example.com/attraction/activity.aspx!!!!
  Love u all! <3"
}

example curl command:
curl -v 'https://hzxpe6c2alzifcul6b5oqhpkaa0eekcy.lambda-url.us-east-2.on.aws/' \
-H 'content-type: application/json' \
-d '{
  "req_id": 12345,
  "text": "Today is such a beautiful day, grabbed brunch with @daisyyedda, @janesunnn, and @wizmyphone. Click into the following links for a promo code: https://www.example.com/?breath=bone&base=boot, http://blade.example.com/base/attack, http://example.com/attraction/activity.aspx!!!! Love u all! <3"
}'
'''

