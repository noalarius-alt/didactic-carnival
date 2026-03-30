# Discord Translation Voice Bot

A Discord bot that translates messages and speaks them aloud in voice channels.

## Features

- 🌍 Translates messages to any language using Google Cloud Translation API
- 🔊 Speaks translated text in voice channels
- 🎯 Simple command interface
- ⚙️ Configurable language settings

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Google Cloud credentials and Discord bot token
4. Create `.env` file with your credentials (see `.env.example`)

## Configuration

Create a `.env` file with:
```
DISCORD_BOT_TOKEN=your_token_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
DEFAULT_LANGUAGE=es
```

## Usage

Start the bot:
```bash
python main.py
```

### Commands

- `!translate <message>` - Translates and speaks the message in your voice channel

## Requirements

- Python 3.8+
- Discord.py 2.0+
- Google Cloud Translation API
- pyttsx3 for text-to-speech

## License

MIT