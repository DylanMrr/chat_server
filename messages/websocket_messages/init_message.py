import json


class InitMessage:
    type = "init"
    jwt: str

    def __init__(self, jwt: str):
        self.jwt = jwt
        self.type = "init"

    def serialize(self) -> dict:
        return json.dumps({
            'jwt': self.jwt,
            'type': self.type
        })

    @staticmethod
    def deserialize(message: str):
        source_dict = json.loads(message)
        return InitMessage(
            jwt=source_dict['jwt'],
        )