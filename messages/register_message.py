from messages.base_message import BaseMessage
import json


class RegisterMessage(BaseMessage):
    login: str
    password: str

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def serialize(self) -> dict:
        return json.dumps({
            'login': self.login,
            'password': self.password
        })

    @staticmethod
    def deserialize(message: str):
        source_dict = json.loads(message)
        return RegisterMessage(
            login=source_dict['login'],
            password=source_dict['password']
        )
