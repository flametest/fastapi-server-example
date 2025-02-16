from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import DatabaseSession

DB = Annotated[Session, Depends(DatabaseSession.get_session)]
