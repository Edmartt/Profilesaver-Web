from abc import ABC, abstractmethod
from app.users import User


class IUsersdao(ABC):

    @abstractmethod
    def get(self, user: User) -> dict:
        pass

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def check_user_exists(self, user: User) -> bool:
        pass
