#generates a singleton

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
            self.history[user_id] = []
        self.history[user_id].append(message)

    def clean_history(self, user_id):
        if user_id in self.history:
            self.history[user_id] = []

    def get_history(self, user_id):
        if user_id not in self.history:
            return []
        return self.history[user_id]

