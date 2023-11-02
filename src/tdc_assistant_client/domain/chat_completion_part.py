from typing import Literal
from .base import Base

ChatCompletionPartType = Literal["CONVERSATION", "CODE"]


class ChatCompletionPart(Base):
    content: str
    type: ChatCompletionPartType
    programmingLanguage: str
    shouldOmit: bool
