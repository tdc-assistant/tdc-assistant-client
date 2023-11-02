from typing import Union
from .response_annotation import ResponseAnnotation
from .workspace_annotation import WorkspaceAnnotation
from .chat_completion_annotation import ChatCompletionAnnotation


Annotation = Union[ResponseAnnotation, WorkspaceAnnotation, ChatCompletionAnnotation]
