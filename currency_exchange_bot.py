import telebot
import requests
import config
from telebot import types

# Создание бота
bot = telebot.TeleBot(config.token)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('VND --> USD')
    btn2 = types.KeyboardButton('VND --> KGS')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'VND Convertor to KGS , USD:', reply_markup=markup)

    
@bot.message_handler(func=lambda message: message.text == 'VND --> USD')
def handle_btn1(message):
    bot.send_message(message.chat.id, 'Введите число для вычисления валюты:')
    bot.register_next_step_handler(message, calculate_btn1)


def calculate_btn1(message):
    try:
        number = int(message.text)
        converter = number / 23000
        bot.send_message(message.chat.id, f"Converting {number} equal to {converter}")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число.")



@bot.message_handler(func=lambda message: message.text == 'VND --> KGS')
def btn2(message):
    bot.send_message(message.chat.id, 'Введите число для вычисления валюты:')
    bot.register_next_step_handler(message, calculate_btn2)


def calculate_btn2(message):
    try:
        number = int(message.text)
        converter = number * 0.003724
        bot.send_message(message.chat.id, f"Converting {number} equal to {converter}")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число.")


# Запуск бота
bot.polling()


