import openai
import os

from src.session_manager import SessionManager


class ChatGPT:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.engine = "gpt-3.5-turbo"

    def ask(self, question, user_id):
        SessionManager.getInstance().add_message(user_id, "user", question)
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=SessionManager.getInstance().get_history(user_id)
        )
        message = response["choices"][0]["message"]["content"]
        SessionManager.getInstance().add_message(user_id, "assistant", message)
        return message.strip()

