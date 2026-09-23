import asyncio
import os
import threading

from flask import Flask, request

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot import start, dollar, silver, gold18, quarter, suggestion, handle_menu
app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "10000"))

telegram_app = Application.builder().token(TOKEN).build()

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("dollar", dollar))
telegram_app.add_handler(CommandHandler("silver", silver))
telegram_app.add_handler(CommandHandler("gold", gold18))
telegram_app.add_handler(CommandHandler("quarter", quarter))
telegram_app.add_handler(CommandHandler("suggestion", suggestion))

telegram_app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu)
)

loop = asyncio.new_event_loop()


def run_telegram():
    asyncio.set_event_loop(loop)

    loop.run_until_complete(telegram_app.initialize())
    loop.run_until_complete(telegram_app.start())

    webhook_url = "https://dollarcalculator.ardalansafaei.blitz.cloud/telegram"

    loop.run_until_complete(
        telegram_app.bot.set_webhook(webhook_url)
    )

    loop.run_forever()


@app.get("/")
def health():
    return "OK"


@app.post("/telegram")
def telegram_webhook():
    data = request.get_json(force=True)

    update = Update.de_json(data, telegram_app.bot)

    loop.call_soon_threadsafe(
        telegram_app.update_queue.put_nowait,
        update
    )

    return "OK"


if __name__ == "__main__":
    threading.Thread(
        target=run_telegram,
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=PORT
    )