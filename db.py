import pymongo
from pymongo import MongoClient

cluster = MongoClient("DBTOKEN")
db = cluster["DBNAME"]
collection = db["DBCOLLECTION"]

def insertNewPlayer(discord_id, slippi_code):
    collection.remove({"discord_id": discord_id})
    collection.insert_one({"discord_id": discord_id, "slippi_code": slippi_code })

def findCode(discord_id):
    results = collection.find({"discord_id": discord_id})
    for result in results:
        return(result["slippi_code"])

def findDiscordId(slippi_code):
    results = collection.find({"slippi_code": slippi_code})
    for result in results:
        return(result["discord_id"])