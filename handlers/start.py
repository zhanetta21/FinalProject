from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from utils.keyboards import main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Student Assistant Bot.\nChoose a section:",
        reply_markup=main_menu_keyboard()
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Grades":
        await update.message.reply_text("Grades section opened.")
    elif text == "Attendance":
        await update.message.reply_text("Attendance section opened.")
    elif text == "Deadlines":
        await update.message.reply_text("Deadlines section opened.")
    elif text == "Schedule":
        await update.message.reply_text("Schedule section opened.")
    else:
        await update.message.reply_text("Please choose an option from the menu.")