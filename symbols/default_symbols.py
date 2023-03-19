import json
import os
import httpx

from symbols.base.base_symbols import BaseSymbols


SYMBOLS_URL = os.environ.get('SYMBOLS_URL', 'https://scalpstation.com/kapi/binance/futures/symbols')


class DefaultSymbols(BaseSymbols):

    def __init__(self):
        super().__init__()
        self.url = SYMBOLS_URL

    async def get_data(self):
        client = httpx.AsyncClient()
        resp = await client.get(self.url)
        body = resp.read()
        return json.loads(body.decode('utf8'))
