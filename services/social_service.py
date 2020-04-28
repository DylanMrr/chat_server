from services.online_users_service import OnlineUsersService


class SocialService:
    def __init__(self, online_users_service: OnlineUsersService):
        self._online_users_service = online_users_service

    def get_user_id(self, jwt: str):
        return self._online_users_service.get_user_id(jwt)

    def add_contact(self, self_id, request_id):
        pass
