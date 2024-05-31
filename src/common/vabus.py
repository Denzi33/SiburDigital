import sys

sys.path.append("../data")
sys.path.append("../common")

from data.event import Event
from data.metric import Metric
from aiohttp import ClientSession
from common.decorators import singleton


@singleton
class VaBus:
    def __init__(self, url: str = None) -> None:
        self.url: str = url
        self._session = ClientSession(base_url=url) if url is not None else None

    async def __aenter__(self) -> "VaBus":
        """
        Initialize connection to bus
        """

        await self._session.__aenter__()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close connection to bus
        """

        await self._session.__aexit__(exc_type, exc_val, exc_tb)

    async def get_event(self) -> Event:
        pass

    async def get_metric(self) -> Metric:
        pass

    async def send_event(self, event: Event) -> int:
        pass

    async def send_metric(self, metric: Metric) -> int:
        pass
