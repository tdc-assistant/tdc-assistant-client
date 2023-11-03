from typing import Any, Optional, Dict, TypedDict, Unpack

import asyncio

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
)

from .domain import ChatLog, Message, ChatCompletionAnnotation, MessageRole


class GetChatLogArgs(TypedDict):
    chat_log_id: str


class CreateChatLogArgs(TypedDict):
    customer_name: str


class CreateChatCompletionAnnotationArgs(TypedDict):
    message_id: str


class CreateMessageArgs(TypedDict):
    chat_log_id: str
    content: str
    role: MessageRole


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
            variable_values={"messageId": kwargs["message_id"]},
        )

    def create_chat_log(self, **kwargs: Unpack[CreateChatLogArgs]) -> ChatLog:
        return self.execute_query(
            query=create_chat_log_mutation,
            key="createChatLog",
            variable_values={"customerName": kwargs["customer_name"]},
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
