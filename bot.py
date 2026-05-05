from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

from flask import Flask
from threading import Thread

# 🔑 NEW TOKEN HERE
BOT_TOKEN = "8629478489:AAE0UWX2WAZXQmjA6Q8AOEPL7J8GivZOlLc"


# 🌐 Keep-alive web server (for Replit)
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is running!"

def run():
    app_web.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


# 🤖 Welcome function
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.new_chat_members:
        for member in update.message.new_chat_members:
            name = member.full_name

            welcome_text = (
                f"🌟 Welcome {name}!\n\n"

                "Tamil Friendship Group ✨ Tamil Chatting Group 💗💗 தமிழ்\n\n"

                "Thanks for joining our group 🙌\n\n"

                "📌 Please follow group rules:\n"
                "• Respect everyone\n"
                "• No spam or ads\n"
                "• Stay active and friendly\n\n"

                "🛡 Safety Reminder:\n"
                "Do not share your phone number, photo, location with anyone. ⚠️\n\n"

                "Enjoy and stay safe! 😊"
            )

            await update.message.reply_text(welcome_text)


def main():
    keep_alive()  # 🔥 keeps Replit alive

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome
        )
    )

    print("🤖 Bot started successfully...")
    app.run_polling()


if __name__ == "__main__":
    main()
