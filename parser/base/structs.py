
class Chat:
    id: int = 0
    username: str = ''
    title: str = ''

    def __init__(self, chat_id, username, title):
        self.id = chat_id
        self.username = username
        self.title = title


class Message:
    chat: Chat | None = None
    text: str = ''
    title: str | None = None

    def __init__(self, chat, text, title):
        self.chat = chat
        self.text = text
        self.title = title

