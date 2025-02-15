import json
from typing import Any, Callable
import aioredis
from app.domain.interfaces.message_queue import MessageQueue


class RedisMessageQueue(MessageQueue):
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.redis: aioredis.Redis = None
        self.pubsub = None

    async def connect(self):
        if not self.redis:
            self.redis = await aioredis.from_url(self.redis_url)
            self.pubsub = self.redis.pubsub()

    async def publish(self, topic: str, message: Any) -> None:
        await self.connect()
        message_str = json.dumps(message)
        await self.redis.publish(topic, message_str)

    async def subscribe(self, topic: str, callback: Callable) -> None:
        await self.connect()
        await self.pubsub.subscribe(topic)

        while True:
            try:
                message = await self.pubsub.get_message(ignore_subscribe_messages=True)
                if message:
                    data = json.loads(message['data'])
                    await callback(data)
            except Exception as e:
                print(f"Error processing message: {e}")

    async def close(self) -> None:
        if self.pubsub:
            await self.pubsub.close()
        if self.redis:
            await self.redis.close()
