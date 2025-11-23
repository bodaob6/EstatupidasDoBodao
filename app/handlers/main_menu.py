from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Jogos de hoje", callback_data="games_today")],
        [InlineKeyboardButton("🔮 Palpites automáticos", callback_data="predictions")],
    ]

    await update.message.reply_text(
        "📍 *Menu Principal*\nEscolha uma opção:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )
