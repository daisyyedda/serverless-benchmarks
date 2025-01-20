import json
from typing import List
from my_struct import Creator

def compose_creator(req_id: int, user_id: int, username: str):
    # if both user_id and username given, we compose a creator and return
    # if only user_name is given, we need to look up user_id in db
    # since db is not setup yet, we assume the first case
    creator = Creator()
    if user_id != -1:
        creator.user_id = user_id,
        creator.username = username

    serialized_creator = []
    creator_dict = {
        "user_id": creator.user_id,
        "username": creator.username
    }
    serialized_creator.append(creator_dict)
    return json.dumps(creator_dict)
