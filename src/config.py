import os
from dotenv import load_dotenv

load_dotenv()

VNEXPRESS_URL = os.getenv("VNEXPRESS_URL")
MONGO_URI = os.getenv("MONGO_URI")
TOTAL_RETRY_REQUEST = os.getenv("TOTAL_RETRY_REQUEST")
FORCELIST = os.getenv("FORCELIST")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_NEWS_COLLECTION = os.getenv("MONGO_NEWS_COLLECTION")
