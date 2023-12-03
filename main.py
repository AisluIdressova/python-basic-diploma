from telebot import types

from database.common.models import User, db
from site_API.core import site_api, url, headers, querystring
from database.core import crud
from tg_api.util.core import bot

import datetime


@bot.message_handler(commands=['start'])
def say_hello(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Привет👋'),
               types.KeyboardButton('Отправить номер телефона', request_contact=True),
               types.KeyboardButton('Отправить геолокацию', request_location=True))
    bot.reply_to(message, f'<b>Добро пожаловать, {message.from_user.first_name}\n'
                          f'Меня зовут - AirportCityFinderBot\n'
                          f'Я умею находить название всех аэропортов\n'
                          f'выбранного города</b>', parse_mode='html', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

def on_click(message):
    bot.reply_to(message, 'Мои возможности', reply_markup=types.ReplyKeyboardRemove())
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('Найти аэропорты городов', callback_data='search'),
               types.InlineKeyboardButton('Посмотреть историю запросов', callback_data='lookup'))
    bot.reply_to(message, 'Выберите действие', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'search')
def searching_airport(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    bot.reply_to(callback.message, 'Напишите название города')


@bot.message_handler(func=lambda message: True)
def checker(message):
    check_api = site_api.get_info()
    result = check_api(url, headers, querystring, message.text)
    if not result:
        bot.reply_to(message,'Ошибка! Попробуйте заново.')
    else:
        bot.reply_to(message, result)
        bot.send_message(message.chat.id, 'Напишите следующий город или начните сначала /start')
    db_write = crud.create()
    now = datetime.datetime.now()
    current_time = now.strftime("%H-%M-%S  %d/%m/%Y")
    data = [{'message': message.text, 'date': current_time}]
    db_write(db, User, *data)


@bot.callback_query_handler(func=lambda call: call.data == 'lookup')
def retrieving_info(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                          text='Выберите действие', reply_markup=None)
    show_info = crud.retrieve()
    result = show_info(db, User)
    bot.reply_to(callback.message, result)



if __name__ == '__main__':
    bot.infinity_polling()
