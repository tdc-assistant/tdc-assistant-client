from typing import TypedDict
from datetime import datetime


class Base(TypedDict):
    id: str
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime
