from telebot import types


markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add(types.KeyboardButton('Привет👋'),
           types.KeyboardButton('Отправить номер телефона', request_contact=True),
           types.KeyboardButton('Отправить геолокацию', request_location=True))
