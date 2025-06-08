# 🤖 Telegram Streaming Bot

A containerized Telegram bot system that converts audio/video files using FFmpeg and streams them via Icecast. The bot is built in Python and interacts with Telegram's API to enable media streaming directly from Telegram chats.

---

## 🚀 Features

- 🤖 Telegram bot interface for receiving and processing media (`python/bot.py`)
- 🎞️ FFmpeg container for audio/video format conversion
- 📡 Icecast and Ices2 setup for streaming media over HTTP
- 🌐 Optional NGINX reverse proxy configuration
- 🐳 Orchestrated with Docker Compose for easy deployment

---

## 🗂️ Project Structure

```
telegram-main/
├── docker-compose.yml          # Docker Compose orchestration file
├── ffmpeg/
│   ├── convert.sh              # Media conversion script using FFmpeg
│   └── dockerfile              # FFmpeg Docker image build file
├── icecast/
│   └── icecast.xml             # Icecast streaming server configuration
├── ices2/
│   ├── dockerfile              # Ices2 Docker image build file
│   └── ices-playlist.xml       # Streaming playlist and metadata
├── nginx_conf/
│   └── nginx.conf              # NGINX reverse proxy configuration
└── python/
    ├── bot.py                 # Telegram bot main script
    └── dockerfile             # Python bot Docker image build file
```

---

## 🛠️ Prerequisites

- 🐳 Docker
- 📦 Docker Compose
- 🤖 A valid Telegram bot token (from BotFather)

---

## ⚡ Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/telegram-main.git
   cd telegram-main
   ```

2. **Create a `.env` file with your configuration variables:**

   ```
   DOMAIN=example.org
   BOT_TOKEN=your_telegram_bot_token_here
   ```

3. **Start the full stack:**

   ```bash
   docker compose up -d
   ```

4. **Use your Telegram bot:**  
   Open Telegram, find your bot, and send audio/video files to start streaming.

---

## ⚙️ Configuration Details

- `icecast/icecast.xml`: Configure your Icecast streaming server (ports, passwords, mount points).
- `ices2/ices-playlist.xml`: Playlist metadata and stream details.
- `nginx_conf/nginx.conf`: NGINX reverse proxy setup (if you want to expose Icecast streams via domain).
- `ffmpeg/convert.sh`: Script that handles media conversion using FFmpeg.
- `python/bot.py`: Core Telegram bot logic — manages file downloads, conversion triggers, and interaction with Telegram API.

---

## 📝 License

This project is licensed under the MIT License.

---

## 👤 Author

Jorge Del Rey Prieto
