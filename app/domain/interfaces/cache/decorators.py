from functools import wraps
from typing import Any, Callable
from app.domain.interfaces.cache.provider import CacheProvider


def cached(ttl: int = 300):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(self, *args, **kwargs) -> Any:
            if not hasattr(self, 'cache_provider'):
                return await func(self, *args, **kwargs)

            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached_value = await self.cache_provider.get(cache_key)

            if cached_value is not None:
                return cached_value

            result = await func(self, *args, **kwargs)
            await self.cache_provider.set(cache_key, result, ttl)
            return result

        return wrapper

    return decorator
