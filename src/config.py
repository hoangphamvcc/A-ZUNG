import os
from dotenv import load_dotenv

load_dotenv()

VNEXPRESS_URL = os.getenv("VNEXPRESS_URL")
MONGO_URI = os.getenv("MONGO_URI")
TOTAL_RETRY_REQUEST = os.getenv("TOTAL_RETRY_REQUEST")
FORCELIST = os.getenv("FORCELIST")
