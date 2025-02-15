# 在应用启动时初始化消息队列
message_queue = MessageQueueFactory.create(
    queue_type="redis", 
    redis_url="redis://localhost:6379"
)

# 发布消息
await message_queue.publish("user_created", {"user_id": "123", "username": "test"})

# 订阅消息
async def handle_user_created(message):
    print(f"New user created: {message}")

await message_queue.subscribe("user_created", handle_user_created)