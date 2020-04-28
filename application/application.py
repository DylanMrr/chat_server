from tornado.web import Application


class Application(Application):
    def __init__(self):
        self.websocket_pool = []

