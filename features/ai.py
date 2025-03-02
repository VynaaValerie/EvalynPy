# features/ai.py
import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from evalyn import BOT_TOKEN

API_URL = "https://api.siputzx.my.id/api/ai/gpt3"

async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = "kamu adalah ai yang ceria"
    content = update.message.text
    response = requests.get(f"{API_URL}?prompt={prompt}&content={content}").json()
    await update.message.reply_text(response["data"])

def register_handlers(application):
    application.add_handler(CommandHandler("ai", ai_command))