from .base import Base
from .image_capture_type import ImageCaptureType


class ImageCapture(Base):
    chatLogId: str
    type: ImageCaptureType
    imageUrl: str
