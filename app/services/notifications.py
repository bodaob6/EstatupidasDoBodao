from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from .api_football import fetch_fixtures_by_date
import logging
from app.config import TIMEZONE
import pytz

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler(timezone=pytz.timezone(TIMEZONE))

def schedule_daily_checks(send_fn):
    # schedule daily 09:00 check
    scheduler.add_job(lambda: daily_check(send_fn), "cron", hour=9, minute=0)
    scheduler.start()

def daily_check(send_fn):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    fixtures = fetch_fixtures_by_date(today)
    # filter important matches (placeholder)
    important = []
    for f in fixtures:
        # placeholder rules to determine importance
        important.append(f)
    if important:
        send_fn(important)
