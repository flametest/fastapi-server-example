from abc import ABC, abstractmethod
from typing import Any, Callable

class MessageQueue(ABC):
    @abstractmethod
    async def publish(self, topic: str, message: Any) -> None:
        pass

    @abstractmethod
    async def subscribe(self, topic: str, callback: Callable) -> None:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass