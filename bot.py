from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import TOKEN
from handlers.start import start, menu_handler
from handlers.grades import grades_handler
from handlers.attendance import attendance_handler
from handlers.deadlines import deadlines_handler
from handlers.schedule import schedule_handler

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))

    app.add_handler(MessageHandler(filters.Regex("^Grades$"), grades_handler))
    app.add_handler(MessageHandler(filters.Regex("^Attendance$"), attendance_handler))
    app.add_handler(MessageHandler(filters.Regex("^Deadlines$"), deadlines_handler))
    app.add_handler(MessageHandler(filters.Regex("^Schedule$"), schedule_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()