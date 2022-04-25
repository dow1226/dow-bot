import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TEST_CHANNEL_ID = os.getenv('TEST_CHANNEL_ID')
URL_PIC = os.getenv('URL_PIC')