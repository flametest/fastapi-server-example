from abc import ABC, abstractmethod
from http import HTTPStatus


class BaseApplicationError(Exception, ABC):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    @abstractmethod
    def http_code(self) -> int:
        return HTTPStatus.INTERNAL_SERVER_ERROR


class NotFoundError(BaseApplicationError):
    def http_code(self) -> int:
        return HTTPStatus.NOT_FOUND


class ForbiddenError(BaseApplicationError):
    def http_code(self) -> int:
        return HTTPStatus.FORBIDDEN


class UnauthorizedError(BaseApplicationError):
    def http_code(self) -> int:
        return HTTPStatus.UNAUTHORIZED


class BadRequestError(BaseApplicationError):
    def http_code(self) -> int:
        return HTTPStatus.BAD_REQUEST
