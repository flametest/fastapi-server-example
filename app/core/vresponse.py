from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class VResponse(BaseModel, Generic[T]):
    code: int
    data: T | None = None
    message: str | None = None

    @classmethod
    def ok(
        cls, data: T | None, code: int = 200, message: str = "success"
    ) -> "VResponse[T]":
        return cls(code=code, data=data, message=message)

    @classmethod
    def fail(cls, code: int, message: str) -> "VResponse[T]":
        return cls(code=code, message=message)
