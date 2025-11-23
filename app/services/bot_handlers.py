# handlers: start, jogos (skeleton), comparar
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import logging
from .api_football import fetch_fixtures_by_date, get_team_stats

logger = logging.getLogger(__name__)

def start(update, context):
    msg = (
        "👋 Olá! Sou o FutBodeBetBot.\n\n"
        "Comandos:\n"
        "/jogos - listar partidas do dia\n"
        "/comparar <time1> vs <time2> - comparar times\n"
    )
    update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

def comparar_command(update, context):
    raw = update.message.text.replace("/comparar", "").strip()
    if not raw:
        update.message.reply_text("Use: /comparar TimeA vs TimeB")
        return
    sep = "vs" if "vs" in raw else "x" if " x " in raw else None
    if sep:
        parts = raw.replace(",", " ").replace(" x ", " vs ").split("vs")
    else:
        parts = raw.split()
    if len(parts) < 2:
        update.message.reply_text("Formato inválido. Use: /comparar TimeA vs TimeB")
        return
    team_a = parts[0].strip()
    team_b = parts[1].strip()
    update.message.reply_text(f"Processando comparação entre *{team_a}* e *{team_b}*...", parse_mode=ParseMode.MARKDOWN)
    stats = build_comparison_text(team_a, team_b)
    update.message.reply_text(stats, parse_mode=ParseMode.MARKDOWN)

def build_comparison_text(team_a, team_b):
    sa = get_team_stats(team_a)
    sb = get_team_stats(team_b)
    if not sa or not sb:
        return "Dados insuficientes para comparação (API indisponível ou time não encontrado)."
    # simplified output; adapt as needed
    text = f"📊 *Comparativo*: {team_a} vs {team_b}\n\n"
    text += f"*{team_a}* - Gols marcados (média): {sa.get('goals_for_avg', 0)}\n"
    text += f"*{team_b}* - Gols marcados (média): {sb.get('goals_for_avg', 0)}\n"
    text += "\n_Baseado nos últimos 10 jogos._"
    return text

def jogos_command(update, context):
    from datetime import datetime
    today = datetime.utcnow().strftime("%Y-%m-%d")
    fixtures = fetch_fixtures_by_date(today)
    if not fixtures:
        update.message.reply_text("Nenhuma partida disponível hoje ou API indisponível.")
        return
    msg_lines = ["📅 Partidas de hoje:"]
    for f in fixtures[:20]:
        home = f.get("teams", {}).get("home", {}).get("name")
        away = f.get("teams", {}).get("away", {}).get("name")
        time = f.get("fixture", {}).get("date","")[11:16]
        league = f.get("league", {}).get("name")
        msg_lines.append(f"• {home} vs {away} — {league} — {time}")
    update.message.reply_text("\n".join(msg_lines))

def register_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("comparar", comparar_command))
    dispatcher.add_handler(CommandHandler("jogos", jogos_command))
    # add more handlers as needed

# Helper to run polling locally for tests
def run_polling():
    from telegram.ext import Updater
    from app.config import TELEGRAM_TOKEN
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    register_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()
