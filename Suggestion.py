from TGJU import get_live_prices


def get_trade_suggestion():

    print(
        "========== TRADE SUGGESTION CALCULATION ==========",
        flush=True
    )

    # =========================
    # LIVE PRICES
    # =========================

    prices = get_live_prices()

    fullcoin_price_riyal = prices["fullcoin"]
    gold18_price_riyal = prices["gold18"]

    fullcoin_price_toman = (
        fullcoin_price_riyal / 10
    )

    gold18_price_toman = (
        gold18_price_riyal / 10
    )

    print(
        "Full coin (regular) price:",
        fullcoin_price_toman,
        flush=True
    )

    print(
        "Gold 18K price:",
        gold18_price_toman,
        flush=True
    )

    # =========================
    # RATIO
    # =========================

    ratio = (
        fullcoin_price_toman
        / gold18_price_toman
    )

    print(
        "Ratio (full coin / gold18):",
        ratio,
        flush=True
    )

    # =========================
    # SUGGESTION
    # =========================

    if 11.3 <= ratio <= 11.8:

        suggestion = (
            "باید طلای آب‌شده رو بفروشی و سکه امامی بخری."
        )

    elif 11.9 <= ratio <= 12.2:

        suggestion = (
            "در حال حاضر هیچ پیشنهاد مناسبی وجود نداره."
        )

    elif 12.3 <= ratio <= 12.8:

        suggestion = (
            "سکه‌ها رو بفروش و طلای ۱۸ عیار بخر."
        )

    else:

        suggestion = (
            "نسبت فعلی خارج از محدوده‌های تعریف‌شده است، "
            "در حال حاضر پیشنهاد مشخصی وجود نداره."
        )

    print(
        "========== TRADE SUGGESTION SUCCESS ==========",
        flush=True
    )

    return {
        "fullcoin_price": fullcoin_price_toman,
        "gold18_price": gold18_price_toman,
        "ratio": ratio,
        "suggestion": suggestion
    }
