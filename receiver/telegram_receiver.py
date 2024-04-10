from typing import Callable, Awaitable

import aiofiles as aiofiles
from telethon import TelegramClient, events
from telethon.tl.types import Message as TgMessage

from parser.base.structs import Message, Chat
from receiver.base.base_receiver import BaseReceiver


class TelegramReceiver(BaseReceiver):
    chat_cache = {}
    whitelist: set | None = None

    def __init__(self, config: dict):
        self.api_id = config['api_id']
        self.api_hash = config['api_hash']
        self.chat_cache = {}
        self.whitelist = None

    def set_whitelist(self, text):
        rows = text.splitlines() if text else ''
        items = [row.split('#')[0].strip() for row in rows]
        self.whitelist = set([item for item in items if item and item.lower() != 'whitelist'])

    async def check_whitelist(self, chat: Chat):
        if self.whitelist is None:
            await self.load_whitelist()
        if not self.whitelist:
            return True
        return chat.id in self.whitelist or chat.username in self.whitelist

    async def save_whitelist(self, text: str):
        if text.lower().startswith('whitelist'):
            self.set_whitelist(text)
            async with aiofiles.open('whitelist.txt', mode='w') as f:
                await f.write(text)

    async def load_whitelist(self):
        try:
            async with aiofiles.open('whitelist.txt', mode='r') as f:
                text = await f.read()
                self.set_whitelist(text)
        except FileNotFoundError:
            self.set_whitelist('')

    def filter_message(self, message: TgMessage) -> bool:
        if message.out:  # only inbox
            return False
        if not message.message:  # only with text
            return False
        return True

    async def prepare_message(self, message):
        chat_id = message.chat_id
        chat = message.chat
        if chat:
            mchat = Chat(chat_id, chat.username, chat.title)
        else:
            chat = self.chat_cache.get(chat_id)
            if not chat:
                chat = await message.get_chat()
                self.chat_cache[chat_id] = chat
            mchat = Chat(chat_id, chat.username, chat.username)
        return Message(mchat, message.message, '')

    def listen(self, func: Callable[[Message], Awaitable[None]]):
        with TelegramClient('name', self.api_id, self.api_hash) as client:

            @client.on(events.NewMessage())
            async def handler(event):
                message = event.message
                if message.out and message.sender.id == message.to_id.user_id:
                    await self.save_whitelist(message.message)
                if self.filter_message(message):
                    msg = await self.prepare_message(message)
                    wl = await self.check_whitelist(msg.chat)
                    if wl:
                        await func(msg)

            client.run_until_disconnected()
