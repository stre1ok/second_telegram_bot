import telebot

bot = telebot.TeleBot("5112916900:AAH3sDGJ1LYO0LmBNRM1BPBaXHbRkLYqWmI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
print('Hello, git')
