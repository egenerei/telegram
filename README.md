# Telegram Streaming Bot

This project sets up a containerized Telegram bot system that converts audio/video files using FFmpeg and streams them via Icecast. The bot is built in Python and interacts with Telegram's API.

## Features

- Telegram bot interface (`python/bot.py`)
- FFmpeg container for audio/video conversion
- Icecast + Ices2 setup for streaming
- NGINX as a reverse proxy (optional)
- Docker Compose orchestration

## Directory Structure
```
telegram-main/
├── docker-compose.yml
├── ffmpeg/
│ ├── convert.sh
│ └── dockerfile
├── icecast/
│ └── icecast.xml
├── ices2/
│ ├── dockerfile
│ └── ices-playlist.xml
├── nginx_conf/
│ └── nginx.conf
└── python/
├── bot.py
└── dockerfile
```

## Prerequisites

- Docker
- Docker Compose
- A valid Telegram bot token

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/telegram-main.git
   cd telegram-main
   ```
2. Create a .env file with the necessary environment variables (e.g., Telegram bot token).
3. Launch the stack:
```bash
docker compose up -d
```
4. Interact with the bot on Telegram and send media to stream.

## Configuration
- icecast/icecast.xml: Icecast server settings
- ices2/ices-playlist.xml: Playlist and stream metadata
- nginx_conf/nginx.conf: Reverse proxy configuration
- ffmpeg/convert.sh: Media conversion logic
- python/bot.py: Bot logic (includes file handling, conversion, and interaction)

## License

MIT License

## Author

Jorge
