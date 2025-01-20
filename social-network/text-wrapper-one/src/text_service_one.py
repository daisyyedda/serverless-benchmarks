import re
import json
from my_struct import TextServiceReturn

'''
part one of compose text
- extract all user mentions
- extract all urls
'''
def compose_text_one(req_id: int, text: str):
    # extract all user mentions and append them to existing ones
    mention_usernames = re.findall(r"@[a-zA-Z0-9-_]+", text)
    # remove @
    user_mentions = [username[1:] for username in mention_usernames]
    # extract all urls
    urls = re.findall(r"https?://[^!\s,]+", text)

    # create a TextServiceReturn object
    res = TextServiceReturn()
    res.user_mentions = user_mentions
    res.text = text
    res.urls = urls

    # serialize the Text object
    serialized_text = []
    text_obj = {
        "text": res.text,
        "user_mentions": res.user_mentions,
        "urls": res.urls
    }
    serialized_text.append(text_obj)

    return json.dumps(serialized_text)
