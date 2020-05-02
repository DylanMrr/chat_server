import tornado.websocket


class OnlineUserData:
    def __init__(self, id: str):
        self.id = id
        self.socket = None


class OnlineUsersService:
    def __init__(self):
        self.__users_online = dict()

    def add_user_online(self, jwt: str, id: str):
        self.__users_online[jwt] = OnlineUserData(id)
        #self.__users_online[jwt] = id

    def get_user_id(self, jwt: str):
        return self.__users_online[jwt].id if jwt in self.__users_online.keys() else -1

    def delete_user_online(self):
        pass

    def init_user(self, jwt: str, socket: tornado.websocket.WebSocketHandler):
        self.__users_online[jwt].socket = socket

    def is_user_online(self, id):
        for v in self.__users_online.values():
            if v.id == id:
                return True
        return False

    def get_socket(self, id) -> tornado.websocket.WebSocketHandler:
        for v in self.__users_online:
            if self.__users_online[v].id == id:
                return self.__users_online[v].socket
        return None
