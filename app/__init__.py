from flask import Flask, request, jsonify
from telegram import Bot, Update
from telegram.ext import Dispatcher
import logging
from .config import TELEGRAM_TOKEN
from .services.bot_handlers import register_handlers

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)

    if not TELEGRAM_TOKEN:
        logger.warning("TELEGRAM_TOKEN is not set. Webhook will not work until token is provided.")

    # initialize bot and dispatcher
    bot = Bot(token=TELEGRAM_TOKEN)
    dispatcher = Dispatcher(bot, None, use_context=True)

    # register command handlers
    register_handlers(dispatcher)

    # webhook route
    @app.route("/", methods=["GET"])
    def home():
        return "FutBodeBot API - OK"

    @app.route(f"/webhook/{TELEGRAM_TOKEN}", methods=["POST"])
    def webhook():
        try:
            update = Update.de_json(request.get_json(force=True), bot)
            dispatcher.process_update(update)
        except Exception as e:
            logger.exception("Failed to process update: %s", e)
        return jsonify({"ok": True})

    return app
