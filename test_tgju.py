import re
import requests

html = requests.get(
    "https://www.tgju.org/",
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
).text

profiles = [
    "price_dollar_rl",
    "geram18",
    "silver_999",
    "rob",
]

for profile in profiles:
    pattern = (
        r'data-market-nameslug="'
        + profile
        + r'".*?data-price="([0-9,]+)"'
    )

    match = re.search(pattern, html, re.S)

    if match:
        print(profile, match.group(1))
    else:
        print(profile, "NOT FOUND")
