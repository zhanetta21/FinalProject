from telegram import Update
from telegram.ext import ContextTypes

from utils.keyboards import (
    main_menu_keyboard,
    grades_keyboard,
    attendance_keyboard,
    deadlines_keyboard,
    schedule_keyboard
)

from utils.helpers import load_json, save_json

from handlers.grades import calculate_total, calculate_needed_score, get_grade_status
from handlers.attendance import (
    calculate_attendance,
    calculate_allowed_absences,
    check_attendance_status
)


DEADLINES_FILE = "data/deadlines.json"
SCHEDULE_FILE = "data/schedule.json"


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
        context.user_data.clear()
        await update.message.reply_text(
            "Grades Module\nChoose an option:",
            reply_markup=grades_keyboard()
        )

    elif text == "Attendance":
        context.user_data.clear()
        await update.message.reply_text(
            "Attendance Module\nChoose an option:",
            reply_markup=attendance_keyboard()
        )

    elif text == "Deadlines":
        context.user_data.clear()
        await update.message.reply_text(
            "Deadlines Module\nChoose an option:",
            reply_markup=deadlines_keyboard()
        )

    elif text == "Schedule":
        context.user_data.clear()
        await update.message.reply_text(
            "Schedule Module\nChoose an option:",
            reply_markup=schedule_keyboard()
        )

    # GRADES

    elif text == "Calculate Total":
        context.user_data["mode"] = "calculate_total"
        await update.message.reply_text(
            "Enter regmid, regend and final scores separated by spaces.\n"
            "Example: 80 75 90"
        )

    elif text == "Needed Score":
        context.user_data["mode"] = "needed_score"
        await update.message.reply_text(
            "Enter regmid, regend and target score separated by spaces.\n"
            "Example: 80 75 70"
        )

    elif context.user_data.get("mode") == "calculate_total":
        try:
            regmid, regend, final = map(float, text.split())

            if regmid < 0 or regend < 0 or final < 0:
                await update.message.reply_text("Scores cannot be negative.")
                return

            total = calculate_total(regmid, regend, final)
            status = get_grade_status(total)

            await update.message.reply_text(
                f"Regmid: {regmid} × 0.3 = {round(regmid * 0.3, 2)}\n"
                f"Regend: {regend} × 0.3 = {round(regend * 0.3, 2)}\n"
                f"Final: {final} × 0.4 = {round(final * 0.4, 2)}\n\n"
                f"Total score: {total}\n"
                f"Grade: {status}"
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 3 numbers correctly.\nExample: 80 75 90"
            )

    elif context.user_data.get("mode") == "needed_score":
        try:
            regmid, regend, target = map(float, text.split())

            needed = calculate_needed_score(regmid, regend, target)

            if needed == 0:
                await update.message.reply_text(
                    f"You already reached {target} points before final."
                )
            elif needed > 100:
                await update.message.reply_text(
                    f"Current weighted score: {round(regmid * 0.3 + regend * 0.3, 2)}\n"
                    f"Target score: {target}\n"
                    f"You need {needed} on final.\n"
                    f"Unfortunately, this is more than 100, so the target is not possible."
                )
            else:
                await update.message.reply_text(
                    f"Current weighted score: {round(regmid * 0.3 + regend * 0.3, 2)}\n"
                    f"Target score: {target}\n"
                    f"You need {needed} on final."
                )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 3 numbers correctly.\nExample: 80 75 70"
            )

    # ATTENDANCE

    elif text == "Calculate Attendance":
        context.user_data["mode"] = "calculate_attendance"
        await update.message.reply_text(
            "Enter total classes and missed classes separated by spaces.\n"
            "Example: 30 5"
        )

    elif text == "Allowed Absences":
        context.user_data["mode"] = "allowed_absences"
        await update.message.reply_text(
            "Enter total classes and missed classes separated by spaces.\n"
            "Example: 30 5"
        )

    elif context.user_data.get("mode") == "calculate_attendance":
        try:
            total_classes, missed_classes = map(int, text.split())

            if total_classes <= 0 or missed_classes < 0 or missed_classes > total_classes:
                await update.message.reply_text("Please enter correct numbers.")
                return

            attended = total_classes - missed_classes
            attendance = calculate_attendance(total_classes, missed_classes)
            status = check_attendance_status(attendance)

            await update.message.reply_text(
                f"Total classes: {total_classes}\n"
                f"Missed classes: {missed_classes}\n"
                f"Attended classes: {attended}\n\n"
                f"Attendance: {attendance}%\n"
                f"Status: {status}"
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 2 numbers correctly.\nExample: 30 5"
            )

    elif context.user_data.get("mode") == "allowed_absences":
        try:
            total_classes, missed_classes = map(int, text.split())

            if total_classes <= 0 or missed_classes < 0 or missed_classes > total_classes:
                await update.message.reply_text("Please enter correct numbers.")
                return

            allowed = calculate_allowed_absences(total_classes, missed_classes)

            await update.message.reply_text(
                f"You can still miss {allowed} classes."
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 2 numbers correctly.\nExample: 30 5"
            )

    # DEADLINES

    elif text == "Add Deadline":
        context.user_data["mode"] = "add_deadline"
        await update.message.reply_text(
            "Enter deadline in this format:\n"
            "Subject - Date\n"
            "Example: Python Project - 25 May"
        )

    elif text == "View Deadlines":
        deadlines = load_json(DEADLINES_FILE)

        if not deadlines:
            await update.message.reply_text("You have no deadlines yet.")
        else:
            message = "Your deadlines:\n\n"

            for index, item in enumerate(deadlines, start=1):
                message += f"{index}. {item['subject']} - {item['date']}\n"

            await update.message.reply_text(message)

    elif text == "Delete Deadline":
        context.user_data["mode"] = "delete_deadline"
        await update.message.reply_text(
            "Enter the number of the deadline you want to delete.\n"
            "Use View Deadlines to see numbers."
        )

    elif context.user_data.get("mode") == "add_deadline":
        try:
            subject, date = text.split("-", 1)

            deadlines = load_json(DEADLINES_FILE)

            deadlines.append({
                "subject": subject.strip(),
                "date": date.strip()
            })

            save_json(DEADLINES_FILE, deadlines)

            await update.message.reply_text("Deadline added successfully.")

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Wrong format.\nExample: Python Project - 25 May"
            )

    elif context.user_data.get("mode") == "delete_deadline":
        try:
            number = int(text)

            deadlines = load_json(DEADLINES_FILE)

            if number < 1 or number > len(deadlines):
                await update.message.reply_text("There is no deadline with this number.")
                return

            deleted = deadlines.pop(number - 1)
            save_json(DEADLINES_FILE, deadlines)

            await update.message.reply_text(
                f"Deleted: {deleted['subject']} - {deleted['date']}"
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter only the number.\nExample: 1"
            )

    # SCHEDULE

    elif text == "Add Schedule":
        context.user_data["mode"] = "add_schedule"
        await update.message.reply_text(
            "Enter schedule in this format:\n"
            "Day - Subject - Time\n"
            "Example: Monday - Python - 10:00"
        )

    elif text == "View Schedule":
        schedule = load_json(SCHEDULE_FILE)

        if not schedule:
            await update.message.reply_text("Your schedule is empty.")
        else:
            message = "Your schedule:\n\n"

            for index, item in enumerate(schedule, start=1):
                message += f"{index}. {item['day']} - {item['subject']} - {item['time']}\n"

            await update.message.reply_text(message)


    elif context.user_data.get("mode") == "add_schedule":

        try:

            text = text.replace("–", "-").replace("—", "-")

            day, subject, time = text.split("-", 2)

            schedule = load_json(SCHEDULE_FILE)

            schedule.append({

                "day": day.strip(),

                "subject": subject.strip(),

                "time": time.strip()

            })

            save_json(SCHEDULE_FILE, schedule)

            await update.message.reply_text("Schedule added successfully.")

            context.user_data.clear()


        except ValueError:

            await update.message.reply_text(

                "Wrong format.\nExample: Monday - Python - 10:00"

            )

    else:
        await update.message.reply_text(
            "Please choose an option from the menu."
        )