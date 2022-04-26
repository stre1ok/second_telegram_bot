import telebot
from telebot import types

bot = telebot.TeleBot("5112916900:AAH3sDGJ1LYO0LmBNRM1BPBaXHbRkLYqWmI")
#
name = ''
surname = ''
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, "Ну привет")
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Write your name")
        bot.register_next_step_handler(message, name_registration)

def name_registration(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Write your surname')
    bot.register_next_step_handler(message, surname_registration)

def surname_registration(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Write your age')
    bot.register_next_step_handler(message, age_registration)

def age_registration(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Only integer numbers!')

bot.polling()
