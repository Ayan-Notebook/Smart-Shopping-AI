# agents/session_agent.py
class SessionAgent:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user_id):
        self.sessions[user_id] = {"history": []}

    def update_session(self, user_id, message):
        if user_id in self.sessions:
            self.sessions[user_id]["history"].append(message)
