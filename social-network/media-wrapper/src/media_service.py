import json
from typing import List
from my_struct import Media

# socialNetwork/src/MediaService/MediaHandler.h
def compose_media(req_id: int, media_types: List[str], media_ids: List[int]):

    # initialize the list of Media objects
    _return = []

    if len(media_types) != len(media_ids):
        raise Exception("The lengths of media_id list and media_type list are not equal.")

    for i in range(len(media_ids)):
        new_media = Media()
        new_media.media_id = media_ids[i]
        new_media.media_type = media_types[i]
        _return.append(new_media)

    # serialize the Media objects into dictionaries
    serialized_media = []
    for media in _return:
        media_dict = {
            "media_id": media.media_id,
            "media_type": media.media_type
        }
        serialized_media.append(media_dict)

    # convert the list of dictionaries into a JSON string so we can call it in our lambda handler
    return json.dumps(serialized_media)
