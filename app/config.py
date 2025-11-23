import os
from dotenv import load_dotenv

load_dotenv()  # carrega .env localmente (não usado em Render)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY", "")
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "True").lower() in ("1", "true", "yes")
PUBLIC_URL = os.getenv("PUBLIC_URL", "")  # ex: https://meu-servico.onrender.com
TIMEZONE = os.getenv("TIMEZONE", "America/Sao_Paulo")
