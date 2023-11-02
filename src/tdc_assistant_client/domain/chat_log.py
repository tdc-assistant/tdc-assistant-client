from .base import Base
from .message import Message
from .workspace import Workspace


class ChatLog(Base):
    customerName: str
    messages: list[Message]
    workspaces: list[Workspace]
