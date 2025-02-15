from dataclasses import dataclass
from typing import Optional

from app.domain.entities.company import Company
from app.domain.value_objects.email import Email


@dataclass
class UserAggregate:
    id: int
    username: str
    email: Email
    gender: Optional[str]
    company: Optional[Company] = None

    @classmethod
    def create(cls, username: str, email: str, gender: Optional[str] = None) -> 'UserAggregate':
        return cls(
            id=None,
            username=username,
            email=Email(email),
            gender=gender
        )

    def assign_company(self, company: Company) -> None:
        if self.company is not None:
            raise ValueError("User already has a company")
        self.company = company

    def update_email(self, new_email: str) -> None:
        self.email = Email(new_email)
