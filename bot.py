from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8146540311:AAEHNvISpd2tBr7BlAWrPedDwTT14VypOHo"

# Restoran menyusi
menu = {
    "Osh": "25 000 so'm",
    "Lag'mon": "30 000 so'm",
    "Manti": "28 000 so'm",
    "Shashlik": "22 000 so'm",
    "Somsa": "8 000 so'm"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[item] for item in menu.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🍽 Restoran menyusiga xush kelibsiz!\nOvqatni tanlang:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in menu:
        narx = menu[text]
        await update.message.reply_text(f"✅ {text} narxi: {narx}")
    else:
        await update.message.reply_text("❌ Iltimos menyudan tanlang.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot ishga tushdi...")
app.run_polling()