from TGJU import get_live_prices
import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7",
}


OUNCE_TO_GRAM = 31.1034768

PURE_GOLD_WEIGHT = 1.8305955


def get_global_gold_price():

    url = (
        "https://api.tgju.org/v1/market/"
        "indicator/summary-table-data/ons"
    )

    params = {
        "lang": "fa",
        "order_dir": "asc"
    }

    response = requests.get(
        url,
        params=params,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    rows = data.get("data", [])

    if not rows:
        raise RuntimeError(
            "No global gold data returned from TGJU"
        )

    last_row = rows[-1]

    price_text = last_row[3]

    price = float(
        price_text
        .replace(",", "")
        .replace("٬", "")
        .replace(" ", "")
    )

    return price


def get_live_dollar_price():

    prices = get_live_prices()

    dollar_price_riyal = prices["dollar"]

    return dollar_price_riyal / 10


def calculate_quarter_coin_bubble():

    print(
        "========== QUARTER COIN BUBBLE CALCULATION ==========",
        flush=True
    )

    # =========================
    # LIVE QUARTER COIN PRICE
    # =========================

    prices = get_live_prices()

    quarter_price_riyal = prices["quarter"]

    quarter_price_toman = (
        quarter_price_riyal / 10
    )

    print(
        "Quarter coin price:",
        quarter_price_toman,
        flush=True
    )

    # =========================
    # GLOBAL GOLD PRICE
    # =========================

    gold_global = get_global_gold_price()

    print(
        "Gold global:",
        gold_global,
        flush=True
    )

    # =========================
    # LIVE DOLLAR
    # =========================

    dollar_price_toman = get_live_dollar_price()

    print(
        "Dollar price:",
        dollar_price_toman,
        flush=True
    )

    # =========================
    # GOLD PRICE PER GRAM
    # =========================

    gold_price_per_gram = (
        gold_global
        * dollar_price_toman
        / OUNCE_TO_GRAM
    )

    # =========================
    # INTRINSIC VALUE
    # =========================

    intrinsic_price = (
        gold_price_per_gram
        * PURE_GOLD_WEIGHT
    )

    # =========================
    # BUBBLE
    # =========================

    bubble = (
        quarter_price_toman
        - intrinsic_price
    )

    bubble_percent = (
        bubble / intrinsic_price
    ) * 100

    # =========================
    # OUTPUT
    # =========================

    print(
        "========== CALCULATION ==========",
        flush=True
    )

    print(
        "Quarter coin:",
        quarter_price_toman,
        flush=True
    )

    print(
        "Gold global:",
        gold_global,
        flush=True
    )

    print(
        "Dollar:",
        dollar_price_toman,
        flush=True
    )

    print(
        "Gold price per gram:",
        gold_price_per_gram,
        flush=True
    )

    print(
        "Intrinsic:",
        intrinsic_price,
        flush=True
    )

    print(
        "Bubble:",
        bubble,
        flush=True
    )

    print(
        "Bubble percent:",
        bubble_percent,
        flush=True
    )

    # =========================
    # STATUS
    # =========================

    if bubble > 0:

        bubble_status = "حباب مثبت"

        bubble_meaning = (
            "قیمت ربع‌سکه بالاتر از ارزش محاسباتی "
            "طلای خالص موجود در آن قرار دارد."
        )

    elif bubble < 0:

        bubble_status = "حباب منفی"

        bubble_meaning = (
            "قیمت ربع‌سکه پایین‌تر از ارزش محاسباتی "
            "طلای خالص موجود در آن قرار دارد."
        )

    else:

        bubble_status = "بدون حباب"

        bubble_meaning = (
            "قیمت ربع‌سکه تقریباً برابر با ارزش محاسباتی "
            "طلای خالص آن است."
        )

    print(
        "========== QUARTER COIN CALCULATION SUCCESS ==========",
        flush=True
    )

    return {
        "asset": "ربع سکه",
        "market_price": quarter_price_toman,
        "intrinsic_price": intrinsic_price,
        "bubble": bubble,
        "bubble_percent": bubble_percent,
        "bubble_status": bubble_status,
        "bubble_meaning": bubble_meaning
    }

