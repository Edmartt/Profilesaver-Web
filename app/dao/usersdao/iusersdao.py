from abc import ABC, abstractmethod
from app.users import User
from app.querymanager import QueryManager


class IUsersdao(ABC):

    @abstractmethod
    def get(self, user: User, db: QueryManager) -> dict:
        pass

    @abstractmethod
    def add(self, user: User, db: QueryManager) -> None:
        pass

    @abstractmethod
    def check_user_exists(self, user: User, db: QueryManager) -> bool:
        pass
