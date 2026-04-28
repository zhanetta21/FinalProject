from telegram import Update
from telegram.ext import ContextTypes

async def grades_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Grades module\n"
        "Here we will calculate:\n"
        "- regmid\n"
        "- regend\n"
        "- final\n"
        "- total\n"
        "- needed score"
    )
from utils.keyboards import grades_keyboard


async def grades_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Grades Module\nChoose an option:",
        reply_markup=grades_keyboard()
    )
