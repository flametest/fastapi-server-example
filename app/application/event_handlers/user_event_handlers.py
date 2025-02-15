from ...domain.events.user_events import UserCreatedEvent, UserCompanyChangedEvent
import asyncio


class UserEventHandler:
    def handle_user_created(self, event: UserCreatedEvent):
        """同步处理用户创建事件"""
        print(f"同步处理：新用户已创建: {event.user_id}")

    async def handle_user_created_async(self, event: UserCreatedEvent):
        """异步处理用户创建事件"""
        await asyncio.sleep(1)  # 模拟异步操作
        print(f"异步处理：新用户已创建: {event.user_id}")

    def handle_company_changed(self, event: UserCompanyChangedEvent):
        """同步处理公司变更事件"""
        print(f"同步处理：用户 {event.user_id} 已更换公司")

    async def handle_company_changed_async(self, event: UserCompanyChangedEvent):
        """异步处理公司变更事件"""
        await asyncio.sleep(1)  # 模拟异步操作
        print(f"异步处理：用户 {event.user_id} 已更换公司")
