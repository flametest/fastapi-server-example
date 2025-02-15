from dataclasses import dataclass
from typing import Optional
from pydantic import validator, field_validator
from datetime import datetime


@dataclass
class Company:
    id: int
    name: str
    address: Optional[str] = None

    @field_validator('name')
    def validate_name(self, v):
        if len(v.strip()) == 0:
            raise ValueError('公司名称不能为空')
        return v

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True
