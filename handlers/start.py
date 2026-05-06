from telegram import Update
from telegram.ext import ContextTypes

from utils.keyboards import main_menu_keyboard, grades_keyboard, attendance_keyboard
from handlers.grades import calculate_total, calculate_needed_score
from handlers.attendance import calculate_attendance, calculate_allowed_absences


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "Hello! I am your Student Assistant Bot.\nChoose a section:",
        reply_markup=main_menu_keyboard()
    )


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Back":
        context.user_data.clear()
        await update.message.reply_text(
            "Main menu:",
            reply_markup=main_menu_keyboard()
        )

    elif text == "Grades":
        await update.message.reply_text(
            "Grades Module\nChoose an option:",
            reply_markup=grades_keyboard()
        )

    elif text == "Attendance":
        await update.message.reply_text(
            "Attendance Module\nChoose an option:",
            reply_markup=attendance_keyboard()
        )

    elif text == "Calculate Total":
        context.user_data["mode"] = "calculate_total"
        await update.message.reply_text(
            "Enter regmid, regend and final scores separated by spaces.\nExample: 25 30 35"
        )

    elif text == "Needed Score":
        context.user_data["mode"] = "needed_score"
        await update.message.reply_text(
            "Enter regmid, regend and target score separated by spaces.\nExample: 25 30 70"
        )

    elif text == "Calculate Attendance":
        context.user_data["mode"] = "calculate_attendance"
        await update.message.reply_text(
            "Enter total classes and missed classes separated by spaces.\nExample: 30 5"
        )

    elif text == "Allowed Absences":
        context.user_data["mode"] = "allowed_absences"
        await update.message.reply_text(
            "Enter total classes and missed classes separated by spaces.\nExample: 30 5"
        )

    elif context.user_data.get("mode") == "calculate_total":
        try:
            regmid, regend, final = map(float, text.split())
            total = calculate_total(regmid, regend, final)

            await update.message.reply_text(
                f"Your total score is: {total}"
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 3 numbers correctly.\nExample: 25 30 35"
            )

    elif context.user_data.get("mode") == "needed_score":
        try:
            regmid, regend, target = map(float, text.split())
            needed = calculate_needed_score(regmid, regend, target)

            await update.message.reply_text(
                f"You need {needed} points to reach {target}."
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 3 numbers correctly.\nExample: 25 30 70"
            )

    elif context.user_data.get("mode") == "calculate_attendance":
        try:
            total_classes, missed_classes = map(int, text.split())
            attendance = calculate_attendance(total_classes, missed_classes)

            if attendance >= 70:
                status = "OK"
            else:
                status = "Warning: below 70%"

            await update.message.reply_text(
                f"Your attendance is: {attendance}%\nStatus: {status}"
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 2 numbers correctly.\nExample: 30 5"
            )

    elif context.user_data.get("mode") == "allowed_absences":
        try:
            total_classes, missed_classes = map(int, text.split())
            allowed = calculate_allowed_absences(total_classes, missed_classes)
