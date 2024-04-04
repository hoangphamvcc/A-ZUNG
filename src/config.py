import os
from dotenv import load_dotenv

load_dotenv()

VNEXPRESS_URL = os.getenv("VNEXPRESS_URL")
MONGO_URI = os.getenv("MONGO_URI")

