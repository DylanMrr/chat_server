import tornado.web
from messages.register_message import RegisterMessage
from services.register_service import RegisterService
import json


class RegisterHandler(tornado.web.RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def initialize(self, register_service) -> None:
        self._register_service = register_service

    def post(self):
        message = RegisterMessage.deserialize(self.request.body.decode('utf-8'))
        result = self._register_service.register(message)
        self.set_header("Content-Type", "application/json")
        self.write(result)
        self.finish()

    def get(self):
        pass
