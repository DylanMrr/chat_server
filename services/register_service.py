from database.database_service import DatabaseService
from messages.register_message import RegisterMessage
from common_types.enumerations import RegisterResults
from services import jwt_service
import json


class RegisterService:
    def __init__(self, database_service: DatabaseService):
        self._database_service = database_service

    def register(self, message: RegisterMessage):
        db_result, id = self._database_service.register(message.login, message.password)
        if db_result == RegisterResults.success:
            jwt = jwt_service.create_jwt(id)
            response = dict({"result": "success", "jwt": str(jwt)})
        elif db_result == RegisterResults.login_busy or db_result == RegisterResults.not_validated or db_result == RegisterResults.server_error:
            response = dict({"result": "failed"})
        return response

