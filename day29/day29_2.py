# Token: 5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM

import telebot, wikipedia


from wikigettext import getwiki

bot = telebot.TeleBot("5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM")
wikipedia.set_lang("en")

@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, "Что мне для Вас найти?")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    q = message.text
    bot.send_message(message.chat.id, getwiki(q))

bot.polling(non_stop=True,interval=0)
