from typing import Union

from .code_editor import CodeEditor
from .word_processor import WordProcessor


Workspace = Union[CodeEditor, WordProcessor]
