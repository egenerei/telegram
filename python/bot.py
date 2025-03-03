import os  # Importing the os module to interact with the operating system
import hashlib  # Importing hashlib for generating MD5 hash
import yt_dlp  # Importing yt_dlp for downloading YouTube videos
from telegram import Update  # Importing Update class from python-telegram-bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext  # Importing necessary classes for Telegram bot

# Retrieve the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Path to store downloaded videos
SAVE_PATH_VIDEOS = "downloads/videos/"
SAVE_PATH_AUDIO = "downloads/audio/"

# Function to generate an MD5 hash from a string and return the first 8 characters
def generate_md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()[:8]

# Function to handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me a YouTube link, and I'll download the video for you!")

# Function to handle messages containing YouTube URLs
async def download_video(update: Update, context: CallbackContext):
    url = update.message.text  # Get the URL from the user's message
    chat_id = update.message.chat_id  # Get the chat ID

    url = url[3:]
    # Check if the message contains a YouTube URL
    if "youtube.com" in url or "youtu.be" in url:
        await update.message.reply_text("Downloading video, please wait...")

        # Ensure the downloads folder exists
        os.makedirs(SAVE_PATH_VIDEOS, exist_ok=True)

        # Generate an MD5 hash for the filename
        file_hash = generate_md5_hash(url)
        
        # Define yt-dlp options for downloading
        ydl_opts = {
            'outtmpl': SAVE_PATH_VIDEOS + file_hash + '.%(ext)s',  # Output filename using MD5 hash
        }

        try:
            # Use yt-dlp to download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)  # Extract video info and download
                file_path = ydl.prepare_filename(info)  # Get the downloaded file path

            await update.message.reply_text("Download complete! Uploading...")

        except Exception as e:
            # Handle errors and notify the user
            await update.message.reply_text(f"Error: {str(e)}")
    else:
        # Inform the user if the URL is not a valid YouTube link
        await update.message.reply_text("Please send a valid YouTube link.")


    # Function to handle messages containing YouTube URLs and download audio
async def download_audio(update: Update, context: CallbackContext):
    url = update.message.text  # Get and clean the URL from the user's message
    chat_id = update.message.chat_id   # Get the chat ID

    url = url[3:]  # Trim the first 3 characters if needed

    # Check if the message contains a YouTube URL
    if "youtube.com" in url or "youtu.be" in url:
        await update.message.reply_text("Downloading audio, please wait...")

        # Ensure the downloads folder exists
        os.makedirs(SAVE_PATH_AUDIO, exist_ok=True)

        # Generate an MD5 hash for the filename
        file_hash = generate_md5_hash(url)
        
        # Define yt-dlp options for downloading audio
        ydl_opts = {
            'format': 'bestaudio/best',  # Select best available audio format
            'outtmpl': SAVE_PATH_AUDIO + file_hash + '.%(ext)s',  # Output filename using MD5 hash
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Convert to standard audio format
                'preferredcodec': 'mp3',  # Convert to MP3
                'preferredquality': '192',  # Set quality to 192kbps
            }],
        }

        try:
            # Use yt-dlp to download the audio
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)  # Extract info and download
                file_path = ydl.prepare_filename(info)  # Get the original downloaded file path
                file_path = os.path.splitext(file_path)[0] + ".mp3"  # Ensure MP3 extension

            await update.message.reply_text("Download complete! Uploading...")

        except Exception as e:
            # Handle errors and notify the user
            await update.message.reply_text(f"Error: {str(e)}")
    else:
        # Inform the user if the URL is not a valid YouTube link
        await update.message.reply_text("Please send a valid YouTube link.")



# Main function to run the bot
def main():
    # Create a Telegram bot application instance
    app = Application.builder().token(BOT_TOKEN).build()

    # Add handlers for bot commands and messages
    app.add_handler(CommandHandler("start", start))  # Handle /start command
    app.add_handler(CommandHandler("dv", download_video))  # Handle YouTube link messages
    app.add_handler(CommandHandler("da", download_audio))  # Handle YouTube link messages

    print("Bot is running...")
    app.run_polling()  # Start polling for new messages

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()