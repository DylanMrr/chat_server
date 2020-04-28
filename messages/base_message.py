from abc import abstractmethod
import json


class BaseMessage:
    @abstractmethod
    def serialize(self) -> str:
        pass
