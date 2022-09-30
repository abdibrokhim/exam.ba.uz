from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TG_BOT_TOKEN = ''


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'🌚 Sap!, {update.effective_user.first_name}')
    await update.message.reply_text('🌝 Send me a message and I will reverse it!')


async def reverse_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Original: ' + update.message.text + '\n\nReversed: ' + update.message.text[::-1])


if __name__ == '__main__':
    app = ApplicationBuilder().token(TG_BOT_TOKEN).read_timeout(100).get_updates_read_timeout(100).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.TEXT, reverse_handler))

    print('updated...')
    app.run_polling()
