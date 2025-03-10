import telebot  #  مكتبة التعامل مع التيليجرام
TELEGRAM_BOT_TOKEN =

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# 🔹 عندما يرسل المستخدم رسالة، يرد عليه البوت
@bot.message_handler(func=lambda message: True)
def chat_with_user(message):
    bot.reply_to(message, "🤖 مرحبًا! كيف يمكنني مساعدتك؟")

# 🔹 تشغيل البوت
print("✅ البوت يعمل الآن...")
bot.polling()
