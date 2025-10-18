from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "testdb")

client = AsyncIOMotorClient(MONGO_URL)
database = client[DB_NAME]

def get_database():
    return database
