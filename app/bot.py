from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Ex: https://seuapp.onrender.com/webhook

app = Flask(__name__)

# ========================
# Telegram Bot Application
# ========================

application = ApplicationBuilder().token(TOKEN).build()

# ---- Commands ----

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot funcionando no Render! 🚀")

application.add_handler(CommandHandler("start", start))


# ========================
# Webhook route (Flask)
# ========================

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok", 200


# ========================
# Root route
# ========================

@app.route("/", methods=["GET"])
def home():
    return "Bot online! ✔"


# ========================
# Start webhook server
# ========================

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 10000)),
        webhook_url=WEBHOOK_URL
    )
