import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TEST_CHANNEL_ID = os.getenv('TEST_CHANNEL_ID')