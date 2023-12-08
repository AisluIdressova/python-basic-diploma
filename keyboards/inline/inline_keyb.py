from telebot import types



inline_markup = types.InlineKeyboardMarkup()
inline_markup.row(types.InlineKeyboardButton('Найти аэропорты городов', callback_data='search'),
           types.InlineKeyboardButton('Посмотреть историю запросов', callback_data='lookup'))
