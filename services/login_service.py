from database.database_service import DatabaseService
from messages.login_message import LoginMessage
from common_types.enumerations import LoginResults
from services import jwt_service
import json

class LoginService:
    def __init__(self, database_service: DatabaseService):
        self._database_service = database_service

    def login(self, message: LoginMessage):
        db_result, id = self._database_service.login(message.login, message.password)
        if db_result == LoginResults.success:
            jwt = jwt_service.create_jwt(id)
            response = dict({"result": "success", "jwt": str(jwt)})
        elif db_result == LoginResults.error or db_result == LoginResults.not_validated or db_result == LoginResults.server_error:
            response = dict({"result": "failed"})
        return response
