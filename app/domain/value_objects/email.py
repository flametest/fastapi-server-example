from dataclasses import dataclass
import re

from pydantic import field_validator


@dataclass(frozen=True)
class Email:
    value: str

    @classmethod
    @field_validator("value")
    def validate_email(cls, v):
        if not cls._is_valid_email(v):
            raise ValueError("Invalid email format")

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
