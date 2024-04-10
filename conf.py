import os
import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    for section in ['telegram', 'parser', 'sender']:
        if section not in config:
            config[section] = {}

    tg_api_id = os.environ.get('TG_API_ID', '')
    tg_api_hash = os.environ.get('TG_API_HASH', '')

    if tg_api_id and tg_api_hash:
        config['telegram']['api_id'] = tg_api_id
        config['telegram']['api_hash'] = tg_api_hash

    if not config['telegram'].get('api_id') or not config['telegram'].get('api_hash'):
        print('set config or variables TG_API_ID and TG_API_HASH')
        raise SystemExit(1)

    api_url = os.environ.get('API_URL', '')
    if api_url:
        config['sender']['api_url'] = api_url

    api_key = os.environ.get('API_KEY', '')
    if api_key:
        config['sender']['api_key'] = api_key

    if not config['sender'].get('api_key'):
        print('set config or variable API_KEY')
        raise SystemExit(1)

    return config
