# index.py
import os
import json
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from evalyn import OWNER_ID, BOT_TOKEN

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="logs/bot.log"
)
logger = logging.getLogger(__name__)

# Load database
DATABASE_FILE = "database.json"
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "w") as f:
        json.dump({"users": {}, "groups": {}, "premium_users": [], "limits": {}}, f)

def load_database():
    with open(DATABASE_FILE, "r") as f:
        return json.load(f)

def save_database(data):
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Load all features dynamically
def load_features(application):
    features_dir = "features"
    for filename in os.listdir(features_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = __import__(f"features.{module_name}", fromlist=[module_name])
            if hasattr(module, "register_handlers"):
                module.register_handlers(application)

# Notify owner when bot is online
async def notify_owner(application):
    await application.bot.send_message(chat_id=OWNER_ID, text="🤖 Evalyn Era is now online!")

# Main function
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Load features
    load_features(application)

    # Notify owner
    application.run_polling()
    application.run_until_disconnected()

if __name__ == "__main__":
    main()