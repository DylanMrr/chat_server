import tornado.web
from messages.login_message import LoginMessage
from services.login_service import LoginService
import json


class LoginHandler(tornado.web.RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def initialize(self, login_service: LoginService) -> None:
        self._login_service = login_service

    def post(self):
        message = LoginMessage.deserialize(self.request.body.decode('utf-8'))
        result = self._login_service.login(message)
        self.set_header("Content-Type", "application/json")
        self.write(result)
        self.finish()

    def get(self):
        pass
