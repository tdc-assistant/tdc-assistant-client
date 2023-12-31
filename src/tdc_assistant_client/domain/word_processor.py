from typing import Literal
from .base import Base


class WordProcessor(Base):
    type: Literal["WORD_PROCESSOR"]
    chatLogId: str
    number: int
    content: str
