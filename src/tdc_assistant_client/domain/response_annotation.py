from typing import Literal
from .base import Base


class ResponseAnnotation(Base):
    type: Literal["RESPONSE"]
    content: str
