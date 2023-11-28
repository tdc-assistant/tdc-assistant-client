from typing import Literal
from datetime import datetime

from .base import Base

ChatCompletionPartType = Literal["CONVERSATION", "CODE"]


class ChatCompletionPart(Base):
    sentAt: datetime
    content: str
    type: ChatCompletionPartType
    programmingLanguage: str
    shouldOmit: bool
