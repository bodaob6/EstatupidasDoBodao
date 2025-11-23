from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📘 *Ajuda do Bot*\n\n"
        "Aqui estão alguns comandos úteis:\n"
        "• /start – Inicia o bot\n"
        "• /help – Mostra esta mensagem de ajuda\n"
        "• /menu – Abre o menu principal\n"
    )

    await update.message.reply_text(text, parse_mode="Markdown")
