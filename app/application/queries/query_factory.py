from app.application.queries.user_queries import UserQueries
from app.infrastructure.repository.user_repository import UserRepository


class QueryFactory:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user_queries(self) -> UserQueries:
        return UserQueries(self.user_repository)
