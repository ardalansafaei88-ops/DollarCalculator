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


GRAMS_PER_OUNCE = 31.1034768


def get_silver_global_price():
    url = (
        "https://api.tgju.org/v1/market/"
        "indicator/summary-table-data/silver"
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
            "No silver global data returned from TGJU"
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


def calculate_silver_bubble():

    print(
        "========== SILVER BUBBLE CALCULATION ==========",
        flush=True
    )

    # =========================
    # LIVE SILVER 999 PRICE
    # =========================

    prices = get_live_prices()

    silver_price_riyal = prices["silver999"]

    silver_price_toman = (
        silver_price_riyal / 10
    )

    print(
        "Silver 999 price:",
        silver_price_toman,
        flush=True
    )

    # =========================
    # GLOBAL SILVER PRICE
    # =========================

    silver_ounce = get_silver_global_price()

    print(
        "Silver ounce:",
        silver_ounce,
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
    # INTRINSIC VALUE
    # =========================

    intrinsic_price = (
        silver_ounce
        * dollar_price_toman
    ) / GRAMS_PER_OUNCE

    # =========================
    # BUBBLE
    # =========================

    bubble = (
        silver_price_toman
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
        "Silver 999:",
        silver_price_toman,
        flush=True
    )

    print(
        "Silver ounce:",
        silver_ounce,
        flush=True
    )

    print(
        "Dollar:",
        dollar_price_toman,
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
            "قیمت بازار بالاتر از ارزش محاسباتی قرار دارد. "
            "این وضعیت می‌تواند ناشی از تقاضای بیشتر، "
            "محدودیت عرضه یا انتظارات بازار باشد."
        )

    elif bubble < 0:

        bubble_status = "حباب منفی"

        bubble_meaning = (
            "قیمت بازار پایین‌تر از ارزش محاسباتی قرار دارد. "
            "این وضعیت می‌تواند ناشی از فشار فروش، "
            "تقاضای کمتر یا شرایط بازار باشد."
        )

    else:

        bubble_status = "بدون حباب"

        bubble_meaning = (
            "قیمت بازار تقریباً برابر با ارزش محاسباتی است."
        )

    print(
        "========== SILVER CALCULATION SUCCESS ==========",
        flush=True
    )

    return {
        "asset": "نقره ۹۹۹",
        "market_price": silver_price_toman,
        "intrinsic_price": intrinsic_price,
        "bubble": bubble,
        "bubble_percent": bubble_percent,
        "bubble_status": bubble_status,
        "bubble_meaning": bubble_meaning
    }

