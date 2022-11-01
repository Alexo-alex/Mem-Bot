import telebot
import random

TOKEN = 'ваш токен'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/1.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "Привіт, я бот, створенний для того щоб підняти твій настрій!")


@bot.message_handler(content_types=['text'])
def send_mem(message):
    text = message.text.lower()
    if 'як справи' in text:
        sti_1 = open('static/2.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif 'норм' in text:
        sti_2 = open('static/3.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti_2)
    elif 'хочу мем' in text:
        num = random.randrange(4, 12)
        sti_mem = open(f'static/{num}.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti_mem)
    elif 'бувай' in text:
        sti_3 = open('static/16.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti_3)
    else:
        sti_3 = open('static/15.jpg', 'rb')
        bot.send_sticker(message.chat.id, sti_3)


bot.polling(none_stop=True)
