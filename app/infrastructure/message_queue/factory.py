from typing import Optional
from app.infrastructure.message_queue.interfaces import MessageQueue
from app.infrastructure.message_queue.redis_message_queue import RedisMessageQueue

class MessageQueueFactory:
    _instance: Optional[MessageQueue] = None

    @classmethod
    def create(cls, queue_type: str = "redis", **kwargs) -> MessageQueue:
        if cls._instance is None:
            if queue_type == "redis":
                redis_url = kwargs.get("redis_url", "redis://localhost:6379")
                cls._instance = RedisMessageQueue(redis_url)
            else:
                raise ValueError(f"Unsupported queue type: {queue_type}")
        return cls._instance

    @classmethod
    def get_instance(cls) -> Optional[MessageQueue]:
        return cls._instance