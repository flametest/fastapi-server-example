from typing import Any, Optional, Dict
import time
from app.domain.interfaces.cache.provider import CacheProvider

class MemoryProvider(CacheProvider):
    def __init__(self):
        self._cache: Dict[str, tuple[Any, float | None]] = {}

    async def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
            
        value, expiry = self._cache[key]
        if expiry and time.time() > expiry:
            await self.delete(key)
            return None
            
        return value

    async def set(self, key: str, value: Any, ttl: int = None) -> None:
        expiry = time.time() + ttl if ttl else None
        self._cache[key] = (value, expiry)

    async def delete(self, key: str) -> None:
        self._cache.pop(key, None)