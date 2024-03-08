import telebot 

token = "6518751357:AAEe0rsaSM_JJqYPq9XFLvmQIV6GZZAW4b8"

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def start_bot(message):

    user = message.chat.id
    bot.send_message(user , "Say something so I can repeat after you.")


@bot.message_handler(content_types=["text"])
def user_message(message):

    text = message.text
    user = message.chat.id

    bot.send_message(user,text)

    bot.send_photo(user,"https://w.forfun.com/fetch/71/7117a465603218834b5afd8f06c7209b.jpeg")

if __name__ == '__main__':
    bot.polling(none_stop=True)








# import telebot
# import random

# token = "6107755679:AAFZ9VB2Fif6ygIQc83Fj3k9advYBEtbiY8"
# bot = telebot.TeleBot(token=token)
# stickers = []

# @bot.message_handler(content_types=['sticker'])
# def echo(message):
#     user = message.chat.id
#     sticker = message.sticker.file_id

#     stickers.append(sticker)

#     bot.send_sticker(user,random.choice(stickers))

# bot.polling(none_stop=True)