import asyncio

import tornado.httpserver
import tornado.web
import tornado.ioloop

from handlers.login_handler import LoginHandler
from handlers.register_handler import RegisterHandler
from handlers.add_contact_handler import AddContactHandler
from handlers.get_all_contacts_handler import GetAllContactsHandler
from handlers.confirm_contact_handler import ConfirmContactHandler
from handlers.chat_handler import ChatHandler

from database.database_service import DatabaseService

from services.register_service import RegisterService
from services.login_service import LoginService
from services.social_service import SocialService
from services.online_users_service import OnlineUsersService
from services.websocket_service import WebSocketService


def main():
    client = DatabaseService()
    online_users_service = OnlineUsersService()
    websocket_service = WebSocketService(online_users_service, client)
    register_service = RegisterService(client)
    login_service = LoginService(client, online_users_service)
    social_service = SocialService(online_users_service, client)

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    application = tornado.web.Application([
        (r"/login", LoginHandler, dict(login_service=login_service)),
        (r"/register", RegisterHandler, dict(register_service=register_service)),
        (r"/add_contact", AddContactHandler, dict(social_service=social_service)),
        (r"/get_all_contacts", GetAllContactsHandler, dict(social_service=social_service)),
        (r"/confirm_contact", ConfirmContactHandler, dict(social_service=social_service)),
        (r"/chat", ChatHandler, {'social_service': social_service, 'websocket_service': websocket_service})
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
