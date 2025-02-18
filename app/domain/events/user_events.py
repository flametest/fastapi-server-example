from uuid import uuid4
from .base import DomainEvent


class UserCreatedEvent(DomainEvent):
    user_id: int
    company_id: int

    def __init__(self, **data):
        super().__init__(
            event_id=str(uuid4()),
            event_type="user.created",
            **data
        )


class UserCompanyChangedEvent(DomainEvent):
    user_id: int
    old_company_id: int
    new_company_id: int

    def __init__(self, **data):
        super().__init__(
            event_id=str(uuid4()),
            event_type="user.company_changed",
            **data
        )