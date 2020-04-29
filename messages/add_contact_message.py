from messages.base_message import BaseMessage
import json


class AddContactMessage(BaseMessage):
    request_id: str

    def __init__(self, request_id: str):
        self.request_id = request_id

    def serialize(self) -> dict:
        return json.dumps({
            'request_id': self.request_id
        })

    @staticmethod
    def deserialize(message: str):
        source_dict = json.loads(message)
        return AddContactMessage(
            request_id=source_dict['request_id']
        )