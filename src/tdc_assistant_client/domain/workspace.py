from typing import Optional, Literal
from .base import Base


WorkspaceType = Literal["WHITEBOARD", "TEXT_EDITOR", "CODE_EDITOR"]


class Workspace(Base):
    chatLogId: str
    boardNumber: int
    type: Optional[WorkspaceType]
    content: str
