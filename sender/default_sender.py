import httpx

from sender.base.structs import AlertMessage
from sender.base.base_sender import BaseSender

API_URL = 'https://scalpstation.com/userapi/external_api/v1/alert'


class DefaultSender(BaseSender):
    url = ''
    api_key = ''

    def __init__(self, config: dict):
        self.url = config.get('url') or API_URL
        self.api_key = config['api_key']
        if not self.api_key or not self.url:
            print('set variable API_KEY')
            raise SystemExit(1)

    async def send(self, alert: AlertMessage):
        client = httpx.AsyncClient()
        print(alert.to_json())
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        resp = await client.post(self.url, headers=headers, json=alert.to_dict())
