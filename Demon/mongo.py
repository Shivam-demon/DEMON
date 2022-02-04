import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Demon import MONGO_DB_URI


MONGO_PORT = "27017"
MONGO_DB_URI = "mongodb+srv://Shivamdemon:Shivam123@cluster0.livbp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGO_DB = "Demonbot"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, 27017)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, 27017)
db = motor[MONGO_DB]
db = client["Demonbot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
