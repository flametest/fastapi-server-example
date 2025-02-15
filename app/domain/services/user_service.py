from app.domain.aggregates.user import UserAggregate
from app.domain.value_objects.email import Email
from app.domain.services.base_service import BaseDomainService


class UserService(BaseDomainService):
    @staticmethod
    def validate_user_registration(self, email: str, username: str) -> bool:
        if len(username) < 3:
            raise ValueError("用户名长度必须大于3个字符")
        if not Email._is_valid_email(email):
            raise ValueError("邮箱格式不正确")
        return True

    def create_user_aggregate(self, user_data: dict) -> UserAggregate:
        pass
