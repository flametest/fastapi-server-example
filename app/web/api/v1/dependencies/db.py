from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db.session import get_db

DB = Annotated[AsyncSession, Depends(get_db)]
