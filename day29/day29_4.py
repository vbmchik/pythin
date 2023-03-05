import telebot
import os
from brain import answer
from wikigettext import getwiki

bot = telebot.TeleBot("5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM")

mas=[]
if os.path.exists( "brain.txt"):
    f = open("brain.txt", "r", encoding="UTF-8")
    for x in f:
        if(len(x.strip())>2):
            mas.append(x.strip().lower())

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(
        m.chat.id, "Давай поговорим? Задай мне вопрос")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    ans = answer(message.text, mas)
    if "wiki:::" == ans:
        ans = getwiki(message.text.lower().replace("что", "").replace(
            "такой", "").replace("кто", "").replace("такое", "").replace("такая", ""))
    bot.send_message(message.chat.id, ans)


bot.polling(non_stop=True, interval=0)
