import telebot  # مكتبة التعامل مع تيليجرام

7895482872:AAGpz3mO84SPPwZWS_38QCmXve1r2ikhm1w
TELEGRAM_BOT_TOKEN = 7895482872:AAGpz3mO84SPPwZWS_38QCmXve1r2ikhm1w

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# 🔹 عندما يرسل المستخدم رسالة، يرد عليه البوت
@bot.message_handler(func=lambda message: True)
def chat_with_user(message):
    bot.reply_to(message, "🤖 مرحبًا! كيف يمكنني مساعدتك؟")

# 🔹 تشغيل البوت
print("✅ البوت يعمل الآن...")
bot.polling()
