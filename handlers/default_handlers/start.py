from telebot import types

from tg_api.util.core import bot
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