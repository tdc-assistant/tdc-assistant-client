from typing import Any, Optional, Dict

import asyncio

from graphql import DocumentNode

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.utilities import update_schema_scalars

from .scalars import DatetimeScalar
from .queries import get_chat_logs_query

from .domain import ChatLog


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
        self, query: DocumentNode, key: str, variable_values: Optional[Dict[str, Any]]
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
