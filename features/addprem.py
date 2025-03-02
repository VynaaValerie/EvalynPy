# features/addprem.py
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from index import load_database, save_database

async def addprem_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = int(context.args[0])
    data = load_database()
    if user_id not in data["premium_users"]:
        data["premium_users"].append(user_id)
        save_database(data)
        await update.message.reply_text(f"✅ User {user_id} added to premium!")
    else:
        await update.message.reply_text(f"❌ User {user_id} is already premium!")

def register_handlers(application):
    application.add_handler(CommandHandler("addprem", addprem_command))