import requests
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("BASE_URL")

def extract_matches_historic():
    headers = {"X-Auth-Token": TOKEN}
    response = requests.get(f"{API_URL}/competitions/BSA/matches", headers=headers)
    return response.json().get("matches", []) if response.status_code == 200 else []


