from typing import Literal

from .base import Base
from .image_capture import ImageCapture


class ImageCaptureAnnotation(Base):
    type: Literal["IMAGE_CAPTURE"]
    image_capture: ImageCapture
