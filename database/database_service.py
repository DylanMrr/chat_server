from pymongo import MongoClient
from bson.objectid import ObjectId
from common_types.enumerations import RegisterResults
from common_types.enumerations import LoginResults


class DatabaseService:
    def __init__(self):
        self.__mongo_client = MongoClient("localhost", 27017)
        self.__db = self.__mongo_client["chat_db"]
        self.__collection = self.__db["chat_db"]
        print(self.__db.name)

    def login(self, login: str, password: str):
        result = LoginResults.default
        id_object = -1
        user_entry = self.__collection.find_one({"login": login, "password": password})
        if user_entry is None:
            result = LoginResults.error
        else:
            result = LoginResults.success
            id_object = user_entry["_id"]
        return result, str(id_object)


    def register(self, login: str, password: str):
        result = RegisterResults.default
        id_object = -1
        user_entry = self.__collection.find_one({"login": login})
        if user_entry is None:
            id_object = self.__collection.insert_one(
                {"login": login, "password": password,
                 "contacts": [], "contacts_requests": [], "not_confirmed_contact": []}).inserted_id
            result = RegisterResults.success
        else:
            result = RegisterResults.login_busy
        return result, str(id_object)

    def add_not_confirmed_contact(self, self_id, request_id):
        # todo возможно косяк, из-за несоответствия типов id. Если так, то руками в бд добавлять id
        self.__collection.update({"_id": ObjectId(self_id)}, {"$push": {"not_confirmed_contact": request_id}})

    def add_contact_request(self, self_id, request_id):
        self.__collection.update({"_id": ObjectId(request_id)}, {"$push": {"contacts_requests": self_id}})
