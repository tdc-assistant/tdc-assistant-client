from .base import Base
from .message_role import MessageRole
from .annotation import Annotation


class Message(Base):
    chatLogId: str
    content: str
    role: MessageRole
    annotations: list[Annotation]
    is_awaiting_chat_completion: bool
