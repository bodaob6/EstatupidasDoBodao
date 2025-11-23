from flask import Blueprint, request
from telegram import Update
from telegram.ext import Dispatcher

webhook_bp = Blueprint("webhook", __name__)

dispatcher: Dispatcher = None

def set_dispatcher(d):
    global dispatcher
    dispatcher = d

@webhook_bp.route("/webhook", methods=["POST"])
def webhook():
    if dispatcher is None:
        return "Dispatcher not ready", 500

    update = Update.de_json(request.get_json(force=True), dispatcher.bot)
    dispatcher.process_update(update)
    return "OK", 200
