await update.message.reply_text(
                f"You can still miss {allowed} classes."
            )

            context.user_data.clear()

        except ValueError:
            await update.message.reply_text(
                "Please enter 2 numbers correctly.\nExample: 30 5"
            )

    elif text == "Deadlines":
        await update.message.reply_text(
            "Deadlines module will be added in the next update."
        )

    elif text == "Schedule":
        await update.message.reply_text(
            "Schedule module will be added in the next update."
        )

    else:
        await update.message.reply_text(
            "Please choose an option from the menu."
        )
