# features/totaluser.py
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from index import load_database

async def totaluser_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_database()
    total_users = len(data["users"])
    await update.message.reply_text(f"📊 Total Users: {total_users}")

def register_handlers(application):
    application.add_handler(CommandHandler("totaluser", totaluser_command))