import os
import feedparser
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

RSS = {
    "nigeria": "https://punchng.com/feed/",
    "world": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "sport": "http://feeds.bbci.co.uk/sport/rss.xml"
}

def get_news(cat="nigeria"):
    feed = feedparser.parse(RSS[cat])
    txt = f"📰 LATEST {cat.upper()} NEWS\n\n"
    for i, e in enumerate(feed.entries[:5], 1):
        txt += f"{i}. {e.title}\n{e.link}\n\n"
    return txt

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /nigeria /world /sport")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cat = update.message.text.replace("/", "")
    await update.message.reply_text(get_news(cat))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("nigeria", news))
app.add_handler(CommandHandler("world", news))
app.add_handler(CommandHandler("sport", news))
app.run_polling()
