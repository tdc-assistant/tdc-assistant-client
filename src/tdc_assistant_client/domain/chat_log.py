from .base import Base
from .chat_completion import ChatCompletion
from .message import Message
from .workspace import Workspace


class ChatLog(Base):
    customerName: str
    rawText: str
    messages: list[Message]
    workspaces: list[Workspace]
    chat_completions: list[ChatCompletion]
