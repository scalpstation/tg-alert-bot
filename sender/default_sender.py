import os
import httpx

from sender.base.structs import AlertMessage
from sender.base.base_sender import BaseSender

API_URL = os.environ.get('API_URL', 'https://scalpstation.com/userapi/external_api/v1/alert')
API_KEY = os.environ.get('API_KEY', '')


class DefaultSender(BaseSender):
    url = ''
    api_key = ''

    def __init__(self, url: str = '', api_key: str = ''):
        self.url = url or API_URL
        self.api_key = api_key or API_KEY
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
