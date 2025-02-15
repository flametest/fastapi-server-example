from app.domain.interfaces.distributed_lock import DistributedLock
from app.infrastructure.distributed_lock.redis_lock import RedisLock


class DistributedLockFactory:
    @staticmethod
    def create(lock_type: str = "redis", **kwargs) -> DistributedLock:
        if lock_type == "redis":
            return RedisLock(**kwargs)
        raise ValueError(f"Unsupported lock type: {lock_type}")