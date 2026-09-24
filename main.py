import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

main_keyboard = [["📄 CV","📝 Lettre"],["📞 Contact","🏢 Orinasa"]]
main_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)

async def start(update, context):
    await update.message.reply_text("Salama! 👋\nTongasoa ao @AsasyEzaka_bot 🇲🇬\n\nFidio:", reply_markup=main_markup)

async def handle(update, context):
    text = update.message.text
    if text == "📄 CV":
        kb = [["🎓 Manana Diplaoma","💪 Tsy manana Diplaoma"],["🔙 Miverina"]]
        await update.message.reply_text("Manana diplaoma?", reply_markup=ReplyKeyboardMarkup(kb, resize_keyboard=True))
    elif "Diplaoma" in text:
        await update.message.reply_text(f"Voaray: {text}\nAnarana, Diplaoma, Traikefa alefaso amboariko PDF! 📄", reply_markup=main_markup)
    elif text == "🔙 Miverina":
        await update.message.reply_text("Fidio:", reply_markup=main_markup)
    else:
        await update.message.reply_text("Tsindrio bokotra ambany 👇", reply_markup=main_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
