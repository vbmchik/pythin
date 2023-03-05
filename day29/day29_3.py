import telebot
from telebot import types

bot = telebot.TeleBot("5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM")


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Button1")
    item2 = types.KeyboardButton("Button2")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(   
        m.chat.id, "Check buttons funtionality", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "чего вам надо?"
    if message.text.strip() == "Button1":
        answer = "вы нажали кнопку 1"
    if message.text.strip() == "Button2":
        answer = "Кнопка 2"
    bot.send_message(message.chat.id, answer)


bot.polling(non_stop=True, interval=0)
