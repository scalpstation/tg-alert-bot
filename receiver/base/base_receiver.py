from abc import abstractmethod
from typing import Callable, Awaitable

from parser.base.structs import Message


class BaseReceiver:

    @abstractmethod
    def listen(self, func: Callable[[Message], Awaitable[None]]):
        pass
