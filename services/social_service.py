from services.online_users_service import OnlineUsersService
from database.database_service import DatabaseService


class SocialService:
    def __init__(self, online_users_service: OnlineUsersService, database_service: DatabaseService):
        self._online_users_service = online_users_service
        self._database_service = database_service

    def get_user_id(self, jwt: str):
        return self._online_users_service.get_user_id(jwt)

    def add_contact(self, self_id, request_id):
        self._database_service.add_not_confirmed_contact(self_id, request_id) # Добавляем в неподтвержденные
        self._database_service.add_contact_request(self_id, request_id) #Добавляем в запрос

