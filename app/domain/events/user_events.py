from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserCreatedEvent:
    user_id: int
    username: str
    company_id: int
    email: str
    created_at: datetime = datetime.now()
