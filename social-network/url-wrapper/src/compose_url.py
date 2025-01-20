from my_struct import Url
from typing import List
import random
import string
import json

# hard-coding the hostname for now
HOSTNAME = "http://short-url/"

def _gen_random_str(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def compose_url(req_id: int, urls: List[str]):
    target_urls = []
    if urls:
        for url in urls:
            new_target_url = Url()
            new_target_url.expanded_url = url
            new_target_url.shortened_url = HOSTNAME + _gen_random_str(10)
            target_urls.append(new_target_url)
    
    # serialize the Url objects into dictionaries
    serialized_url = []
    for url in target_urls:
        url_dict = {
            "shortened_url": url.shortened_url,
            "expanded_url": url.expanded_url

        }
        serialized_url.append(url_dict)
    # print(serialized_url)
    return json.dumps(serialized_url)


# req_id = 12345
# urls = ["https://www.example.com/?breath=bone&base=boot", 
#             "http://blade.example.com/base/attack",
#             "http://example.com/attraction/activity.aspx",
#             "https://www.example.net/anger.php?argument=afternoon",
#             "https://baseball.example.com/boat/baseball.html#apparel"]


# compose_url(req_id=req_id, urls=urls)