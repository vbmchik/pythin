import telebot
from solver import solve

bot = telebot.TeleBot("5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Please enter what you want to calculate!")
    

@bot.message_handler(content_types=["text"])
def handle_text(message):
    try:
        s = solve(message.text)
        bot.send_message(message.chat.id, s)
    except Exception as e:
        bot.send_message(message.chat.id, repr(e))


bot.polling(non_stop=True, interval=0)
