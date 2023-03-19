import json


class AlertMessage:
    symbol = ''
    exchange = ''
    title = ''
    text = ''
    signals = []
    color = ''

    def __init__(
            self,
            symbol: str,
            exchange: str,
            signals: list[str],
            title: str | None = None,
            text: str | None = None,
            color: str | None = None
    ):
        self.symbol = symbol
        self.exchange = exchange
        self.title = title
        self.text = text
        self.signals = signals
        self.color = color

    def __str__(self):
        return f'{self.symbol}: {self.signals}: {self.title}'

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'exchange': self.exchange,
            'title': self.title,
            'text': self.text,
            'signals': self.signals,
            'color': self.color,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)
