class OnlineUsersService:
    def __init__(self):
        self.__users_online = dict()

    def add_user_online(self, jwt: str, id: str):
        self.__users_online[jwt] = id

    def get_user_id(self, jwt: str):
        return self.__users_online[jwt] if jwt in self.__users_online.keys() else -1

    def delete_user_online(self):
        pass
