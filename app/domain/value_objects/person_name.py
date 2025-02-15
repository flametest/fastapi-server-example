from dataclasses import dataclass

from pydantic import validator, field_validator


@dataclass(frozen=True)
class PersonName:
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def name_not_empty(self, v):
        if not v.strip():
            raise ValueError('姓名不能为空')
        return v.strip()

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
