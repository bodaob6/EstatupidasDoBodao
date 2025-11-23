from telegram import Update
from telegram.ext import ContextTypes

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Menu principal em construção 🛠️")
