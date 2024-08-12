import telebot

# Замените на ваш токен API
TOKEN = "7119506745:AAF_Sn9rDnkCYh3i23WWjaKBVQ2ldMDdL-s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()

print("What the fuck")
