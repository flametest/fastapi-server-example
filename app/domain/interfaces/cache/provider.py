from typing import Any, Optional
from abc import ABC, abstractmethod


class CacheProvider(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        pass

    @abstractmethod
    async def set(self, key: str, value: Any, ttl: int = None) -> None:
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        pass
