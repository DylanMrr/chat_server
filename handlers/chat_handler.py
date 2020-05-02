import tornado.websocket
from services.social_service import SocialService
from services.websocket_service import WebSocketService
import json


class ChatHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        self._social_service = kwargs.pop('social_service')
        self._websocket_service = kwargs.pop('websocket_service')
        super(ChatHandler, self).__init__(*args, **kwargs)

    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_close(self):
        pass#todo убирать из онлайн

    def on_message(self, message):
        type = json.loads(message)['type']
        self._websocket_service.handlers[type](message, self)
