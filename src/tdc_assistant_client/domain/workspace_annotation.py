from typing import Literal
from .base import Base


class WorkspaceAnnotation(Base):
    type: Literal["WORKSPACE"]
    content: str
    board_number: int
