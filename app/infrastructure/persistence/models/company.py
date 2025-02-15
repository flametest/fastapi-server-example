from sqlalchemy import Column, Integer, String
from app.db.session import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    address = Column(String(255), nullable=True)