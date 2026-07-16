import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌹 Baga nagaan dhuftan gara Ahmedalajami Bot!\n\n"
        "📚 Channelota Barnootaa\n"
        "🎓 Barnoota fi beekumsa argachuuf nu hordofaa."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Ahmedalajami Bot hojii jalqabe...")
    app.run_polling()

if __name__ == "__main__":
    main()
