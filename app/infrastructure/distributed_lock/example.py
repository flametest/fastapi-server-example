from datetime import timedelta
from app.infrastructure.distributed_lock.lock_factory import DistributedLockFactory

# 创建锁实例
lock = DistributedLockFactory.create("redis")

# 使用示例
async def example_with_lock():
    try:
        if await lock.acquire("my-resource", timeout=timedelta(seconds=10)):
            # 执行需要加锁的操作
            print("获取锁成功，执行业务逻辑")
    finally:
        await lock.release("my-resource")

# 使用 async with 的方式
async def example_with_context():
    async with lock:
        if await lock.acquire("my-resource", timeout=timedelta(seconds=10)):
            print("获取锁成功，执行业务逻辑")