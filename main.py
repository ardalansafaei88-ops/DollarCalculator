from Dollar import calculate_dollar_bubble
from Silver import calculate_silver_bubble
from QuarterCoin import calculate_quarter_coin_bubble
from Gold18 import calculate_gold18_bubble
from BubbleGuide import get_bubble_guide


def print_result(result):

    print("\n" + "=" * 60)

    print(f"دارایی: {result['asset']}")

    print(
        f"قیمت بازار: "
        f"{result['market_price']:,.0f} تومان"
    )

    print(
        f"ارزش محاسباتی: "
        f"{result['intrinsic_price']:,.0f} تومان"
    )

    print(
        f"حباب: "
        f"{result['bubble']:,.0f} تومان"
    )

    print(
        f"درصد حباب: "
        f"{result['bubble_percent']:.2f}%"
    )

    print(
        f"وضعیت: "
        f"{result['bubble_status']}"
    )

    print(
        f"راهنما: "
        f"{result['bubble_meaning']}"
    )

    print("=" * 60)


def main():

    # =========================
    # Dollar
    # =========================

    print("\nدر حال محاسبه دلار...")

    dollar = calculate_dollar_bubble()

    print_result(dollar)

    # =========================
    # Silver
    # =========================

    print("\nدر حال محاسبه نقره...")

    silver = calculate_silver_bubble()

    print_result(silver)

    # =========================
    # Quarter Coin
    # =========================

    print("\nدر حال محاسبه ربع سکه...")

    quarter = calculate_quarter_coin_bubble()

    print_result(quarter)

    # =========================
    # Gold 18
    # =========================

    print("\nدر حال محاسبه طلای ۱۸ عیار...")

    gold18 = calculate_gold18_bubble()

    print_result(gold18)

    # =========================
    # Guide
    # =========================

    print("\n")

    print(get_bubble_guide())


if __name__ == "__main__":
    main()