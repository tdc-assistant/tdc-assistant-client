from typing import Literal
from .base import Base


class CodeEditor(Base):
    type: Literal["CODE_EDITOR"]
    chat_log_id: str
    programming_language: str
    editor_number: int
    content: str
