import configparser
import logging
import os

from services.chatgpt import ChatGPT
from services.telegram_helper import TelegramHelper

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# read config ini
script_dir = os.path.dirname(__file__)
config = configparser.ConfigParser()
config_file_path = os.path.join(script_dir, 'config/config.ini')
config.read(config_file_path)

CHAT_GPT_KEY = config['ChatGPT']['api_key']
CHAT_GPT_MODEL = config['ChatGPT']['model']
TELEGRAM_TOKEN = config['Telegram']['token']

chatgpt = ChatGPT(CHAT_GPT_KEY, CHAT_GPT_MODEL)
telegram_helper = TelegramHelper(TELEGRAM_TOKEN, chatgpt)



if __name__ == '__main__':
    telegram_helper.run()

