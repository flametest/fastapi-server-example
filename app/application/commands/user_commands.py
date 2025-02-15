from pydantic import BaseModel


class CreateUserCommand(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    company_id: int


class UpdateUserCommand(BaseModel):
    user_id: int
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    company_id: int | None = None


class ChangeUserCompanyCommand(BaseModel):
    user_id: int
    new_company_id: int
