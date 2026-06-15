# slovnykBot

Telegram bot for looking up Ukrainian words on slovnyk.ua.

## MVP

- /start command
- user sends a Ukrainian word or short phrase
- bot validates input
- bot fetches slovnyk.ua page
- parser extracts title, grammar and short definitions
- bot returns concise result with source link

## Project structure

- bot/main.py
- bot/config.py
- bot/handlers/
- bot/services/
- bot/models/
- bot/utils/
- tests/

## Setup

1. Create virtual environment
2. Install dependencies
3. Copy .env.example to .env
4. Add BOT_TOKEN

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Development plan

1. Parser fixtures
2. WordResult model
3. HTML parser
4. Parser tests
5. HTTP client
6. Telegram handler
