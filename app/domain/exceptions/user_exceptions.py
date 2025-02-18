from typing import Optional


class UserException(Exception):
    """用户相关异常的基类"""

    def __init__(self, message: str = "用户操作异常"):
        self.message = message
        super().__init__(self.message)


class UserNotFoundError(UserException):
    """用户不存在异常"""

    def __init__(self, user_id: Optional[int] = None, username: Optional[str] = None):
        message = "用户不存在"
        if user_id:
            message = f"ID为 {user_id} 的用户不存在"
        elif username:
            message = f"用户名为 {username} 的用户不存在"
        super().__init__(message)


class UserAlreadyExistsError(UserException):
    """用户已存在异常"""

    def __init__(self, field: str, value: str):
        super().__init__(f"{field} '{value}' 已被注册")


class InvalidPasswordError(UserException):
    """密码无效异常"""

    def __init__(self):
        super().__init__("密码不正确")


class CompanyAlreadyAssignedError(UserException):
    """公司已分配异常"""

    def __init__(self, user_id: int):
        super().__init__(f"用户 {user_id} 已经关联了公司")


class CompanyNotFoundError(UserException):
    """公司不存在异常"""

    def __init__(self, company_id: int):
        super().__init__(f"ID为 {company_id} 的公司不存在")


class InvalidEmailError(UserException):
    """邮箱格式无效异常"""

    def __init__(self, email: str):
        super().__init__(f"邮箱格式无效: {email}")
