from gql.transport.aiohttp import AIOHTTPTransport

from .queries import get_chat_logs


class TdcAssistantClient:
    _transport: AIOHTTPTransport

    def __init__(self, url: str):
        self._transport = AIOHTTPTransport(url=url)

    def get_chat_logs(self):
        return get_chat_logs(self._transport)
