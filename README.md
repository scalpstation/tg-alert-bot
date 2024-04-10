# Telegram to ScalpStation alert bot

This bot resends signals from Telegram messages to ScalpStation.com API

## Installation

1. Clone this repository
2. Install python 3.11+ and pipenv
3. Type
```bash
pipenv sync
```

## Start

1. Copy file config.sample.ini to config.ini and fill it with your data
```bash
[telegram]
api_id = 123456  # https://core.telegram.org/api/obtaining_api_id
api_hash = 123456  # https://core.telegram.org/api/obtaining_api_id
[sender]
api_key = 123456  # https://scalpstation.com/settings/alerts
[receiver]
```
2. Run
```bash
pipenv shell
python main.py
```
3. Enter phone number and login code
4. Enjoy

## Run on Windows

https://www.youtube.com/watch?v=nfDWL8Mg2Q4
