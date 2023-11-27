from typing import Any, Optional, Dict, TypedDict, Literal, Union
from typing_extensions import Unpack

import asyncio
from datetime import datetime

from graphql import DocumentNode

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.utilities import update_schema_scalars

from .scalars import DatetimeScalar

from .queries import get_chat_logs_query, get_chat_log_query

from .mutations import (
    create_chat_completion_annotation_mutation,
    create_chat_log_mutation,
    create_message_mutation,
    create_response_annotation_mutation,
    create_workspace_annotation_mutation,
    update_chat_completion_annotation_mutation,
    update_chat_log_mutation,
    create_image_capture_annotation_mutation,
    create_code_editor_mutation,
    update_code_editor_mutation,
    create_word_processor_mutation,
    update_word_processor_mutation,
)

from .domain import (
    ChatLog,
    Message,
    ChatCompletionAnnotation,
    MessageRole,
    CodeEditor,
    WordProcessor,
)


class GetChatLogArgs(TypedDict):
    chat_log_id: str


class CreateChatLogArgs(TypedDict):
    customer_name: str
    raw_text: str
    messages: list[Message]


class CreateChatCompletionAnnotationArgs(TypedDict):
    message: Message


class CreateMessageArgs(TypedDict):
    chat_log_id: str
    content: str
    role: MessageRole


class CreateResponseAnnotationArgs(TypedDict):
    message: Message
    content: str


class CreateWorkspaceAnnotationArgs(TypedDict):
    message: Message
    content: str
    board_number: int


ChatCompletionAnnotationApprovalStatus = Union[Literal["APPROVED"], Literal["DECLINED"]]


class UpdateChatCompletionAnnotation(TypedDict):
    chat_completion_annotation: ChatCompletionAnnotation
    sent_at: Optional[datetime]
    approval_status: Optional[ChatCompletionAnnotationApprovalStatus]


class UpdateChatLog(TypedDict):
    customer_name: str
    raw_text: str
    messages: list[Message]
    shouldClearMessages: bool


class CreateImageCaptureAnnotation(TypedDict):
    message: Message
    image_url: str


class CreateCodeEditor(TypedDict):
    chat_log: ChatLog
    programming_language: str
    editor_number: int
    content: str


class UpdateCodeEditor(TypedDict):
    code_editor: CodeEditor
    content: str


class CreateWordProcessor(TypedDict):
    chat_log: ChatLog
    number: int
    content: str


class UpdateWordProcessor(TypedDict):
    word_processor: WordProcessor
    content: str


class TdcAssistantClient:
    _transport: AIOHTTPTransport

    def __init__(self, url: str):
        self._transport = AIOHTTPTransport(url=url)

    def execute_query(
        self,
        query: DocumentNode,
        key: str,
        variable_values: Optional[Dict[str, Any]] = None,
    ):
        return asyncio.run(
            self._execute_query_async(
                query=query, variable_values=variable_values, key=key
            )
        )

    async def _execute_query_async(
        self,
        query: DocumentNode,
        key: str,
        variable_values: Optional[Dict[str, Any]] = None,
    ):
        async with Client(
            transport=self._transport,
            fetch_schema_from_transport=True,
            execute_timeout=None,
        ) as session:
            update_schema_scalars(session.client.schema, [DatetimeScalar])

            result = await session.execute(
                query,
                variable_values=variable_values,
                serialize_variables=True,
                parse_result=True,
            )

            return result[key]

    def get_chat_logs(self) -> list[ChatLog]:
        return self.execute_query(query=get_chat_logs_query, key="chatLogs")

    def get_chat_log(self, **kwargs: Unpack[GetChatLogArgs]) -> ChatLog:
        return self.execute_query(
            query=get_chat_log_query,
            key="chatLog",
            variable_values={"chatLogId": kwargs["chat_log_id"]},
        )

    def create_chat_completion_annotation(
        self, **kwargs: Unpack[CreateChatCompletionAnnotationArgs]
    ) -> Optional[ChatCompletionAnnotation]:
        return self.execute_query(
            query=create_chat_completion_annotation_mutation,
            key="createChatCompletionAnnotation",
            variable_values={"messageId": kwargs["message"]["id"]},
        )

    def create_chat_log(self, **kwargs: Unpack[CreateChatLogArgs]) -> ChatLog:
        return self.execute_query(
            query=create_chat_log_mutation,
            key="createChatLog",
            variable_values={
                "input": {
                    "customerName": kwargs["customer_name"],
                    "rawText": kwargs["raw_text"],
                    "messages": kwargs["messages"],
                }
            },
        )

    def create_message(self, **kwargs: Unpack[CreateMessageArgs]) -> Message:
        return self.execute_query(
            query=create_message_mutation,
            key="createMessage",
            variable_values={
                "chatLogId": kwargs["chat_log_id"],
                "content": kwargs["content"],
                "role": kwargs["role"],
            },
        )

    def create_response_annotation(
        self, **kwargs: Unpack[CreateResponseAnnotationArgs]
    ):
        return self.execute_query(
            query=create_response_annotation_mutation,
            key="createResponseAnnotation",
            variable_values={
                "messageId": kwargs["message"]["id"],
                "content": kwargs["content"],
            },
        )

    def create_workspace_annotation(
        self, **kwargs: Unpack[CreateWorkspaceAnnotationArgs]
    ):
        return self.execute_query(
            query=create_workspace_annotation_mutation,
            key="createWorkspaceAnnotation",
            variable_values={
                "messageId": kwargs["message"]["id"],
                "content": kwargs["content"],
                "boardNumber": kwargs["board_number"],
            },
        )

    def update_chat_completion_annotation(
        self, **kwargs: Unpack[UpdateChatCompletionAnnotation]
    ):
        return self.execute_query(
            query=update_chat_completion_annotation_mutation,
            key="updateChatCompletionAnnotation",
            variable_values={
                "input": {
                    "id": kwargs["chat_completion_annotation"]["id"],
                    "sentAt": kwargs["sent_at"],
                    "approvalStatus": kwargs["approval_status"],
                }
            },
        )

    def update_chat_log(self, **kwargs: Unpack[UpdateChatLog]):
        return self.execute_query(
            query=update_chat_log_mutation,
            key="updateChatLog",
            variable_values={
                "input": {
                    "customerName": kwargs["customer_name"],
                    "rawText": kwargs["raw_text"],
                    "messages": kwargs["messages"],
                    "shouldClearMessages": kwargs["shouldClearMessages"],
                }
            },
        )

    def create_image_capture_annotation(
        self, **kwargs: Unpack[CreateImageCaptureAnnotation]
    ):
        return self.execute_query(
            query=create_image_capture_annotation_mutation,
            key="createImageCaptureAnnotation",
            variable_values={
                "messageId": kwargs["message"]["id"],
                "imageUrl": kwargs["image_url"],
            },
        )

    def create_code_editor(self, **kwargs: Unpack[CreateCodeEditor]):
        return self.execute_query(
            query=create_code_editor_mutation,
            key="createCodeEditor",
            variable_values={
                "input": {
                    "chatLogId": kwargs["chat_log"]["id"],
                    "programmingLanguage": kwargs["programming_language"],
                    "editorNumber": kwargs["editor_number"],
                    "content": kwargs["content"],
                }
            },
        )

    def update_code_editor(self, **kwargs: Unpack[UpdateCodeEditor]):
        return self.execute_query(
            query=update_code_editor_mutation,
            key="updateCodeEditor",
            variable_values={
                "input": {
                    "id": kwargs["code_editor"]["id"],
                    "content": kwargs["content"],
                }
            },
        )

    def create_word_processor(self, **kwargs: Unpack[CreateWordProcessor]):
        return self.execute_query(
            query=create_word_processor_mutation,
            key="createWordProcessor",
            variable_values={
                "input": {
                    "chatLogId": kwargs["chat_log"]["id"],
                    "number": kwargs["number"],
                    "content": kwargs["content"],
                }
            },
        )

    def update_word_processor(self, **kwargs: Unpack[UpdateWordProcessor]):
        return self.execute_query(
            query=update_word_processor_mutation,
            key="updateWordProcessor",
            variable_values={
                "input": {
                    "id": kwargs["word_processor"]["id"],
                    "content": kwargs["content"],
                }
            },
        )
