import asyncio

import tornado.httpserver
import tornado.web
import tornado.ioloop

from handlers.login_handler import LoginHandler
from handlers.register_handler import RegisterHandler

from database.database_service import DatabaseService

from services.register_service import RegisterService
from services.login_service import LoginService


def main():
    client = DatabaseService()
    register_service = RegisterService(client)
    login_service = LoginService(client)

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    application = tornado.web.Application([
        (r"/login", LoginHandler, dict(login_service=login_service)),
        (r"/register", RegisterHandler, dict(register_service=register_service))
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
