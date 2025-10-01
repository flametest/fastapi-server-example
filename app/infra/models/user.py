from sqlalchemy import Column, Integer, String

from app.infra.db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    gender = Column(String(10), nullable=True)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
