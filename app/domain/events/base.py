from datetime import datetime
from pydantic import BaseModel


class DomainEvent(BaseModel):
    event_id: str
    occurred_on: datetime = datetime.now()
    event_type: str