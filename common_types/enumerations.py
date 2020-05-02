from enum import Enum


class RegisterResults(Enum):
    success = 1
    login_busy = 2
    not_validated = 3
    server_error = 4
    default = 5


class LoginResults(Enum):
    success = 1,
    error = 2
    not_validated = 3,
    server_error = 4,
    default = 5


class WebSocketMessageTypes(Enum):
    init = 1
