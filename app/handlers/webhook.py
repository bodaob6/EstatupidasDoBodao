from telegram import Update
from telegram.ext import ContextTypes
from app.utils.logs import log

async def webhook_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(f"Update recebido: {update.to_dict()}")
    
    if update.message:
        await update.message.reply_text("Recebido!")
