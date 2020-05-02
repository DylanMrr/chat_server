from messages.websocket_messages.init_message import InitMessage
from services.online_users_service import OnlineUsersService
from database.database_service import DatabaseService
import tornado.websocket


class WebSocketService:
    def init_handler(self, message: str, socket: tornado.websocket.WebSocketHandler):
        deserialized_message = InitMessage.deserialize(message)
        #todo делать, проверку, что он залогинен
        self._online_user_service.init_user(deserialized_message.jwt, socket)
        unsended_messages = str(self._database_service.get_unsended_messages(
                self._online_user_service.get_user_id(deserialized_message.jwt)))
        socket.write_message(
            '{"type": "init", "unsended_messages": %s}' % (unsended_messages))

    def __init__(self, online_user_service: OnlineUsersService, database_service: DatabaseService):
        self._online_user_service = online_user_service
        self._database_service = database_service
        self.handlers = {
            'init': self.init_handler
        }
