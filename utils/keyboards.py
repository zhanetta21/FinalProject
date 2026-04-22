from telegram import ReplyKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        ["Grades", "Attendance"],
        ["Deadlines", "Schedule"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)