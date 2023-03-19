import pytest

from parser.default_parser import DefaultParser
from parser.base.structs import Message, Chat


@pytest.mark.asyncio
async def test_format_1():
    parser = DefaultParser()
    msg = '''
    LONG #BTCUSDT from $50000 stop loss $49900

    5m TF. many many text
    '''
    chat = Chat(1, 'chat', 'chat')
    message = Message(chat, msg, '')
    alert = await parser.process_message(message)
    assert alert.symbol == 'BTCUSDT'
    assert alert.exchange == ''
    assert alert.signals == ['telegram', 'long']
