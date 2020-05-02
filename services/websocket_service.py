from messages.websocket_messages.init_message import  InitMessage
from services.online_users_service import OnlineUsersService
import tornado.websocket


class WebSocketService:

    #@staticmethod
    def init_handler(self, message: str, socket: tornado.websocket.WebSocketHandler):
        deserialized_message = InitMessage.deserialize(message)
        self._online_user_service.init_user(deserialized_message.jwt, socket)

    def __init__(self, online_user_service: OnlineUsersService):
        self._online_user_service = online_user_service
        self.handlers = {
            'init': self.init_handler
        }
