from messages.base_message import BaseMessage
import json


class AddContactMessage(BaseMessage):
    jwt: str
    request_id: str

    def __init__(self, jwt: str, request_id: str):
        self.jwt = jwt
        self.request_id = request_id

    def serialize(self) -> dict:
        return json.dumps({
            'login': self.jwt,
            'password': self.request_id
        })

    @staticmethod
    def deserialize(message: str):
        source_dict = json.loads(message)
        return AddContactMessage(
            login=source_dict['jwt'],
            password=source_dict['request_id']
        )