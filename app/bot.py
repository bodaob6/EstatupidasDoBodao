import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from app.handlers.start import start_command
from app.handlers.help import help_command
from app.handlers.main_menu import menu_command
from app.utils.logs import logger


TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", 10000))

# Flask app
app = Flask(__name__)

# Telegram Application
application = ApplicationBuilder().token(TOKEN).build()

# ========================
# Register Handlers
# ========================
application.add_handler(CommandHandler("start", start_command))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("menu", menu_command))


# ========================
# Webhook (Flask)
# ========================
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, application.bot)
        application.update_queue.put_nowait(update)

        logger.info("Update recebido do webhook.")
        return "ok", 200

    except Exception as e:
        logger.error(f"Erro no webhook: {e}")
        return "error", 500


@app.route("/", methods=["GET"])
def home():
    return "Bot online e funcionando ✔", 200


# ========================
# Iniciar o Webhook
# ========================
if __name__ == "__main__":
    logger.info("Iniciando servidor do bot...")
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
    )
