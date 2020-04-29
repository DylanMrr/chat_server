from messages.base_message import BaseMessage
import json


class ConfirmContactMessage(BaseMessage):
    requested_id: str
    answer: int

    def __init__(self, requested_id: str, answer: int):
        self.requested_id = requested_id
        self.answer = answer

    def serialize(self) -> dict:
        return json.dumps({
            'requested_id': self.requested_id,
            'answer': self.answer
        })

    @staticmethod
    def deserialize(message: str):
        source_dict = json.loads(message)
        return ConfirmContactMessage(
            requested_id=source_dict['requested_id'],
            answer=source_dict['answer']
        )