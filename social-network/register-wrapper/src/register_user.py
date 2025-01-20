import random
import string
import uuid
import json
import hashlib
from datetime import datetime
from my_struct import User

current_timestamp = -1
counter = 0
CUSTOM_EPOCH = 1514764800000

def get_counter(timestamp):
    global current_timestamp, counter

    if current_timestamp > timestamp:
        raise ValueError("Timestamps are not incremental.")
    if current_timestamp == timestamp:
        counter += 1
        return counter - 1
    else:
        current_timestamp = timestamp
        counter = 1
        return counter - 1

def get_random_string(length):
    alphanum = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanum) for _ in range(length))

def register_user(req_id: int, user_id: str, first_name: str, last_name: str, username: str, password: str):
    # if user_id not given, compose user_id
    if user_id == "":
        timestamp = int((datetime.now() - datetime(1970, 1, 1)).total_seconds() * 1000) - CUSTOM_EPOCH
        idx = get_counter(timestamp)

        # convert timestamp to hex and reformat
        timestamp_hex = format(timestamp, 'x')
        if len(timestamp_hex) > 10:
            timestamp_hex = timestamp_hex[-10:]
        elif len(timestamp_hex) < 10:
            timestamp_hex = timestamp_hex.zfill(10)

        counter_hex = format(idx, 'x')
        if len(counter_hex) > 3:
            counter_hex = counter_hex[-3:]
        elif len(counter_hex) < 3:
            counter_hex = counter_hex.zfill(3)

        machine_id = uuid.uuid4().hex
        user_id_str = machine_id + timestamp_hex + counter_hex
        user_id = int(user_id_str, 16) & 0x7FFFFFFFFFFFFFFF
    
    # get salt, hash password
    salt = get_random_string(32)
    password_hashed = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

    # TODO: store user info in mongodb
    # TODO: check if the username has existed in the database

    # register user
    new_user = User()
    new_user.user_id = user_id
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.username = username
    new_user.password_hashed = password_hashed
    new_user.salt = salt

    # serialize the User object into dict
    serialized_user = []
    user_dict = {
        "user_id": new_user.user_id, 
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "username": new_user.username,
        "password_hashed": new_user.password_hashed,
        "salt": new_user.salt
    }
    serialized_user.append(user_dict)

    # print(json.dumps(serialized_user))
    # convert the list of dictionaries into a JSON string so we can call it in our lambda handler
    return json.dumps(serialized_user)


# req_id = 0
# user_id = ""
# first_name = "Daisy"
# last_name = "Ye"
# username = "daisyyedda"
# password = "abcdefg123!"

# register_user(req_id, user_id, first_name, last_name, username, password)