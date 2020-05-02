from messages.websocket_messages.init_message import InitMessage
from messages.websocket_messages.send_message_to_server import SendMessageToServer
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
            '{"type": "init", "unsended_messages": %s}' % (unsended_messages)
        )
        # Удаление из БД
        self._database_service.delete_unsended_messages(self._online_user_service.get_user_id(deserialized_message.jwt))

    #TODO ЕСЛИ БУДУТ ОШИБКИ В ДЕСЕРИАЛИЗЦИИ - ЗАМЕНИТЬ КАВЫЧКИ
    def message_to_server_handler(self, message: str, socket: tornado.websocket.WebSocketHandler):
        deserialized_message = SendMessageToServer.deserialize(message)
        receiver = deserialized_message.receiver
        # Receiver онлайн
        if self._online_user_service.is_user_online(deserialized_message.receiver):
            receiver_socket = self._online_user_service.get_socket(
                deserialized_message.receiver)
            receiver_socket.write_message(
                '{"type": "to_client", "message": %s, "sender": %s}' %
                (deserialized_message.message, self._online_user_service.get_user_id(deserialized_message.jwt))
            )
        # Receiver not online
        else:
            self._database_service.add_unsended_message(receiver,
                                                        self._online_user_service.get_user_id(deserialized_message.jwt),
                                                        deserialized_message.message)

    def __init__(self, online_user_service: OnlineUsersService, database_service: DatabaseService):
        self._online_user_service = online_user_service
        self._database_service = database_service
        self.handlers = {
            'init': self.init_handler,
            'to_server': self.message_to_server_handler
        }
