import openai
import os


class ChatGPT:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.engine = "gpt-3.5-turbo"

    def ask(self, question):
        prompt = {
            "role": "user",
            "content": question
        }
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[prompt],
        )
        message = response["choices"][0]["message"]["content"]
        return message.strip()

