from abc import ABC, abstractmethod
from app.websites import Website


class IWebsitesdao(ABC):

    @abstractmethod
    def get(self, web_id: int) -> dict:
        pass

    @abstractmethod
    def get_all(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def add(self, web: Website) -> None:
        pass

    @abstractmethod
    def update(self, web: Website, id: int) -> None:
        pass

    @abstractmethod
    def delete(self, web_id: int):
        pass
