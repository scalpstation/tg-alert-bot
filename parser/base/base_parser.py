from abc import abstractmethod

from parser.base.structs import Message
from sender.base.structs import AlertMessage


class BaseParser:

    @abstractmethod
    async def process_message(self, message: Message) -> AlertMessage | None:
        pass
