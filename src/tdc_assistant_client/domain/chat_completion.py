from .base import Base
from .chat_completion_part import ChatCompletionPart
from .chat_completion_approval_status import *


class ChatCompletion(Base):
    content: str
    approvalStatus: ChatCompletionApprovalStatus
    parts: list[ChatCompletionPart]
