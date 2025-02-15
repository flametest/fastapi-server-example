from typing import Any, Optional
import aioredis
from app.domain.interfaces.cache.provider import CacheProvider
import json

class RedisProvider(CacheProvider):
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = aioredis.from_url(redis_url)

    async def get(self, key: str) -> Optional[Any]:
        value = await self.redis.get(key)
        if value:
            return json.loads(value)
        return None

    async def set(self, key: str, value: Any, ttl: int = None) -> None:
        value_str = json.dumps(value)
        if ttl:
            await self.redis.setex(key, ttl, value_str)
        else:
            await self.redis.set(key, value_str)

    async def delete(self, key: str) -> None:
        await self.redis.delete(key)