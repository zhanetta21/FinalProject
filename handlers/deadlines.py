from telegram import Update
from telegram.ext import ContextTypes

async def deadlines_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Deadlines module\n"
        "Here we will:\n"
        "- add deadlines\n"
        "- view deadlines\n"
        "- delete deadlines"
    )