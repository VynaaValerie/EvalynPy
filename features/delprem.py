# features/delprem.py
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from index import load_database, save_database

async def delprem_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = int(context.args[0])
    data = load_database()
    if user_id in data["premium_users"]:
        data["premium_users"].remove(user_id)
        save_database(data)
        await update.message.reply_text(f"✅ User {user_id} removed from premium!")
    else:
        await update.message.reply_text(f"❌ User {user_id} is not premium!")

def register_handlers(application):
    application.add_handler(CommandHandler("delprem", delprem_command))