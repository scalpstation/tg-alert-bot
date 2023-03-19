from parser.base.base_parser import BaseParser
from receiver.base.base_receiver import BaseReceiver
from sender.base.base_sender import BaseSender


class Router:
    def __init__(self, receiver: BaseReceiver, parser: BaseParser, sender: BaseSender):
        self.receiver = receiver
        self.parser = parser
        self.sender = sender

    async def process(self, message):
        alert = await self.parser.process_message(message)
        if alert:
            await self.sender.send(alert)

    def run(self):
        self.receiver.listen(self.process)
