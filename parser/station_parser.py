from parser.base.structs import Message
from parser.default_parser import DefaultParser

from symbols.default_symbols import DefaultSymbols


class StationParser(DefaultParser):

    def __init__(self, config: dict):
        super().__init__()
        self.symbols = DefaultSymbols()

    async def get_symbol(self, message: Message) -> str | None:
        symbol = await super().get_symbol(message)
        if symbol:
            return symbol
        symbols = await self.symbols.list()
        for symbol in symbols:
            coin = symbol.replace('USDT', '').replace('BUSD', '')
            if f'{coin} ' in message.text:
                return symbol
            if f'{coin}\n' in message.text:
                return symbol

