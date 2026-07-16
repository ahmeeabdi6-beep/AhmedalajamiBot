import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text(
            "🌹 Baga nagaan dhuftan gara Ahmedalajami Bot!\n\n"
            "📚 Channelota Barnootaa\n"
            "🎓 Barnoota fi beekumsa argachuuf nu hordofaa."
        )
        logger.info(f"Start command used by {update.effective_user.username}")
    except Exception as e:
        logger.error(f"Error in start command: {e}")

async def post_init(app: Application) -> None:
    logger.info("Bot successfully started and ready!")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set!")
    
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    
    # Add post_init callback
    app.post_init = post_init
    
    logger.info("Ahmedalajami Bot hojii jalqabe...")
    
    try:
        app.run_polling()
    except KeyboardInterrupt:
        logger.info("Bot stop requests...")
    except Exception as e:
        logger.error(f"Critical error: {e}")
        raise

if __name__ == "__main__":
    main()
