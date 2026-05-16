from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

# 🔑 Your Bot Token
BOT_TOKEN = "8629478489:AAEqCCZVwwVuoDp833ach1cfL56Alirdsdc"


# 🤖 Welcome Function
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message and update.message.new_chat_members:

        for member in update.message.new_chat_members:

            name = member.full_name

            welcome_text = (
                f"🌟 Welcome {name}!\n\n"

                "Tamil Friendship Group ✨ தமிழ் Chat Group 💗\n\n"

                "Thanks for joining our group 🙌\n\n"

                "📌 Please follow group rules:\n"
                "• Respect everyone\n"
                "• No spam or ads\n"
                "• Stay active and friendly\n\n"

                "🛡 Safety Reminder:\n"
                "Do not share your phone number, photo, or location with strangers ⚠️\n\n"

                "Enjoy and stay safe 😊"
            )

            await update.message.reply_text(welcome_text)


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome
        )
    )

    print("🤖 Bot Started Successfully...")

    app.run_polling()


if __name__ == "__main__":
    main()
