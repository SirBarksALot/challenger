from uuid import uuid4
from time import time, ctime
from etwas import connection


class Log:
    def __init__(self, content):
        self.uuid = uuid4()
        self.timestamp = ctime(time())
        self.content = content


class Challengelog(Log):
    def __init__(self, **challenge_content):
        super().__init__(challenge_content)
        self.questions = self.content.get('questions', '')
        self.answers = self.content.get('answers', '')
        assert len(self.questions) == len(self.answers), 'Not equal amount of Qs and As!'
        self.data = {
            "q_requested": self.content.get('q_requested', 0),
            "q_provided": self.content.get('q_provided', 0),
            "category": self.content.get('category', ''),
            "score": self.content.get('score', 0),
            "q&a": dict(zip(self.questions, self.answers)),
            "log_date": self.timestamp
        }

    def insert_to_db(self):
        return connection('challenges').insert_one(self.data).inserted_id
