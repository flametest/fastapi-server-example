from typing import Dict, List, Type, Callable
import asyncio
from app.domain.events.user_events import UserCreatedEvent, UserCompanyChangedEvent


class EventBus:
    def __init__(self):
        self._handlers: Dict[Type, List[Callable]] = {}
        self._async_handlers: Dict[Type, List[Callable]] = {}

    def register(self, event_type: Type, handler: Callable):
        """注册同步事件处理器"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def register_async(self, event_type: Type, handler: Callable):
        """注册异步事件处理器"""
        if event_type not in self._async_handlers:
            self._async_handlers[event_type] = []
        self._async_handlers[event_type].append(handler)

    def publish(self, event):
        """同步发布事件"""
        event_type = type(event)
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                handler(event)

    async def publish_async(self, event):
        """异步发布事件"""
        event_type = type(event)
        # 处理同步处理器
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                handler(event)

        # 处理异步处理器
        if event_type in self._async_handlers:
            await asyncio.gather(
                *[handler(event) for handler in self._async_handlers[event_type]]
            )
