import json
import os

from src.utils import utils

script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, '../config/behavior.json')

with open(abs_file_path) as f:
    messages = json.load(f)
    for message in messages:
        message['content'] = utils.append_json_data_on_message(message['content'])

class SessionManager:
    __instance = None
    @staticmethod
    def getInstance():
        if SessionManager.__instance == None:
            SessionManager()
        return SessionManager.__instance
    def __init__(self):
        if SessionManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SessionManager.__instance = self
            self.history = {}

    def add_message(self, user_id, role, content):
        message = {"role": role, "content": content}
        if user_id not in self.history:
            self.history[user_id] = messages
        self.history[user_id].append(message)

    def clean_history(self, user_id):
        if user_id in self.history:
            self.history[user_id] = []

    def get_history(self, user_id):
        if user_id not in self.history:
            return []
        return self.history[user_id]

