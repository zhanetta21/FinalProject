from telegram import Update
from telegram.ext import ContextTypes

async def schedule_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Schedule module\n"
        "Here we will:\n"
        "- show today's schedule\n"
        "- show weekly schedule\n"
        "- add subjects"
    )