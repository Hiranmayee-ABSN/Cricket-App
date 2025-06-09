import requests

class CricketAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.cricapi.com/v1"

    def get_live_matches(self):
        url = f"{self.base_url}/currentMatches?apikey={self.api_key}&offset=0"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get("status") != "success":
                raise Exception("API returned an error")

            matches = data.get("data", [])
            return matches
        except Exception as e:
            print(f"[ERROR] Failed to fetch live matches: {e}")
            return []
