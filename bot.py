import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

API_ID = int(os.environ.get("33650679"))
API_HASH = os.environ.get("7c1d5a774b0df941faa2e6f7693d42fa")
BOT_TOKEN = os.environ.get("8242973997:AAG14K7tjyUykT9SFLuiIT1TdAcIrNytZrY")

TERABOX_DOMAINS = [
    "terabox.com",
    "terabox.app",
    "1024tera.com",
    "1024terabox.com"
]

app = Client(
    "terabox_public_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):

    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("📥 Download")],
            [KeyboardButton("ℹ️ About"), KeyboardButton("❓ Help")]
        ],
        resize_keyboard=True
    )

    await message.reply(
        "🚀 Welcome!\nSend any public TeraBox link.",
        reply_markup=keyboard
    )

@app.on_message(filters.text)
async def handle_text(client, message):

    text = message.text.strip()
    url_lower = text.lower()

    if any(domain in url_lower for domain in TERABOX_DOMAINS):

        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⬇ Download File", url=text)]
            ]
        )

        await message.reply(
            "✅ Link Detected!\nClick below:",
            reply_markup=keyboard
        )
    else:
        await message.reply("❌ Unsupported link.")

print("Bot is running...")
app.run()
