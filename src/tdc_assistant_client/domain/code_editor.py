from typing import Literal
from .base import Base


class CodeEditor(Base):
    type: Literal["CODE_EDITOR"]
    chatLogId: str
    programmingLanguage: str
    editorNumber: int
    content: str
