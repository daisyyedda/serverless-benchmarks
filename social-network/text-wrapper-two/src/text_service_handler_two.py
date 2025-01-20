import json
import logging
import base64
from text_service_two import compose_text_two

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def text_service_handler_two(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    # check if the body is Base64-encoded
    is_base64_encoded = event.get('isBase64Encoded', False)

    try:
        if is_base64_encoded:
            # decode base 64
            decoded_body = base64.b64decode(event.get('body', ''))
            body = json.loads(decoded_body)
        else:
            body = json.loads(event.get('body', '{}'))
    except (json.JSONDecodeError, base64.binascii.Error) as e:
        logger.error(f"Error decoding event body: {e}")
        body = {}

    # extract needed values from payload
    req_id = body.get('req_id')
    text = body.get('text')
    urls = body.get('urls')
    user_mentions = body.get('user_mentions')

    try:
        result = compose_text_two(req_id=req_id, text=text, urls=urls,
                                  user_mentions=user_mentions)
    except Exception as e:
        logger.error(f"Error in compose_text_two: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": 'true',
            },
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": 'true',
        },
        'body': json.dumps(result)
    }


'''
example JSON input:
{
    "req_id": 12345,
    "text": "Today is such a beautiful day, grabbed brunch with @daisyyedda, @janesunnn, and @wizmyphone. Click into the following links for a promo code: https://www.example.com/?breath=bone&base=boot, http://blade.example.com/base/attack, http://example.com/attraction/activity.aspx!!!! Love u all! <3",
    "urls": {
    {
        "shortened_url": "http://short-url/qjcB9yWWJR",
        "expanded_url": "https://www.example.com/?breath=bone&base=boot"
    },
    {
        "shortened_url": "http://short-url/9ZvoFP7JFa",
        "expanded_url": "http://blade.example.com/base/attack"
    },
    {
        "shortened_url": "http://short-url/YOpXmniCoJ",
        "expanded_url": "http://example.com/attraction/activity.aspx"
    },
    {
        "shortened_url": "http://short-url/XcMAPUn74Y",
        "expanded_url": "https://www.example.net/anger.php?argument=afternoon"
    },
    {
        "shortened_url": "http://short-url/MB3VK1zKJG",
        "expanded_url": "https://baseball.example.com/boat/baseball.html#apparel"
    }
    },
    "user_mentions": {
    {
        "user_id": 10001,
        "user_name": "daisyyedda"
    },
    {
        "user_id": 10001,
        "user_name": "janesunnn"
    },
    {
        "user_id": 10001,
        "user_name": "wizmyphone"
    }
    }
}
  
example curl command:  
curl -v 'https://hpq5phqsu2lcc7jprbph3jn2sq0mduvt.lambda-url.us-east-2.on.aws/' \
-d '{
  "req_id": 12345,
  "text": "Today is such a beautiful day, grabbed brunch with @daisyyedda, @janesunnn, and @wizmyphone. Click into the following links for a promo code: https://www.example.com/?breath=bone&base=boot, http://blade.example.com/base/attack, http://example.com/attraction/activity.aspx!!!! Love u all! <3",
  "urls": [
    {
      "shortened_url": "http://short-url/qjcB9yWWJR",
      "expanded_url": "https://www.example.com/?breath=bone&base=boot"
    },
    {
      "shortened_url": "http://short-url/9ZvoFP7JFa",
      "expanded_url": "http://blade.example.com/base/attack"
    },
    {
      "shortened_url": "http://short-url/YOpXmniCoJ",
      "expanded_url": "http://example.com/attraction/activity.aspx"
    },
    {
      "shortened_url": "http://short-url/XcMAPUn74Y",
      "expanded_url": "https://www.example.net/anger.php?argument=afternoon"
    },
    {
      "shortened_url": "http://short-url/MB3VK1zKJG",
      "expanded_url": "https://baseball.example.com/boat/baseball.html#apparel"
    }
  ],
  "user_mentions": [
    {
      "user_id": 10001,
      "user_name": "daisyyedda"
    },
    {
      "user_id": 10001,
      "user_name": "janesunnn"
    },
    {
      "user_id": 10001,
      "user_name": "wizmyphone"
    }
  ]
}'
'''
