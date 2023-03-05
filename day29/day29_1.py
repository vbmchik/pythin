# Token: 5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM
import telebot

bot = telebot.TeleBot("5987821865:AAGspBVM5SCN-moy07bNslGAl-zQEPliBgM")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Hello! I am Altron ready to test you abilities as a coder!")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, f"Your text: {message.text}" )

bot.polling(non_stop=True, interval=0)