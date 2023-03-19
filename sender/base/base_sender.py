from abc import abstractmethod

from sender.base.structs import AlertMessage


class BaseSender:
    @abstractmethod
    async def send(self, alert: AlertMessage):
        pass
