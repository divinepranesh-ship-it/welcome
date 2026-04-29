import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters
)

# Get token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_TEXT = """
👋 Welcome {name}!

Glad to have you in our group 😊
Please read the group rules.
"""

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        for member in update.message.new_chat_members:
            name = member.full_name

            text = WELCOME_TEXT.format(name=name)

            await update.message.reply_text(text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome
        )
    )

    print("Bot started...")

    app.run_polling()

if __name__ == "__main__":
    main()
