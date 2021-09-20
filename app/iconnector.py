from abc import ABC, abstractmethod


class IConnector(ABC):

    @abstractmethod
    def get_db(self):
        pass

    @abstractmethod
    def close_db(self, e=None):
        pass

    @abstractmethod
    def init_db(self):
        pass
