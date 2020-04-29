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

    def get_all_contact(self, jwt: str):
        self_id = self._online_users_service.get_user_id(jwt)
        if self_id == -1:
            print("There is no id")
        contacts = self._database_service.get_contacts(self_id)
        requested_contacts = self._database_service.get_requested_contacts(self_id)
        not_confirmed_contacts = self._database_service.get_not_confirmed_contact(self_id)
        return contacts, requested_contacts, not_confirmed_contacts

