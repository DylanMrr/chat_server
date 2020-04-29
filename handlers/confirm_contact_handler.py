import tornado.web
from messages.confirm_contact_message import ConfirmContactMessage
from services.social_service import SocialService


class ConfirmContactHandler(tornado.web.RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def initialize(self, social_service: SocialService) -> None:
        self._social_service = social_service

    def post(self):
        message = ConfirmContactMessage.deserialize(self.request.body.decode('utf-8'))
        #todo проверить jwt
        self_id = self._social_service.get_user_id(self.request.headers['jwt'])
        self._social_service.confirm_contact(self_id, message.requested_id, message.answer)
        self.set_header("Content-Type", "application/json")
        self.write({"result": "success"})
        self.finish()

