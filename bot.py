
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
)

# 🔑 Your Bot Token
BOT_TOKEN = "8629478489:AAEqCCZVwwVuoDp833ach1cfL56Alirdsdc"

# 📌 Your Telegram Group ID
GROUP_ID = -1003607425997


# 🌟 Welcome New Members Automatically
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    result = update.chat_member

    # Detect new user joined
    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    if old_status in ["left", "kicked"] and new_status == "member":

        user = result.new_chat_member.user

        # User details
        name = user.full_name
        username = f"@{user.username}" if user.username else "N/A"
        user_id = user.id

        # Welcome message
        text = (
            f"🌟 Welcome {name}!\n\n"
            f"🔗 Username : {username}\n"
            f"🆔 User ID : {user_id}\n\n"
            "✨ Tamil Friendship Group ✨\n"
            "💗💗 தமிழ் Chatting Group 💗💗\n\n"
            "Thanks for joining our group 🙌\n\n"
            "📌 Please follow group rules:\n"
            "• Respect everyone\n"
            "• No spam or ads\n"
            "• Stay active and friendly\n\n"
            "Enjoy and stay safe 😊"
        )

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )


# ⏰ Auto Reminder Message
async def auto_post(app):

    while True:

        # Send reminder message
        msg = await app.bot.send_message(
            chat_id=GROUP_ID,
            text=(
                "🛡 Safety Reminder:\n\n"
                "⚠️ Do not share your:\n"
                "• Phone number\n"
                "• Personal photos\n"
                "• Live location\n"
                "with strangers.\n\n"
                "Stay careful while chatting online 💬\n\n"
                "Enjoy and stay safe 😊"
            )
        )

        print("✅ Reminder message sent")

        # Wait 5 minutes
        await asyncio.sleep(300)

        # Delete reminder message
        try:
            await app.bot.delete_message(
                chat_id=GROUP_ID,
                message_id=msg.message_id
            )

            print("🗑 Reminder message deleted")

        except Exception as e:
            print("Delete Error:", e)

        # Wait another 5 minutes
        await asyncio.sleep(300)


# 🚀 Start Background Task
async def post_init(app):

    asyncio.create_task(auto_post(app))


# ▶ Main Function
def main():

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Auto welcome handler
    app.add_handler(
        ChatMemberHandler(
            welcome,
            ChatMemberHandler.CHAT_MEMBER
        )
    )

    print("🤖 Bot Running Successfully...")

    # Start bot
    app.run_polling()


if __name__ == "__main__":
    main()
