from typing import Optional
from pydantic import field_validator, BaseModel
from datetime import datetime


class Company(BaseModel):
    id: int
    name: str
    address: Optional[str] = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @classmethod
    @field_validator("name")
    def validate_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError('公司名称不能为空')
        return v

    class Config:
        from_attributes = True
