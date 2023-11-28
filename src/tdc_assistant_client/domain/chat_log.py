from .base import Base
from .chat_completion import ChatCompletion
from .message import Message
from .workspace import Workspace
from .image_capture import ImageCapture


class ChatLog(Base):
    customerName: str
    rawText: str
    messages: list[Message]
    workspaces: list[Workspace]
    chatCompletions: list[ChatCompletion]
    imageCaptures: list[ImageCapture]
