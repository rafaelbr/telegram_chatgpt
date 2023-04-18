import configparser
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from chatgpt import ChatGPT

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# read config ini
config = configparser.ConfigParser()
config.read('../config/config.ini')

CHAT_GPT_KEY = config['ChatGPT']['api_key']
TELEGRAM_TOKEN = config['Telegram']['token']

chatgpt = ChatGPT(CHAT_GPT_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o ChatGPT!")


async def receive_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.debug(f"Received message from {update.effective_chat.id}: {update.message.text}")
    logging.info(f"Asking ChatGPT....")
    response = chatgpt.ask(update.message.text, update.effective_chat.id)
    logging.debug(f"ChatGPT response: {response}")
    logging.info(f"ChatGPT response completed!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), receive_text)
    application.add_handler(start_handler)
    application.add_handler(message_handler)

    application.run_polling()




