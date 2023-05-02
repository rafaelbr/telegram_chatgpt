
#Telegram Helper
#Receive a Telegram Token and create a Telegram Bot

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from src.utils.session_manager import SessionManager


class TelegramHelper:
    def __init__(self, token, chatgpt):
        self.application = ApplicationBuilder().token(token).build()
        self.chat = chatgpt

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        SessionManager.getInstance().add_message(update.effective_chat.id, "user", "Quem é você?")
        response = self.chat.ask(update.effective_chat.id)
        SessionManager.getInstance().add_message(update.effective_chat.id, "assistant", response)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    async def receive_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logging.debug(f"Received message from {update.effective_chat.id}: {update.message.text}")
        SessionManager.getInstance().add_message(update.effective_chat.id, "user", update.message.text)
        logging.info(f"Asking ChatGPT....")
        response = self.chat.ask(update.effective_chat.id)
        logging.debug(f"ChatGPT response: {response}")
        logging.info(f"ChatGPT response completed!")
        SessionManager.getInstance().add_message(update.effective_chat.id, "assistant", response)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    def run(self):
        start_handler = CommandHandler('start', self.start)
        message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), self.receive_text)
        self.application.add_handler(start_handler)
        self.application.add_handler(message_handler)

        self.application.run_polling()
