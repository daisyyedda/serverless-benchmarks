import json
import sys
import logging
import pymysql
from typing import List
from my_struct import UserMention

def compose_user_mention(req_id: int, usernames: List[str]):
    user_mentions = []

    # db credentials (TODO: in the future, we should be storing the credentials in a config file as opposed to hardcoding)
    rds_host = "social-network-db.cxqkgkcsu34o.us-east-2.rds.amazonaws.com"
    rds_port = 3306
    rds_username = "admin"
    rds_password = "123456789"

    # logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # establish db connection
    try:
        conn = pymysql.connect(
            host=rds_host, 
            user=rds_username, 
            port=rds_port, 
            passwd=rds_password,
            db='social-network-db',
        )
    except pymysql.MySQLError as e:
        logger.error("Connection to MySQL database failed.")
        logger.error(e)
        sys.exit()

    # look up user_ids of usernames
    user_ids = []
    for username in usernames:
        with conn.cursor() as cur:
            query = "SELECT user_id FROM `default`.`user` WHERE username = ?"
            cur.execute(query, (username,))
            for id in cur:
                user_ids.append(id)
        conn.commit()
    
    # create UserMention objects
    idx = 0
    if usernames:
        for username in usernames:
            new_user = UserMention()
            new_user.user_id = user_ids[idx]
            new_user.username = username
            user_mentions.append(new_user)
            idx += 1

    # serialize the UserMention objects into dictionaries
    serialized_user_mention = []
    for new_user in user_mentions:
        new_user = {
            "user_id": new_user.user_id, # hard coded user_Id
            "user_name": new_user.username
        }
        serialized_user_mention.append(new_user)

    print(serialized_user_mention)
    return json.dumps(serialized_user_mention)


# testing
req_id = 1111
usernames = ["daisyyedda", "nickgza"]
compose_user_mention(req_id=req_id, usernames=usernames)