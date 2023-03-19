from abc import abstractmethod
from datetime import datetime, timedelta


class BaseSymbols:
    items = []
    last_updated = None
    timeout = 30

    def __init__(self):
        self.items = []
        self.last_updated = None

    async def list(self):
        if not self.last_updated or (datetime.now() - self.last_updated) > timedelta(minutes=self.timeout):
            await self.update()
        return self.items

    async def update(self):
        self.items = await self.get_data()

    @abstractmethod
    async def get_data(self):
        pass
