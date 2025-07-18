import os
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

async def handle_replace_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message.reply_to_message:
        return

    match = re.match("Quisiste decir: "r'^/s/([^/]+)/([^/]+)$', message.text.strip())
    if not match:
        return

    original, nuevo = match.groups()
    texto_original = message.reply_to_message.text
    texto_nuevo = texto_original.replace(original, nuevo, 1)

    await message.reply_text(texto_nuevo)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.TEXT & filters.Regex(r'^/s/[^/]+/[^/]+'), handle_replace_command)
    app.add_handler(handler)
    print("Bot iniciado correctamente..")
    app.run_polling()

