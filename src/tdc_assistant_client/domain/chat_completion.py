from .base import Base
from .chat_completion_part import ChatCompletionPart


class ChatCompletion(Base):
    sentAt: str
    content: str
    parts: list[ChatCompletionPart]
