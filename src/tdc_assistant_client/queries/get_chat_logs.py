from typing import List

import asyncio

from gql import gql, Client
from gql.utilities import update_schema_scalars
from gql.transport.aiohttp import AIOHTTPTransport

from ..scalars import DatetimeScalar
from ..domain import ChatLog

query = gql(
    """
    query ChatLogs {
      chatLogs {
        id
        createdAt
        updatedAt
        deletedAt
        customerName
        messages {
          id
          createdAt
          updatedAt
          deletedAt
          content
          role
          annotations {
            ... on ResponseAnnotation {
              id
              createdAt
              updatedAt
              deletedAt
              type
              content
              messageId
            }
            ... on WorkspaceAnnotation {
              id
              createdAt
              updatedAt
              deletedAt
              messageId
              type
              content
              boardNumber
            }
            ... on ChatCompletionAnnotation {
              id
              createdAt
              updatedAt
              deletedAt
              sentAt
              messageId
              type
              approvalStatus
              responseAnnotationId
              chatCompletion {
                id
                createdAt
                updatedAt
                deletedAt
                parts {
                  id
                  createdAt
                  updatedAt
                  deletedAt
                  content
                  type
                  programmingLanguage
                  shouldOmit
                }
              }
            }
          }
        }
        workspaces {
          id
          createdAt
          updatedAt
          deletedAt
          chatLogId
          boardNumber
          type
          content
        }
      }
    }
"""
)


async def get_chat_logs_async(transport: AIOHTTPTransport) -> List[ChatLog]:
    async with Client(
        transport=transport, fetch_schema_from_transport=True, execute_timeout=None
    ) as session:
        update_schema_scalars(session.client.schema, [DatetimeScalar])

        result = await session.execute(
            query,
            serialize_variables=True,
            parse_result=True,
        )

        return result["chatLogs"]


def get_chat_logs(transport: AIOHTTPTransport) -> List[ChatLog]:
    return asyncio.run(get_chat_logs_async(transport))
