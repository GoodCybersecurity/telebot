import telebot
from telegram.ext import Updater, CommandHandler
import requests
import json


my_id = '745929732'
token = '1699716991:AAFECEzWLZnPGZVIvbd1_qv_dxCcLM6PhTY'
bot = telebot.TeleBot(token)


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add('1️⃣Чому ми?', '2️⃣Контакти')
keyboard.add('3️⃣Ціни', '4️⃣Місце знаходження')
#,#'4️⃣Перезвонити')
keyboard.add('0️⃣Завершити')

def send(id, text):
    bot.send_message(id, text, reply_markup = keyboard)
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name == None:
        send_mess = f"<b>Привіт👋 {message.from_user.first_name}.Чим можу допомогти?</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup = keyboard)
    else:
        send_mess = f"<b>Привіт👋 {message.from_user.first_name} {message.from_user.last_name}.Чим можу допомогти?</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup = keyboard)

#@bot.message_handler(commands=["phone"])
#def phone(message):
    #keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    #button_phone = types.KeyboardButton(text="☎️Відправити свій номер телефона", request_contact=True)
    #button_back = types.KeyboardButton(text="⬅️Назад")
    #keyboard.add(button_phone, button_back)
    #bot.send_message(message.chat.id,"Відправьте свій номер телефону,щоб ми могли з вами звязатися в найближчий час.",parse_mode='html')
@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == '1️⃣Чому ми?':
        send(message.chat.id, 'Ми пропонуємо:\n'
                              '- Догляд за дітьми у віці від 3 років\n'
                              '- Тільки у нас заняття і розваги проходять виключно англійською мовою\n'
                              '- Професійні вихователі\n'
                              '- Нові, безпечні та сертифіковані іграшки\n'
                              '- I та II зміна, можливість погодинного перебування дитини\n'
                              'Вивчаємо англійську розважаючись!')
    elif msg == '2️⃣Контакти':
        send(id, 'Номер телефону: +380634047039')
    elif msg == '3️⃣Ціни':
        send(id, 'Одна зміна - 4000 грн/місяць\n'
                 'Одна зміна - 220 грн/день\n'
                 'Почасове перебування - 100 грн/год')
    #elif msg == '4️⃣Перезвонити':
        #send(id, 'Введіть команду /phone')
        #bot.forward_message(my_id, message.chat.id, message.message_id)
        #bot.send_message(message.chat.id, "Повідомлення відправлено,оператор найближчим часом вам зателефонує!")
    elif msg == '4️⃣Місце знаходження':
        send(id, 'Софіївська Борщагівка, вул. Кошова, 110, прим. 108')
    elif msg == '0️⃣Завершити':
        send(id, 'Дякую за звернення.Всього найкращого! ❤️')

bot.polling(none_stop=True)