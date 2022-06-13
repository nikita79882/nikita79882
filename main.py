#from email import message
from urllib.request import URLopener
import telebot
from telebot import types

bot = telebot.TeleBot('5523686045:AAHBnTY-8SXfHYACUB5Kd79Bngj1wRkbazU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')  
  
#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    if message.text == "Привет":
#        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#   elif message.text == "id":
#        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#    elif message.text == "Фото":
#        photo = open('rkeep.png', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    else:
#         bot.send_message(message.chat.id, "Я тебя не понимаю((", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вай, крутое фото!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup("Go to Web-site", url="https://docs.rkeeper.ru"))
    bot.send_message(message.chat.id, 'Go to Web-site', perly_markup=markup)

bot.polling(none_stop=True)