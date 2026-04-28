from telegram import Update
from telegram.ext import ContextTypes

from utils.keyboards import main_menu_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your Student Assistant Bot.\nChoose a section:",
        reply_markup=main_menu_keyboard()
    )


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Back":
        await update.message.reply_text(
            "Main menu:",
            reply_markup=main_menu_keyboard()
        )

    elif text == "Calculate Total":
        await update.message.reply_text(
            "Here we will calculate total score."
        )

    elif text == "Needed Score":
        await update.message.reply_text(
            "Here we will calculate needed score."
        )

    elif text == "Calculate Attendance":
        await update.message.reply_text(
            "Here we will calculate attendance percentage."
        )

    elif text == "Allowed Absences":
        await update.message.reply_text(
            "Here we will calculate allowed absences."
        )

    else:
        await update.message.reply_text(
            "Please choose an option from the menu."
        )
