from abc import ABC, abstractmethod
from typing import Optional
from datetime import timedelta


class DistributedLock(ABC):
    @abstractmethod
    async def acquire(self, key: str, timeout: Optional[timedelta] = None) -> bool:
        pass

    @abstractmethod
    async def release(self, key: str) -> bool:
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.release()