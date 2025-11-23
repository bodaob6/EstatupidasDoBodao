import requests
import logging
from app.config import API_FOOTBALL_KEY

API_BASE = "https://v3.football.api-sports.io"
HEADERS = {"x-apisports-key": API_FOOTBALL_KEY} if API_FOOTBALL_KEY else {}

logger = logging.getLogger(__name__)

def api_get(path, params=None):
    try:
        r = requests.get(f"{API_BASE}{path}", headers=HEADERS, params=params, timeout=12)
        if r.status_code != 200:
            logger.warning("API returned %s for %s", r.status_code, path)
            return None
        return r.json().get("response", [])
    except Exception as e:
        logger.exception("API request failed: %s", e)
        return None

def fetch_fixtures_by_date(date_str):
    return api_get("/fixtures", params={"date": date_str}) or []

def fetch_team_id_by_name(team_name):
    res = api_get("/teams", params={"search": team_name})
    if not res:
        return None
    return res[0]["team"]["id"]

def fetch_last_fixtures_for_team(team_id, last=10):
    return api_get("/fixtures", params={"team": team_id, "last": last}) or []

def get_team_stats(team_name):
    tid = fetch_team_id_by_name(team_name)
    if not tid:
        return None
    matches = fetch_last_fixtures_for_team(tid, last=10)
    # parse simplified metrics
    goals_for = []
    goals_against = []
    for m in matches:
        teams = m.get("teams", {})
        if teams.get("home", {}).get("name") == team_name:
            gfor = m.get("goals", {}).get("home")
            gagain = m.get("goals", {}).get("away")
        else:
            gfor = m.get("goals", {}).get("away")
            gagain = m.get("goals", {}).get("home")
        if isinstance(gfor, int): goals_for.append(gfor)
        if isinstance(gagain, int): goals_against.append(gagain)
    return {
        "goals_for_avg": round((sum(goals_for)/len(goals_for)) if goals_for else 0,2),
        "goals_against_avg": round((sum(goals_again)/len(goals_again)) if goals_again else 0,2),
        "games_count": len(matches)
    }
