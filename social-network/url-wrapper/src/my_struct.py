'''
a place for defining the structures
'''
class PostType(object):
    POST = 0
    REPOST = 1
    REPLY = 2
    DM = 3

    _VALUES_TO_NAMES = {
        0: "POST",
        1: "REPOST",
        2: "REPLY",
        3: "DM",
    }

    _NAMES_TO_VALUES = {
        "POST": 0,
        "REPOST": 1,
        "REPLY": 2,
        "DM": 3,
    }


class User(object):
    """
    Attributes:
     - user_id
     - first_name
     - last_name
     - username
     - password_hashed
     - salt

    """

    def __init__(self, user_id=None, first_name=None, last_name=None, username=None, password_hashed=None, salt=None,):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password_hashed = password_hashed
        self.salt = salt
    
    # def read(self, iprot):
    #     pass

    # def write(self, oprot):
    #     pass

    # def validate(self):
    #     return

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, __o: object) -> bool:
    #     pass


class Media(object):
    '''
    Attributes:
    - media_id
    - media_type
    '''
    def __init__(self, media_id=None, media_type=None):
        self.media_id = media_id
        self.media_type = media_type

    # def read(self, iprot):
    #     pass

    # def write(self, oprot):
    #     pass

    # def validate(self):
    #     return

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, __o: object) -> bool:
    #     pass


class Url(object):
    '''
    Attributes:
    - shortened_url
    - expanded_url
    '''

    def __init__(self, shortened_url=None, expanded_url=None):
        self.shortened_url = shortened_url
        self.expanded_url = expanded_url

    # def read(self, iprot):
    #     pass

    # def write(self, oprot):
    #     pass

    # def validate(self):
    #     return

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, __o: object) -> bool:
    #     pass


class UserMention(object):
    '''
    Attributes:
    - user_id
    - username
    '''

    def __init__(self, user_id=None, username=None):
        self.user_id = user_id
        self.username = username
    
    # def read(self, iprot):
    #     pass

    # def write(self, oprot):
    #     pass

    # def validate(self):
    #     return

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, __o: object) -> bool:
    #     pass


class Creator(object):
    '''
    Attributes:
    - user_id
    - username
    '''
    def __init__(self, user_id=None, username=None):
        self.user_id = user_id
        self.username = username
    
    # def read(self, iprot):
    #     pass

    # def write(self, oprot):
    #     pass

    # def validate(self):
    #     return

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, __o: object) -> bool:
    #     pass


class TextServiceReturn(object):
    '''
    Attributes:
    - text
    - user_mentions
    - urls
    '''

    def __init__(self, text=None, user_mentions=None, urls=None):
        self.text = text
        self.user_mentions = user_mentions
        self.urls = urls
    
    # def read(self, iprot):
    #     pass

    # def write(self, iprot):
    #     pass

    # def validate(self):
    #     pass

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, other) -> bool:
    #     return not (self == other)


class Post(object):
    '''
    Attributes:
    - post_id
    - creator
    - req_id
    - text
    - user_mentions
    - media
    - urls
    - timestamp
    - post_type
    '''
    def __init__(self, post_id=None, creator=None, req_id=None, text=None, user_mentions=None, media=None, urls=None, timestamp=None, post_type=None,):
        self.post_id = post_id
        self.creator = creator
        self.req_id = req_id
        self.text = text
        self.user_mentions = user_mentions
        self.media = media
        self.urls = urls
        self.timestamp = timestamp
        self.post_type = post_type
    
    # def read(self, iprot):
    #     pass

    # def write(self, oprot):
    #     pass

    # def validate(self):
    #     return

    # def __repr__(self) -> str:
    #     pass

    # def __eq__(self, __o: object) -> bool:
    #     pass

    # def __ne__(self, __o: object) -> bool:
    #     pass
