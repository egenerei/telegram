import os
import yt_dlp
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

BOT_TOKEN = os.getenv("BOT_TOKEN")

# path to downloaded videos
SAVE_PATH = "downloads/"

# Function to handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me a YouTube link, and I'll download the video for you!")

# Function to handle messages containing YouTube URLs
async def download_video(update: Update, context: CallbackContext):
    url = update.message.text
    chat_id = update.message.chat_id

    if "youtube.com" in url or "youtu.be" in url:
        await update.message.reply_text("Downloading video, please wait...")

        # Ensure the downloads folder exists
        os.makedirs(SAVE_PATH, exist_ok=True)

        # Define yt-dlp options
        ydl_opts = {
            'outtmpl': SAVE_PATH + '%(title)s.%(ext)s',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                file_path = ydl.prepare_filename(info)

            await update.message.reply_text("Download complete! Uploading...")

        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")
    else:
        await update.message.reply_text("Please send a valid YouTube link.")

# Main function to run the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
