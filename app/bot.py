import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

from app.handlers.start import start
from app.handlers.webhook import webhook_handler
from app.utils.logs import log

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

application = (
    Application.builder()
    .token(TOKEN)
    .concurrent_updates(True)
    .build()
)

application.add_handler(CommandHandler("start", start))

@app.post("/")
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    application.create_task(webhook_handler(update, application))
    return "OK", 200

@app.get("/healthz")
def health_check():
    return "Bot OK!", 200

if __name__ == "__main__":
    application.run_polling()
