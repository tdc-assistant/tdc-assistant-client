from typing import Union
from .response_annotation import ResponseAnnotation
from .workspace_annotation import WorkspaceAnnotation
from .chat_completion_annotation import ChatCompletionAnnotation
from .image_capture_annotation import ImageCaptureAnnotation


Annotation = Union[
    ResponseAnnotation,
    WorkspaceAnnotation,
    ChatCompletionAnnotation,
    ImageCaptureAnnotation,
]
