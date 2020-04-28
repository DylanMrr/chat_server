import tornado.web
from messages.add_contact_message import AddContactMessage


class AddContactHandler(tornado.web.RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def initialize(self, social_service) -> None:
        self._social_service = social_service

    def post(self):
        message = AddContactMessage.deserialize(self.request.body.decode('utf-8'))
        #todo проверить jwt
        self_id = self._social_service(message.jwt)
        result = self._social_service.register(self_id, message.request_id)
        self.set_header("Content-Type", "application/json")
        self.write(result)
        self.finish()
