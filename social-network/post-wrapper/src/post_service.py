import json
from my_struct import *
from datetime import datetime

def post_service(post_id, creator, text_return, media, req_id, post_type):
    timestamp = int(datetime.now().timestamp() * 1000)

    new_post = Post()
    new_post.post_id = post_id
    new_post.creator = creator
    new_post.req_id = req_id
    new_post.text_return = text_return.text
    new_post.user_mentions =  text_return.user_mentions
    new_post.media = media
    new_post.urls = text_return.urls
    new_post.timestamp = timestamp
    new_post.post_type = post_type

    # serialize the Post object into dict
    serialized_post = []
    post_dict = {
        "post_id"
        "creator"
        "req_id"
        "text"
        "user_mentions"
        "media"
        "urls"
        "timestamp"
        "post_type"
    }
    serialized_post.append(post_dict)

    return json.dumps(serialized_post)
