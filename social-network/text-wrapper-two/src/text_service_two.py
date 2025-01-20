import re
import json
from typing import List, Dict
from my_struct import TextServiceReturn

def compose_text_two(req_id: int, text: str, urls: List[Dict[str, str]], user_mentions: List[Dict[str, str]]):
    updated_text = text
    
    # Ensure that URLs are separated from the text properly
    for url_data in urls:
        expanded_url = url_data['expanded_url']
        shortened_url = url_data['shortened_url']
        updated_text = updated_text.replace(expanded_url, shortened_url)
    
    res = TextServiceReturn()
    res.text = updated_text
    res.urls = urls
    res.user_mentions = user_mentions
    
    # serialize the TextServiceReturn object
    serialized_text = [{
        "text": res.text,
        "user_mentions": res.user_mentions,
        "urls": res.urls
    }]

    return json.dumps(serialized_text)
