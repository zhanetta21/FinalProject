from telegram import ReplyKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        ["Grades", "Attendance"],
        ["Deadlines", "Schedule"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def grades_keyboard():
    keyboard = [
        ["Calculate Total"],
        ["Needed Score"],
        ["Back"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def attendance_keyboard():
    keyboard = [
        ["Calculate Attendance"],
        ["Allowed Absences"],
        ["Back"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
