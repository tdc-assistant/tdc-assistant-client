from .base import Base
from .message_role import MessageRole
from .annotation import Annotation


class ImageCapture(Base):
    image_url: str
