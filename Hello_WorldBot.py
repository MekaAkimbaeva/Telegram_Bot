import telebot

token = "7075782608:AAGyY1CeeyTv_djd8AO5ujswHvbHxYqPscE"

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message):
    text = message.text
    user = message.chat.id

    if text == "Hello":
        bot.send_message(user, "World")
    else:
        bot.send_message(user, "I am helloing only to word 'Hello' ")

if __name__ == '__main__':
     bot.infinity_polling()
