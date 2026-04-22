from telegram import Update
from telegram.ext import ContextTypes

async def attendance_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Attendance module\n"
        "Here we will calculate:\n"
        "- attendance percentage\n"
        "- allowed absences"
    )