"""Minimal DeFi TVL (DeFiLlama) API call — one typed row per chain.

Docs & schema: https://quanticdata.io/collectors/defillama-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/defillama/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "max_results": 50
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("chain"), row.get("tvl"), row.get("token_symbol"))
print(f"{len(data['results'])} chains, cost ${data['cost']}")
