# features/owner.py
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from evalyn import OWNER_LINK, CHANNEL_LINK

async def owner_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👤 Owner: {OWNER_LINK}\n📢 Channel: {CHANNEL_LINK}")

def register_handlers(application):
    application.add_handler(CommandHandler("owner", owner_command))