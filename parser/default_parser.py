import re

from parser.base.base_parser import BaseParser
from parser.base.structs import Message

from sender.default_sender import AlertMessage

USDT_PATTTERN = re.compile('([a-zA-Z]+USDT)')


class DefaultParser(BaseParser):

    def check_source(self, message: Message) -> bool:
        return True

    async def get_symbol(self, message: Message) -> str | None:
        matches = USDT_PATTTERN.findall(message.text)
        if matches:
            return matches[0]

    def get_exchange(self, message: Message) -> str:
        return ''

    def get_title(self, message: Message) -> str:
        return message.chat.title or 'telegram'

    def get_text(self, message: Message) -> str:
        return message.text

    def get_signals(self, message: Message) -> list[str]:
        signals = ['telegram']
        l_text = message.text.lower()
        if 'long' in l_text:
            signals.append('long')
        if 'short' in l_text:
            signals.append('short')
        return signals

    def get_color(self, message) -> str:
        return ''

    def prepare_alert(
            self, symbol: str, exchange: str, signals: list[str], title: str, text: str, color: str,
    ) -> AlertMessage:
        return AlertMessage(symbol, exchange, signals, title, text, color)

    def filter_alert(self, alert, message: Message):
        return alert

    async def process_message(self, message: Message) -> AlertMessage | None:
        if self.check_source(message):
            symbol = await self.get_symbol(message)
            exchange = self.get_exchange(message)
            if symbol:
                signals = self.get_signals(message)
                color = self.get_color(message)
                text = self.get_text(message)
                title = self.get_title(message)
                alert = self.prepare_alert(symbol, exchange, signals, title, text, color)
                return self.filter_alert(alert, message)
        return None
