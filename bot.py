import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from Dollar import calculate_dollar_bubble
from Silver import calculate_silver_bubble
from Gold18 import calculate_gold18_bubble
from QuarterCoin import calculate_quarter_coin_bubble
from Suggestion import get_trade_suggestion


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")


# =========================
# Main Menu
# =========================

def get_main_keyboard():

    keyboard = [
        ["💵 حباب دلار", "🥈 حباب نقره"],
        ["🥇 حباب طلای ۱۸", "🪙 حباب ربع‌سکه"],
        ["📊 پیشنهاد خرید / فروش"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# =========================
# Start
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "سلام 👋\n\n"
        "به ربات محاسبه حباب خوش آمدید.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=get_main_keyboard()
    )


# =========================
# Dollar
# =========================

async def dollar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⏳ در حال محاسبه حباب دلار..."
    )

    result = calculate_dollar_bubble()

    message = (
        f"💵 {result['asset']}\n\n"
        f"قیمت بازار: {result['market_price']:,.0f} تومان\n"
        f"ارزش محاسباتی: {result['intrinsic_price']:,.0f} تومان\n"
        f"حباب: {result['bubble']:,.0f} تومان\n"
        f"درصد حباب: {result['bubble_percent']:.2f}%\n"
        f"وضعیت: {result['bubble_status']}\n\n"
        f"ℹ️ {result['bubble_meaning']}"
    )

    await update.message.reply_text(
        message,
        reply_markup=get_main_keyboard()
    )


# =========================
# Silver
# =========================

async def silver(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⏳ در حال محاسبه حباب نقره..."
    )

    result = calculate_silver_bubble()

    message = (
        f"🥈 {result['asset']}\n\n"
        f"قیمت بازار: {result['market_price']:,.0f} تومان\n"
        f"ارزش محاسباتی: {result['intrinsic_price']:,.0f} تومان\n"
        f"حباب: {result['bubble']:,.0f} تومان\n"
        f"درصد حباب: {result['bubble_percent']:.2f}%\n"
        f"وضعیت: {result['bubble_status']}\n\n"
        f"ℹ️ {result['bubble_meaning']}"
    )

    await update.message.reply_text(
        message,
        reply_markup=get_main_keyboard()
    )


# =========================
# Gold 18K
# =========================

async def gold18(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⏳ در حال محاسبه حباب طلای ۱۸ عیار..."
    )

    result = calculate_gold18_bubble()

    message = (
        f"🥇 {result['asset']}\n\n"
        f"قیمت بازار: {result['market_price']:,.0f} تومان\n"
        f"ارزش محاسباتی: {result['intrinsic_price']:,.0f} تومان\n"
        f"حباب: {result['bubble']:,.0f} تومان\n"
        f"درصد حباب: {result['bubble_percent']:.2f}%\n"
        f"وضعیت: {result['bubble_status']}\n\n"
        f"ℹ️ {result['bubble_meaning']}"
    )

    await update.message.reply_text(
        message,
        reply_markup=get_main_keyboard()
    )


# =========================
# Quarter Coin
# =========================

async def quarter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⏳ در حال محاسبه حباب ربع‌سکه..."
    )

    result = calculate_quarter_coin_bubble()

    message = (
        f"🪙 {result['asset']}\n\n"
        f"قیمت بازار: {result['market_price']:,.0f} تومان\n"
        f"ارزش محاسباتی: {result['intrinsic_price']:,.0f} تومان\n"
        f"حباب: {result['bubble']:,.0f} تومان\n"
        f"درصد حباب: {result['bubble_percent']:.2f}%\n"
        f"وضعیت: {result['bubble_status']}\n\n"
        f"ℹ️ {result['bubble_meaning']}"
    )

    await update.message.reply_text(
        message,
        reply_markup=get_main_keyboard()
    )


# =========================
# Buy / Sell Suggestion
# =========================

async def suggestion(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "⏳ در حال محاسبه پیشنهاد خرید/فروش..."
    )

    result = get_trade_suggestion()

    message = (
        f"📊 پیشنهاد خرید / فروش\n\n"
        f"قیمت تمام سکه معمولی: "
        f"{result['fullcoin_price']:,.0f} تومان\n"
        f"قیمت طلای ۱۸ عیار: "
        f"{result['gold18_price']:,.0f} تومان\n\n"
        f"نسبت: {result['ratio']:.2f}\n\n"
        f"💡 {result['suggestion']}"
    )

    await update.message.reply_text(
        message,
        reply_markup=get_main_keyboard()
    )


# =========================
# Button Handler
# =========================

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "💵 حباب دلار":
        await dollar(update, context)

    elif text == "🥈 حباب نقره":
        await silver(update, context)

    elif text == "🥇 حباب طلای ۱۸":
        await gold18(update, context)

    elif text == "🪙 حباب ربع‌سکه":
        await quarter(update, context)

    elif text == "📊 پیشنهاد خرید / فروش":
        await suggestion(update, context)

    else:
        await update.message.reply_text(
            "لطفاً یکی از گزینه‌های منو را انتخاب کنید.",
            reply_markup=get_main_keyboard()
        )
