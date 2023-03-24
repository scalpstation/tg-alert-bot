# Telegram to ScalpStation alert bot

This bot resends signals from Telegram messages to ScalpStation.com API

## Installation

1. Clone this repository
2. Install python 3.10+ and pipenv
3. Type
```bash
pipenv sync
```

## Start

1. Set environment variables  
```bash
TG_API_ID=121345  # https://core.telegram.org/api/obtaining_api_id
TG_API_HASH=121345  # https://core.telegram.org/api/obtaining_api_id
API_KEY=121345  # https://scalpstation.com/settings/alerts
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
