import requests
from app.utils.logs import log

class FootballAPI:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or ""
        self.base_url = "https://api-football-v1.p.rapidapi.com/v3"

    def get(self, endpoint, params=None):
        if not self.api_key:
            log("⚠️ Nenhuma API KEY configurada para FootballAPI")
            return None

        url = f"{self.base_url}/{endpoint}"

        headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
        }

        try:
            res = requests.get(url, headers=headers, params=params)
            log(f"Request GET {url} - status {res.status_code}")
            return res.json()
        except Exception as e:
            log(f"Erro ao acessar API Football: {e}")
            return None
