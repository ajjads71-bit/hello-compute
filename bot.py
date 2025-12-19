from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("✅ البوت شغال")

app = ApplicationBuilder().token("8537568402:AAHXW0gSYoBeZCIKokWgWXJGqKpg5mKj4N8").build()
app.add_handler(CommandHandler("start", start))

print("running")
app.run_polling()
