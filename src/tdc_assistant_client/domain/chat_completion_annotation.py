from typing import Literal, Optional
from datetime import datetime
from .base import Base
from .chat_completion import ChatCompletion


ChatCompletionAnnotationApprovalStatus = Literal["APPROVED", "DECLINED"]


class ChatCompletionAnnotation(Base):
    type: Literal["CHAT_COMPLETION"]
    messageId: str
    approvalStatus: Optional[ChatCompletionAnnotationApprovalStatus]
    responseAnnotationId: Optional[str]
    chatCompletion: Optional[ChatCompletion]
    sentAt: datetime
