import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set!")

WELCOME_TEXT = """
👋 Welcome {name}!

Glad to have you here 😊
Please follow the group rules.
"""

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        name = member.full_name

        await update.message.reply_text(
            WELCOME_TEXT.format(name=name)
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome
        )
    )

    print("Bot running successfully...")

    app.run_polling()

if __name__ == "__main__":
    main()
