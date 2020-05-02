import json


class SendMessageToServer:
    type = "to_server"
    jwt: str
    receiver: str
    message: str

    def __init__(self, jwt: str, receiver: str, message: str):
        self.jwt = jwt
        self.receiver = receiver
        self.type = "to_server"
        self.message = message

    def serialize(self) -> dict:
        return json.dumps({
            'jwt': self.jwt,
            'type': self.type,
            'receiver': self.receiver,
            'message': self.message
        })

    @staticmethod
    def deserialize(message: str):
        source_dict = json.loads(message)
        return SendMessageToServer(
            jwt=source_dict['jwt'],
            receiver=source_dict['receiver'],
            message=source_dict['message']
        )