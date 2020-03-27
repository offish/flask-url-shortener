from lib.shrink import generate
import string
import pymongo
import time


client = pymongo.MongoClient("localhost", 27017)

db = client["db"]
col = db["shortified"]


def add(url: str):
    url_exist = col.find_one({"url": url})

    if url_exist:
        print('Error: URL is already in database')
        return
    
    shrinked = generate(url)
    shrink_exist = col.find_one({"shrinked": shrinked})

    if shrink_exist:
        print('Error: Shrinked URL is already in database, generating a new one.')
        add(url)
    
    else:
        data = {
            "url": url,
            "shrinked": shrinked,
            "clicks": 0,
            "created": int(time.time())
        }
        col.insert(data)
        print(f'Success: New URL ({data["url"]}) and Shrinked URL ({data["shrinked"]}) added to database.')
