from tornado.websocket import WebSocketHandler
import tornado.gen as gen

class MainHandler(WebSocketHandler):
    users_online = {}
    users_not_authorized = []

    #@gen.coroutine
    def open(self):
        MainHandler.users_not_authorized.append(self)

    def on_close(self):
        pass

    