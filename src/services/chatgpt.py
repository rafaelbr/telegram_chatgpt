import openai
import os
import json

from src.utils.session_manager import SessionManager


class ChatGPT:
    def __init__(self, api_key, model):
        self.api_key = api_key
        openai.api_key = api_key
        self.model = model

    def ask(self, user_id):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=SessionManager.getInstance().get_history(user_id),
        )
        message = response["choices"][0]["message"]["content"]
        return message.strip()

