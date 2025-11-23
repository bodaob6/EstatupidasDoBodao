import os
from flask import Flask
from telegram.ext import Dispatcher, CommandHandler
from telegram import Bot

from app.handlers.webhook import webhook_bp, set_dispatcher
from app.handlers.start import start
from app.handlers.help import help_command

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def create_app():
    app = Flask(__name__)

    bot = Bot(token=TELEGRAM_TOKEN)
    dispatcher = Dispatcher(bot, None, use_context=True)
    set_dispatcher(dispatcher)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    app.register_blueprint(webhook_bp)

    @app.route("/")
    def home():
        return "Bot online!"

    @app.route("/set_webhook")
    def set_webhook():
        webhook_url = "https://estatupidas-bot.onrender.com/webhook"
        bot.set_webhook(url=webhook_url)
        return f"Webhook definido para: {webhook_url}"

    return app

app = create_app()
