from typing import Literal
from .base import Base


class WordProcessor(Base):
    type: Literal["WORD_PROCESSOR"]
    chat_log_id: str
    number: int
    content: str
