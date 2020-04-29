import tornado.web
from services.social_service import SocialService


class GetAllContactsHandler(tornado.web.RequestHandler):
    def prepare(self):
        header = "Content-Type"
        body = "application/json"
        self.set_header(header, body)

    def initialize(self, social_service: SocialService) -> None:
        self._social_service = social_service

    def get(self):
        jwt = self.request.headers['jwt']
        contacts, req_contacts, not_confirmed_contacts = self._social_service.get_all_contact(jwt)
        self.set_header("Content-Type", "application/json")
        self.write({"contacts": contacts, "requested_contacts": req_contacts, "not_confirmed_contacts": not_confirmed_contacts})
        self.finish()
